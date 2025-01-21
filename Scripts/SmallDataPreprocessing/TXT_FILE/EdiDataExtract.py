import pandas as pd

def detect_edi_type(file_path):
    """
    Detects whether the given EDI file is an 810 (Invoice) or 867 (POS Sales Data).
    Returns '810' or '867' accordingly.
    """
    with open(file_path, 'r') as file:
        content = file.read()
        
    if "ST*810" in content:
        print('810')
        return "810"  # Invoice
    elif "ST*867" in content:
        print('867')
        return "867"  # POS Sales Data
    else:
        return "Unknown"

def parse_edi_810(file_path):
    """
    Parses an EDI 810 (Invoice) file and extracts structured data.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data = []
    order_id = None
    order_date = None
    price = None
    quantity = None
    sku = None
    product_name = None

    for line in lines:
        segments = line.strip().split("*")
        
        if segments[0] == "BIG":  # Invoice Header
            order_date = segments[1]
            order_id = segments[2]
        
        elif segments[0] == "IT1":  # Line Item
            quantity = int(segments[2])
            price = float(segments[4])
            sku = segments[-1][:-1]  # Extract SKU
            
        elif segments[0] == "PNAME":
            product_name = segments[1]            
        
        if order_id and price and quantity and sku:
            data.append({
                "product_name" : product_name,
                "order_id": order_id,
                "order_date": order_date,
                "sku": sku,
                "quantity": quantity,
                "price": price
            })
    
    return pd.DataFrame(data)

def parse_edi_867(file_path):
    """
    Parses an EDI 867 (POS Sales Data) file and extracts structured data.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data = []
    order_date = None
    sku = None
    quantity = None
    product_name = None

    for line in lines:
        segments = line.strip().split("*")
        
        if segments[0] == "BPT":  # POS Transaction Header
            order_date = segments[2]
        
        elif segments[0] == "LIN":  # Line Item
            sku = segments[-1][:-1]  # Extract SKU
            
        
        elif segments[0] == "QTY":  # Quantity
            quantity = int(segments[2])
            
        elif segments[0] == "PNAME":
            product_name = segments[1]
        
        if order_date and sku and quantity:
            data.append({
                "product_name" : product_name,
                "order_date": order_date,
                "sku": sku,
                "quantity": quantity
            })
    
    return pd.DataFrame(data)

def read_edi_file(file_path):
    """
    Automatically detects the EDI type and reads it into a Pandas DataFrame.
    """
    edi_type = detect_edi_type(file_path)
    
    if edi_type == "810":
        print("Detected EDI 810 - Invoice")
        df = parse_edi_810(file_path)
    elif edi_type == "867":
        print("Detected EDI 867 - POS Sales Data")
        df = parse_edi_867(file_path)
    else:
        print("Unknown EDI format")
        return None
    
    return df
