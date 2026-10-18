#info() .shape .descripe()
import pandas as pd

#Створюємо словник
store_data = {
    "item_id": [1, 2, 3, 4, 5, 6],
    "item_name": ["Навушники", "Ноутбук", "Шафа", "Продукти", "Крісло", "Холодильник"],
    "category": ["Техніка", "Техніка", "Меблі", "Їжа", "Меблі", "Техніка"],
    "price": [2200, 50000, 5000, 1000, 1300, 18000],
    "stock": [5, 20, 13, 120, 378, 12]
}

#Перетворюємо у двовимірну структуру даних зі рядками та стовпцями 
store_df = pd.DataFrame(store_data)
store_df.to_csv('store_inventory.csv', index=False) #Зберігаємо таблицю у різні розширення файлів це окремі 2 файли 
store_df.to_excel('store_inventory.xlsx', index=False)

#Зчитуємо файли
df_csv = pd.read_csv('store_inventory.csv')
df_excel = pd.read_excel('store_inventory.xlsx')

#Вивід 
print('-' * 30)
print("Перші 2 рядки у таблиці з розширенням csv:", df_csv.head(2))
print('-' * 30)
print("Розмірність таблиці з розширенням excel:", df_excel.shape)
print('-' * 30)
print("Технічна інформація про таблицю з розширенням excel:", df_excel.info())
print('-' * 30)
print("Математична статистика для таблиці з розширенням excel:", df_excel.describe())


