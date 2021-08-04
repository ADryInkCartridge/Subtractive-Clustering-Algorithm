from geopy.geocoders import Nominatim
import pandas as pd

xls = pd.ExcelFile('Data Science\Data Tambahan.xlsx')
df2 = pd.read_excel(xls, 'Sheet2')
df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
print(df2.head())
geolocator = Nominatim(user_agent="Test")
ladd1 = "Semarang"
print("Location address:", ladd1)
location = geolocator.geocode(ladd1)
print(location.address)
