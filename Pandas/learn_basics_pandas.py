import pandas as pd 
import numpy as np

print("Pandas Basics")

print("\n1 Creating Series")

s = pd.Series([10,20,30,40,50,60,70,80,90,100])

print(s)

print("\n2. Creating DataFrame ")

data = {
    "Name": ["Uday", "Shubham", "Harsh"],
    "Age": [21, 20, 22],
    "Marks": [85, 90, 88]
}

# df = pd.DataFrame(data)
# print(df)

print("data frame to CSV")
# df.to_csv("data1.csv", index=False)
df2 = pd.read_csv("data1.csv")
print(df2)

df = pd.read_csv("data.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df["Name"])
print(df[["Name", "Marks"]])

print("\n===== 6. Row Selection =====")
print(df.iloc[0])      # by index
print(df.loc[0])       # by label


print("\n===== 7. Filtering")
print(df[df["Marks"] > 85])


df.loc[0, "Marks"] = 95
print(df)

print("\n===== 10. Dropping Column =====")
df = df.drop("Grade", axis=1)
print(df)


print("\n===== 11. Handling Missing Data =====")
df.loc[[1, 3, 5], "City"] = np.nan

df["City"] = np.nan 
print("\nDrop NA:")
print(df.dropna())

print("\nFill NA:")
print(df.fillna("Unknown"))

print("\n===== 12. Sorting =====")
print(df.sort_values(by="Marks", ascending=False))

print("\n===== 13. GroupBy =====")
group = df.groupby("Name")["Marks"].mean()
print(group)

print("\n===== 14. Merge DataFrames =====")
df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Apex", "Chiku"]})
df2 = pd.DataFrame({"ID": [1, 2], "Marks": [95, 90]})
merged = pd.merge(df1, df2, on="ID")
print(merged)

print("\n===== 15. Apply Function =====")
df["Marks"] = df["Marks"].apply(lambda x: x + 5)
print(df)

print("\n===== 16. Unique & Value Counts =====")
print(df["Name"].unique())
print(df["Name"].value_counts())