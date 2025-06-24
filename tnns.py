import requests

url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/ranking/singles/"

headers = {
	"x-rapidapi-key": "8b949c9815msh72fc1b8c6672d99p1dfb58jsnf17affd2c537",
	"x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())