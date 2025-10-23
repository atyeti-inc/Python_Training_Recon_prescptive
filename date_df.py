import pandas as pd

df = pd.DataFrame([
    {'Date': '25-02-1994'}])
	
	
# Convert to datetime, assuming the format is day-month-year
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

print(df)
	
