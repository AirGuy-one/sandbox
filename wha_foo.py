import pandas as pd

# Define the data
data = {
    '1': ['Иван Гутяк', 'Вячеслав Цочивли', 'Максим Чушко'],
    '2': ['']*3,
    '3': ['777-694-6944:N', '517-058-2076:Y', '847-349-4551:N'],
    '4': ['Иван Гутяк', 'Вячеслав Цочивли', 'Максим Чушко']
}

df = pd.DataFrame(data)
df_transposed = df.T
df_transposed = df_transposed.drop_duplicates(keep='first')
df_no_duplicates = df_transposed.T

print("\nDataFrame after removing duplicate columns:")
print(df_no_duplicates)
