import pandas as pd

# Creating a sample CSV first
pd.DataFrame({"Name": ["Rafia", "Azka"], "Age": [20, 19]}).to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")
print(f"Original Data:\n{df}")

df["Age"] = df["Age"] + 1          # Modify data
df["Course"] = ["BCA", "BCA"]      # Add column
df = df.drop("Name", axis=1)       # Delete column

df.to_csv("updated_data.csv", index=False)
print(f"Updated Data Saved:\n{df}")