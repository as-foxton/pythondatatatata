import pandas
from json import loads, dumps

def methodefelix(landcode):
  bestand = pandas.read_csv("unemploymentpercountry.csv")
  for i, country in bestand.iterrows():
    if(country["CountryCode"]==  landcode):
      pass
    else:
      bestand = bestand.drop(i)
  result = bestand.to_json(orient="records")
  parsed = loads(result)
  return dumps(parsed, indent=4) 

#print(methodefelix("AFG"))