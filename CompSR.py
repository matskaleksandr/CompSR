import requests
import clr
import os
dll_path = os.path.join(os.path.dirname(__file__), "GDELib.dll")
print("Ищу DLL по пути:", dll_path, "— существует?", os.path.exists(dll_path))
clr.AddReference(dll_path)
from GDELib import DEObject

base_path = os.path.join(os.path.dirname(__file__), "data")
DE = DEObject(base_path, True, "temp.ocsr")

parts = [
    "Процессор",
    "Охлаждение",
    "Материнская плата",
    "Оперативная память",
    "Видеокарта",
    "SSD",
    "HDD",
    "Блок питания",
    "Корпус"
]

def get_price_from_product_url(product_url):
    # Берём код товара из конца ссылки
    product_code = product_url.rstrip("/").split("/")[-1]
    api_url = f"https://catalog.onliner.by/sdapi/catalog.api/products/{product_code}"
    
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    return float(data["prices"]["price_min"]["amount"])

total_price = 0

for part in parts:
    link = input(f"{part}: ").strip()
    DE.CreateCell("string",link)
    if not link:
        print(f"{part}: пропущено")
        continue
    try:
        price = get_price_from_product_url(link)
        total_price += price
        print(f"{part}: {price:.2f} BYN")
    except Exception as e:
        print(f"{part}: не удалось получить цену — {e}")

print(f"\nОбщая сумма: {total_price:.2f} BYN")
DE.Save()
