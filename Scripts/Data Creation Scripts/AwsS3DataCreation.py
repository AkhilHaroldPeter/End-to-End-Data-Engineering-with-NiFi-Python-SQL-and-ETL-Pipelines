
# import random
# import pandas as pd
# from faker import Faker
# from datetime import datetime

# # Initialize Faker
# fake = Faker()
# st = datetime.now()
# # Define product master and variations
# product_master = [
#     "iPhone 13",
#     "Samsung Galaxy S21",
#     "Google Pixel 6",
#     "MacBook Air",
#     "Dell XPS 13",
#     "HP Spectre x360",
#     "Sony WH-1000XM4",
#     "Bose QuietComfort 45",
#     "Apple Watch Series 7",
#     "Fitbit Versa 3"
# ]

# product_variations = {
#     "iPhone 13": ["iPhone 13 Mini", "iPhone 13 Pro", "iPhone 13 Pro Max"],
#     "Samsung Galaxy S21": ["Galaxy S21 FE", "Galaxy S21 Ultra"],
#     "Google Pixel 6": ["Pixel 6 Pro", "Pixel 6a"],
#     "MacBook Air": ["MacBook Air M1", "MacBook Air M2"],
#     "Dell XPS 13": ["XPS 13 Plus", "XPS 13 Touch"],
#     "HP Spectre x360": ["Spectre x360 OLED", "Spectre x360 5G"],
#     "Sony WH-1000XM4": ["WH-1000XM4 Silver", "WH-1000XM4 Black"],
#     "Bose QuietComfort 45": ["QuietComfort 45 SE", "QuietComfort 45 Limited"],
#     "Apple Watch Series 7": ["Series 7 GPS", "Series 7 Cellular"],
#     "Fitbit Versa 3": ["Versa 3 SE", "Versa 3 Health Edition"]
# }

# # Generate synthetic data
# def generate_data(num_records=100):
#     data = []
#     for _ in range(num_records):
#         # Randomly pick a product master and variation
#         product_base = random.choice(product_master)
#         product_variant = random.choice(product_variations[product_base])
        
#         # Generate SKU
#         if random.randint(0,6) in (2,5):
#             sku = f"{product_base[:3].upper()}-{random.randint(1000, 9999)}-{random.choice('ABCDEFG')}"
#         else:
#             sku = ''
#         # Generate other data
#         order_date = fake.date_this_year()
#         price = round(random.uniform(50, 1500), 2)
#         quantity = random.randint(1, 10)
#         category = fake.random_element(elements=("Electronics", "Wearables", "Computers", "Accessories"))
#         region = fake.random_element(elements=("North America", "Europe", "Asia", "South America", "Africa"))
#         location = fake.city()
        
        
#         # Append to dataset
#         data.append({
#             "order_id": fake.uuid4(),
#             "order_date": order_date,
#             "product_name": product_variant,
#             "sku": sku,
#             "price": price,
#             "quantity": quantity,
#             "category": category,
#             "region": region,
#             "location": location
#         })
    
#     return pd.DataFrame(data)

# # Generate and save data to CSV
# df = generate_data(10000000) #1000000000   #100000
# print(datetime.now()-st)
# df.to_csv(f"sales_transactions_with_variations_and_sku_{pd.to_datetime(datetime.now()).strftime('%b_%d')}.csv", index=False)
# print(datetime.now()-st)
# print("Data generated and saved to 'sales_transactions_with_variations_and_sku.csv'")
print('S3Filename')
print('sales_transactions_with_variations_and_sku_Dec_30.csv')
