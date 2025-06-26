import requests
import sqlalchemy as db
import pandas as pd

url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/ranking/singles/"

headers = {
	"x-rapidapi-key": "8b949c9815msh72fc1b8c6672d99p1dfb58jsnf17affd2c537",
	"x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
rjson = response.json()
rankings = rjson['data']
#print(rjson)

#df = pd.DataFrame.from_dict(rjson)
df = pd.json_normalize(rankings)
engine = db.create_engine('sqlite:///tennis.db')
df.to_sql('mens_rankings', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM mens_rankings;")).fetchall()
   print(pd.DataFrame(query_result))