#Creating an excel file
import pandas as pd

#sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24,36,50],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

df.to_excel("employees.xlsx", index=False)
print(df)