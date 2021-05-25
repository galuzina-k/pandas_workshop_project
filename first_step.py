import pandas as pd
import re
df = pd.read_csv("~/Desktop/PYCHARM/PyCharmProjects/pandas__workshop/pokemon_data.csv")
# # Print HEADERS
# print(df.columns)

# # Read each Column
# print(df[["Name", "Type 1", "HP"]])
#
# # Read each Row
# print(df.iloc[0:4])

# # Read a specific location(ROW, Column)
# print(df.iloc[2, 1])

# for index, row in df.iterrows():
#     print(index, row["Name"])

# print(df.loc[df["Type 1"] == "Fire"])

# df.describe()

# print(df.sort_values(["Type 1", "HP"], ascending=True))

# df["Total"] = df.iloc[:, 4:10].sum(axis=1)
#
# df = df.drop(columns=["Total"])
# cols = list(df.columns)
# df = df[cols[0:4] + [cols[-1]]+cols[4:12]]
# df.to_csv("~/Desktop/PYCHARM/PycharmProjects/pandas__workshop/modified.csv", index=False)
# df.to_excel("~/Desktop/PYCHARM/PycharmProjects/pandas__workshop/modified.xlsx", index=False)

# FILTERING DATA
# new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]
# new_df = new_df.reset_index(drop=True)
# new_df.to_csv("~/Desktop/PYCHARM/PycharmProjects/pandas__workshop/new.csv")
# print(df.loc[~df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)])
# print(df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)])
# df.loc[df['Type 1'] == "Fire", "Type 1"] = "Flamer"
# df.loc[df['Type 1'] == "Fire", "Legendary"] = True
# print(df)
# df = pd.read_csv("~/Desktop/PYCHARM/PyCharmProjects/pandas__workshop/pokemon_data.csv")
# df.loc[df["HP"] > 500, ["Generation", "Legendary"]] = "TEST"
# print(df)
# df = pd.read_csv("~/Desktop/PYCHARM/PyCharmProjects/pandas__workshop/pokemon_data.csv")
# df.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False)
# df["count"]= 1
# df.groupby(["Type 1", "Type 2"]).sum()/count()["count"]

# Working with LARGE FILES

# pd.read_csv("modified.csv", chunksize=5)
# new_data = pd.DataFrame(columns=df.columns)
