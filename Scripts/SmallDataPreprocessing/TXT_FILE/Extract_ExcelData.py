import sys
import pandas as pd
from io import StringIO

# Read from stdin
input_data = sys.stdin.read()
df = pd.read_csv(StringIO(input_data))  # Use StringIO to wrap the string

# Write to stdout
sys.stdout.write(df.to_csv(index=False))