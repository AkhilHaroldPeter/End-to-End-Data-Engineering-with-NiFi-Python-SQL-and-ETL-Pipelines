import random
import pandas as pd
from faker import Faker
from datetime import datetime
import random
# Initialize Faker
fake = Faker()

# Define product master and variations
product_master = [
    "iPhone 13",
    "Samsung Galaxy S21",
    "Google Pixel 6",
    "MacBook Air",
    "Dell XPS 13",
    "HP Spectre x360",
    "Sony WH-1000XM4",
    "Bose QuietComfort 45",
    "Apple Watch Series 7",
    "Fitbit Versa 3"
]

product_variations = {
    "iPhone 13": ["iPhone 13 Mini", "iPhone 13 Pro", "iPhone 13 Pro Max"],
    "Samsung Galaxy S21": ["Galaxy S21 FE", "Galaxy S21 Ultra"],
    "Google Pixel 6": ["Pixel 6 Pro", "Pixel 6a"],
    "MacBook Air": ["MacBook Air M1", "MacBook Air M2"],
    "Dell XPS 13": ["XPS 13 Plus", "XPS 13 Touch"],
    "HP Spectre x360": ["Spectre x360 OLED", "Spectre x360 5G"],
    "Sony WH-1000XM4": ["WH-1000XM4 Silver", "WH-1000XM4 Black"],
    "Bose QuietComfort 45": ["QuietComfort 45 SE", "QuietComfort 45 Limited"],
    "Apple Watch Series 7": ["Series 7 GPS", "Series 7 Cellular"],
    "Fitbit Versa 3": ["Versa 3 SE", "Versa 3 Health Edition"]
}


# Country names and abbreviations mapping
country_full_names = {
    "North America": ["United States of America", "Canada", "Mexico"],
    "Europe": ["United Kingdom", "Germany", "France", "Italy", "Spain"],
    "Asia": ["China", "India", "Japan", "South Korea", "Singapore"],
    "South America": ["Brazil", "Argentina", "Chile"],
    "Africa": ["Nigeria", "South Africa", "Kenya"]
}

country_abbreviations = {
    "North America": ["USA", "CAN", "MEX"],
    "Europe": ["UK", "DE", "FR", "IT", "ES"],
    "Asia": ["CN", "IN", "JP", "KR", "SG"],
    "South America": ["BR", "AR", "CL"],
    "Africa": ["NG", "ZA", "KE"]
}

# Country and cities mapping
region_city_mapping = {
    "United States of America": ["New York", "Los Angeles", "Chicago"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "Mexico": ["Mexico City", "Guadalajara", "Monterrey"],
    "United Kingdom": ["London", "Manchester", "Birmingham"],
    "Germany": ["Berlin", "Munich", "Frankfurt"],
    "France": ["Paris", "Lyon", "Marseille"],
    "Italy": ["Rome", "Milan", "Naples"],
    "Spain": ["Madrid", "Barcelona", "Seville"],
    "China": ["Beijing", "Shanghai", "Shenzhen"],
    "India": ["Mumbai", "Delhi", "Bangalore"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"],
    "South Korea": ["Seoul", "Busan", "Incheon"],
    "Singapore": ["Singapore"],
    "Brazil": ["Sao Paulo", "Rio de Janeiro", "Brasilia"],
    "Argentina": ["Buenos Aires", "Cordoba", "Rosario"],
    "Chile": ["Santiago", "Valparaiso", "Concepcion"],
    "Nigeria": ["Lagos", "Abuja", "Kano"],
    "South Africa": ["Johannesburg", "Cape Town", "Durban"],
    "Kenya": ["Nairobi", "Mombasa", "Kisumu"],
    "USA": ["New York", "Los Angeles", "Chicago"],
    "CAN": ["Toronto", "Vancouver", "Montreal"],
    "MEX": ["Mexico City", "Guadalajara", "Monterrey"],
    "UK": ["London", "Manchester", "Birmingham"],
    "DE": ["Berlin", "Munich", "Frankfurt"],
    "FR": ["Paris", "Lyon", "Marseille"],
    "IT": ["Rome", "Milan", "Naples"],
    "ES": ["Madrid", "Barcelona", "Seville"],
    "CN": ["Beijing", "Shanghai", "Shenzhen"],
    "IN": ["Mumbai", "Delhi", "Bangalore"],
    "JP": ["Tokyo", "Osaka", "Kyoto"],
    "KR": ["Seoul", "Busan", "Incheon"],
    "SG": ["Singapore"],
    "BR": ["Sao Paulo", "Rio de Janeiro", "Brasilia"],
    "AR": ["Buenos Aires", "Cordoba", "Rosario"],
    "CL": ["Santiago", "Valparaiso", "Concepcion"],
    "NG": ["Lagos", "Abuja", "Kano"],
    "ZA": ["Johannesburg", "Cape Town", "Durban"],
    "KE": ["Nairobi", "Mombasa", "Kisumu"]
}

# Generate synthetic data
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        # Randomly pick a product master and variation
        product_base = random.choice(product_master)
        product_variant = random.choice(product_variations[product_base])
        
        # Generate SKU
        sku = f"{product_base[:3].upper()}-{random.randint(1000, 9999)}-{random.choice('ABCDEFG')}"
        
        # Generate other data
        order_date = fake.date_this_year()
        price = round(random.uniform(50, 1500), 2)
        quantity = random.randint(1, 10)
        category = fake.random_element(elements=("Electronics", "Wearables", "Computers", "Accessories"))
        region = fake.random_element(elements=("North America", "Europe", "Asia", "South America", "Africa"))
        
        # Pick a country and city and randomly decide between full name or abbreviation for country
        is_abbreviation = random.choice([True, False])
        if is_abbreviation:
            country = random.choice(country_abbreviations[region])
        else:
            country = random.choice(country_full_names[region])
        
        city = random.choice(region_city_mapping[country]) 
        # Append to dataset
        data.append({
            "order_id": fake.uuid4(),
            "order_date": order_date,
            "product_name": product_variant,
            "sku": sku,
            "price": price,
            "quantity": quantity,
            "category": category,
            "region": region,
            "country": country,
            "location": city
        })
    
    return pd.DataFrame(data)

# Generate and save data to CSV
df = generate_data(1000)

# Random_file_format will be a random flag depending on which the file format will be decided.
random_file_format = random.randint(0,1)
if random_file_format==0:
    outputfilename = f"{pd.to_datetime(datetime.now()).strftime('%Y_%m_%d__%H_%M_%S%f')}_sales_transactions_storedata.json"
    df.to_json(outputfilename, index=False)
else:
    outputfilename = f"{pd.to_datetime(datetime.now()).strftime('%Y_%m_%d__%H_%M_%S%f')}_sales_transactions_storedata.xlsx"
    df.to_excel(outputfilename, index=False, startrow=random.randint(0,20), startcol=random.randint(0,7)) 

    
print('sftp_local_Filename')
print(outputfilename)   
# print("Data generated and saved to 'sales_transactions_with_variations_and_sku.csv'")


