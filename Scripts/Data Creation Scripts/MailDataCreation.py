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

# Generate synthetic EDI formatted data
def generate_edi_data(num_records=100):
    edi_records = []
    for _ in range(num_records):
        product_base = random.choice(product_master)
        product_variant = random.choice(product_variations[product_base])
        sku = f"{product_base[:3].upper()}-{random.randint(1000, 9999)}-{random.choice('ABCDEFG')}"
        order_id = fake.uuid4()
        order_date = fake.date_this_year()
        # Convert the datetime.date to a string with the desired format
        order_date_str = order_date.strftime('%Y%m%d')
        price = round(random.uniform(50, 1500), 2)
        quantity = int(random.randint(1, 10))
        category = fake.random_element(elements=("Electronics", "Wearables", "Computers", "Accessories"))
        location = fake.city()
        retailer_id = int(fake.random_int(min=10000, max=99999))
        supplier_id = int(fake.random_int(min=10000, max=99999))
        edi_type = random.choice(["810", "867"])  # Invoice or POS Sales Data
        if edi_type == "810":  # EDI 810 - Invoice
#             print(810)
            edi_record = f"ISA*00*          *00*          *12*{supplier_id}*12*{retailer_id}*{order_date_str}*1200*U*00401*000000001*0*P*>~\n" \
                         f"GS*IN*{supplier_id}*{retailer_id}*{order_date_str}*1200*1*X*004010~\n" \
                         f"ST*810*0001~\n" \
                         f"BIG*{order_date_str}*{order_id}*{order_date_str}*PO{random.randint(10000, 99999)}~\n" \
                         f"N1*ST*Retailer Store {retailer_id}*92*{retailer_id}~\n" \
                         f"IT1*1*{quantity}*EA*{price}**UP*{sku}~\n" \
                         f"TDS*{(price * quantity * 100)}~\n" \
                         f"PNAME*{product_variant}"\
                         f"SE*8*0001~\n" \
                         f"GE*1*1~\n" \
                         f"IEA*1*000000001~"
        else:  # EDI 867 - POS Sales Data
            # Now use the formatted string in the f-string
            edi_record = f"ISA*00*          *00*          *12*{retailer_id}*12*{supplier_id}*{order_date_str}*1200*U*00401*000000002*0*P*>~\n" \
                          f"GS*PT*{retailer_id}*{supplier_id}*{order_date_str}*1200*2*X*004010~\n" \
                          f"ST*867*0002~\n" \
                          f"BPT*00*POS{random.randint(10000, 99999)}*{order_date_str}~\n" \
                          f"N1*ST*Retailer Store {retailer_id}*92*{retailer_id}~\n" \
                          f"LIN**UP*{sku}~\n" \
                          f"QTY*32*{quantity}~\n" \
                          f"PNAME*{product_variant}"\
                          f"SE*6*0002~\n" \
                          f"GE*1*2~\n" \
                          f"IEA*1*000000002~"

        
        edi_records.append(edi_record)
    return edi_records



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
        location = fake.city()
        
        # Append to dataset
        data.append({
            "order_id": fake.uuid4(),
            "order_date": order_date,
            "product_name": product_variant,
            "sku": sku,
            "price": price,
            "quantity": quantity,
            "category": category,
            "location": location
        })
    
    return pd.DataFrame(data)

random_file_format = random.randint(0,1)
if random_file_format==1:
    # Generate and save data to CSV
    df = generate_data(1000)
    outputfilename = f"{pd.to_datetime(datetime.now()).strftime('%b_%d')}sales_transactions__W{pd.to_datetime(datetime.now()).strftime('%U')}.xml"
    df.to_xml(outputfilename, index=False)
else:
# Generate EDI formatted data
    edi_data = generate_edi_data(1000)
    # Save to file
    outputfilename = f"{pd.to_datetime(datetime.now()).strftime('%b_%d_%H_%M_%S')}sales_transactions_edi__W{pd.to_datetime(datetime.now()).strftime('%U')}.txt"
    with open(outputfilename, "w") as file:
        file.write("\n".join(edi_data))

    
print('Mail_Filename')
print(outputfilename)         