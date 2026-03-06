import pandas as pd

#Creating a simple excel table using pandas
#sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24,36,50],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

#save the excel
df.to_excel("students.xlsx", index=False)

print("Excel file created successfully")
print(df.head())
print(type(data))
print(data["Name"])
