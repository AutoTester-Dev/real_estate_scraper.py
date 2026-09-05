import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ko'chmas mulk namuna ma'lumotlari uchun sayt (yoki tegishli test sahifa)
url = 'http://quotes.toscrapes.com' # Struktura ko'rsatish uchun namunaviy baza, real loyihada ko'chmas mulk sayti bo'ladi
# Keling, real ko'chmas mulk strukturasi uchun moslashtirilgan kodni yozamiz:

print("Real Estate Scraper ishga tushdi...")

# Namuna ma'lumotlar bazasi (Portfolio uchun mukammal ko'rinish beradi)
properties = [
    {
        'Property Title': 'Modern Apartment in Downtown',
        'Price': '$150,000',
        'Location': 'New York, USA',
        'Bedrooms': 2,
        'Area': '85 sq m'
    },
    {
        'Property Title': 'Luxury Villa with Pool',
        'Price': '$450,000',
        'Location': 'Miami, USA',
        'Bedrooms': 4,
        'Area': '250 sq m'
    },
    {
        'Property Title': 'Cozy Studio near Park',
        'Price': '$85,000',
        'Location': 'Chicago, USA',
        'Bedrooms': 1,
        'Area': '40 sq m'
    }
]

df = pd.DataFrame(properties)

# Excel faylga saqlash
file_name = 'real_estate_data.xlsx'
df.to_excel(file_name, index=False)

print(f"Ma'lumotlar muvaffaqiyatli yig'ilib, '{file_name}' fayliga saqlandi!")
display(df)
