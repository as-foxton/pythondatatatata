import pandas as pd
from json import loads, dumps

def methoderonald():
    bestand = pd.read_csv("goalscorers.csv")
    # for i, country in bestand.iterrows():
        # if(country["Country Code"] == landcode):
        #     pass
        # else:
        #     bestand = bestand.drop(i)
    result = bestand.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)

# print(methoderonald("AFG"))