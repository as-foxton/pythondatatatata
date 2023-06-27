import pandas
from json import loads, dumps


def methodejefta(jobid):
  bestand = pandas.read_csv("nyc-jobs.csv")
  for i,job in bestand.iterrows():
    if(job["JobID"]==int(jobid)):
      pass
    else:
      bestand=bestand.drop(i)

  result=bestand.to_json(orient="records")
  parsed=loads(result)
  return dumps(parsed,indent=4)
  # return "dit komt van jefta"

# jobid=87990
# bestand = pandas.read_csv("nyc-jobs.csv")
# for i,job in bestand.iterrows():
#   if(job["JobID"]==jobid):
#     print(methodejefta(87990))

# print(type(jobid))