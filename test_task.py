import pandas as pd

# Загрузка данных из Excel-файла
borrowers_df = pd.read_excel("loans.xlsx", sheet_name="Borrowers")
loans_df = pd.read_excel("loans.xlsx", sheet_name="Loans")

# Фильтрация заемщиков, зарегистрированных в 2021 году или ранее
borrowers_before_2022 = borrowers_df[borrowers_df['registration_date'].dt.year <= 2021]

# Фильтрация займов с рейтингом <= 12
loans_rating_12_or_lower = loans_df[loans_df['rating'] <= 12]

# Объединение данных о займах и заемщиках по borrower_id
merged_data = pd.merge(loans_rating_12_or_lower, borrowers_before_2022, on='borrower_id', how='inner')

# Совокупный объем всех займов
total_amount = merged_data['amount'].sum()

print("Совокупный объем всех займов с рейтингом <= 12 для компаний, зарегистрированных в 2021 году или ранее:", total_amount)
