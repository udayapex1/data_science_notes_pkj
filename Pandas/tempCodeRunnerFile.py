df.to_csv("data.csv", index=False)
df2 = pd.read_csv("data.csv")
print(df2)