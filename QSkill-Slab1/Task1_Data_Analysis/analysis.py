import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("data.csv")

# Average
print("Average Sales:", data["Sales"].mean())

# ---------------- BAR CHART ----------------
plt.figure()
plt.bar(data["Product"], data["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales by Product")
plt.show()
plt.clf()   

# ---------------- SCATTER PLOT --------------
plt.figure()
plt.scatter(data["Advertising"], data["Sales"])
plt.xlabel("Advertising")
plt.ylabel("Sales")
plt.title("Advertising vs Sales")
plt.show()
plt.clf()

# 
# ---------------- HEATMAP ----------------
plt.figure()

#  only numeric columns
numeric_data = data[["Sales", "Advertising"]]

correlation = numeric_data.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.show()
plt.clf()
