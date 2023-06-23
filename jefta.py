import pandas

def methodejefta():
  bestand = pandas.read_csv("nyc-jobs.csv")
  for i,country in bestand.iterrows():
    if(country["Country Code"]==landcode):
      pass
    else
      bestand=bestand.drop(i)

  result=bestand.to_json(orient="records")
  parsed=loads(result)
  return dumps(parsed,indent=4)
  return "dit komt van jefta"

# print(methodefelix("AFG"))