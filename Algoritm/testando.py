import requests

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

query = "rice"

querystring = {f"ingr":{query}}

headers = {
	"X-RapidAPI-Key": "266546edcfmshdccc130ff584ccdp1c3452jsn802e9665bdaa",
	"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

json = response.json()

print(json)