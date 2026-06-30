import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sales_data.csv")

print("Original Dataset:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Sales with average
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

# Fill missing Quantity with median
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# Save cleaned data
cleaned_file = "reports/cleaned_data.csv"
df.to_csv(cleaned_file, index=False)

# Generate summary statistics
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
highest_sales = df["Sales"].max()
lowest_sales = df["Sales"].min()

# Write report
report_file = "reports/summary_report.txt"

with open(report_file, "w") as file:
    file.write("DATA CLEANING & REPORTING AUTOMATION\n")
    file.write("=" * 40 + "\n\n")
    file.write(f"Total Sales      : {total_sales:.2f}\n")
    file.write(f"Average Sales    : {average_sales:.2f}\n")
    file.write(f"Highest Sales    : {highest_sales:.2f}\n")
    file.write(f"Lowest Sales     : {lowest_sales:.2f}\n")
    file.write(f"Total Records    : {len(df)}\n")

# Create Sales Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Sales"])
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

chart_file = "reports/sales_chart.png"
plt.savefig(chart_file)

print("\nData cleaning completed successfully!")
print("Cleaned data saved to:", cleaned_file)
print("Report saved to:", report_file)
print("Chart saved to:", chart_file)