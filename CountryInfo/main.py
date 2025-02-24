from fastapi import FastAPI
import json

app = FastAPI()

with open("country.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

for country in countries:
    country["Population"] = int(country["Population"].replace(",", ""))
    country["Area"] = float(country["Area"].replace(",", ""))

@app.get("/countries")
def get_countries():
    return {"data": countries}

@app.get("/countries/{name}")
def get_country(name: str):
    for country in countries:
        if country["Name"].lower() == name.lower():
            return {"data": country}
    return {"error": "Country not found"}