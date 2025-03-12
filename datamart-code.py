# Importing Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Initialization
branches = ["Branch A", "Branch B", "Branch C", "Branch D"]
monthly_revenue = np.random.randint(30000, 150000, size=(12, len(branches)))
monthly_expenses = np.random.randint(20000, 100000, size=(12, len(branches)))
employee_satisfaction = np.random.uniform(3.0, 5.0, size=len(branches))

# Key Metrics
annual_revenue_per_branch = monthly_revenue.sum(axis=0)
total_annual_revenue = monthly_revenue.sum()
avg_employee_satisfaction = employee_satisfaction.mean()

# Branch Categorization
def categorize_branch(revenue):
    if revenue > 1_000_000:
        return "Excellent"
    elif 500_000 <= revenue <= 1_000_000:
        return "Good"
    else:
        return "Needs Improvement"

branch_categories = [categorize_branch(rev) for rev in annual_revenue_per_branch]
branch_data = pd.DataFrame({
    "Branch": branches,
    "Annual Revenue": annual_revenue_per_branch,
    "Category": branch_categories
})

# Net Income Calculation
def calculate_net_income(revenue, expenses):
    return revenue - expenses

net_income_per_month = calculate_net_income(monthly_revenue, monthly_expenses)

# Revenue Data Extraction
second_quarter_revenue = monthly_revenue[3:6, :]
last_three_months_revenue = monthly_revenue[-3:, :]
avg_monthly_revenue = monthly_revenue.mean(axis=1)
high_revenue_months = monthly_revenue > 100_000
projected_revenue_next_year = monthly_revenue * 1.1
combined_revenue = np.concatenate((monthly_revenue, projected_revenue_next_year), axis=0)

# Visualizations

# 1. Monthly Revenue Trend of Top-Performing Branch
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue[:, np.argmax(annual_revenue_per_branch)], marker='o')
plt.title("Monthly Revenue Trend of Top-Performing Branch")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.savefig("line_plot_top_branch.png")
plt.show()

# 2. Total Annual Revenue by Branch
plt.figure(figsize=(10, 6))
plt.bar(branches, annual_revenue_per_branch, color='skyblue')
plt.title("Total Annual Revenue by Branch")
plt.xlabel("Branches")
plt.ylabel("Revenue ($)")
plt.savefig("bar_chart_annual_revenue.png")
plt.show()

# 3. Revenue Contribution by Branch
plt.figure(figsize=(8, 8))
plt.pie(annual_revenue_per_branch, labels=branches, autopct="%1.1f%%", startangle=140)
plt.title("Revenue Contribution by Branch")
plt.savefig("pie_chart_revenue_contribution.png")
plt.show()

# 4. Employee Satisfaction vs. Branch Profit
branch_profits = annual_revenue_per_branch - monthly_expenses.sum(axis=0)
plt.figure(figsize=(10, 6))
plt.scatter(employee_satisfaction, branch_profits, c='orange', edgecolors='k', s=100)
plt.title("Employee Satisfaction vs. Branch Profit")
plt.xlabel("Employee Satisfaction")
plt.ylabel("Profit ($)")
plt.savefig("scatter_plot_satisfaction_vs_profit.png")
plt.show()

# 5. Dashboard with Multiple Visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes[0, 0].plot(monthly_revenue[:, np.argmax(annual_revenue_per_branch)], marker='o')
axes[0, 0].set_title("Top Branch Revenue Trend")
axes[0, 1].bar(branches, annual_revenue_per_branch, color='skyblue')
axes[0, 1].set_title("Annual Revenue by Branch")
axes[1, 0].pie(annual_revenue_per_branch, labels=branches, autopct="%1.1f%%")
axes[1, 0].set_title("Revenue Contribution")
axes[1, 1].scatter(employee_satisfaction, branch_profits, c='orange', edgecolors='k')
axes[1, 1].set_title("Satisfaction vs Profit")
plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

# DataFrame Operations
data = pd.DataFrame({
    "Branch": branches,
    "Annual Revenue": annual_revenue_per_branch,
    "Total Expenses": monthly_expenses.sum(axis=0),
    "Employee Satisfaction": employee_satisfaction
})
data["Net Income"] = data["Annual Revenue"] - data["Total Expenses"]
data["Profit Margin"] = (data["Net Income"] / data["Annual Revenue"]) * 100
filtered_data = data[data["Annual Revenue"] > 750_000]
sorted_data = data.sort_values(by="Employee Satisfaction", ascending=False)
data.to_csv("datamart_analysis.csv", index=False)
