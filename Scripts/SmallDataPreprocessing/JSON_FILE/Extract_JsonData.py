import sys
import pandas as pd
from io import StringIO

# Read JSON data from stdin
input_data = sys.stdin.read()
df = pd.read_json(input_data)

# Process and write to stdout(Parquet format)
sys.stdout.write(df.to_csv(index=False))