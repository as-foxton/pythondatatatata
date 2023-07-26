from flask import Flask, request, render_template
from flask_cors import CORS
from flask import Response
# import jefta
# import io
# from matplotlib.figure import Figure
# import os
import pandas as pd

from json import loads, dumps 


app = Flask(__name__) 
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"


# @app.route("/apikey")
# def helloWorld():
#   return "Hello, cross-origin-world!"




# @app.route("/jefta/<ldcode>")
# # jobid=int(jobid)
# def helloJefta(ldcode):
#   # fig, ax = jefta.methodejefta()  # Assuming this generates a plot and returns the figure and axes

#   # output = io.BytesIO()
#   # fig.savefig(output, format='png')

#   # return Response(output.getvalue(), mimetype='image/png')

#   return jefta.methodejefta(ldcode)



# country="DE"
# sex="F"
# def filter_data(country,sex):


@app.route('/filterdata', methods=['GET'])
def filter_data():

  df_filtered = pd.read_csv("df_filtered.csv")
  countries = request.args.get('countries')  # Get the countries as a JSON string
  sex = request.args.get('sex')
  countries_list = loads(countries) if countries else []
  # country="DE"
  # sex="F"
  # print(type(country))
  df_filtered2 = df_filtered[(df_filtered['geo'].isin(countries_list)) & (df_filtered['sex'] == sex)]
  result = df_filtered2.to_json(orient="records")
  parsed = loads(result)
  # print(f"Country: {country}")
  # print(f"Sex: {sex}")
  # print(f"Filtered Data: {df_filtered2}")

  return dumps(parsed, indent=4)







# print(filter_data(country,sex))


# def helloJefta():
#   # fig, ax = jefta.methodejefta()  # Assuming this generates a plot and returns the figure and axes

#   # output = io.BytesIO()
#   # fig.savefig(output, format='png')

#   # return Response(output.getvalue(), mimetype='image/png')

#   return jefta.methodejefta(ldcode)





# @app.route('/')
# def home():
#     with open('api_key.txt', 'r') as f:
#         api_key = f.read().strip()
#     return render_template('vacature1.html', api_key=api_key)

# @app.route("/felix/<landcode>")
# def helloFelix(landcode):
#   return felix.methodefelix(landcode)

# @app.route("/ronald")
# def helloRonald():
#   return ronald.methoderonald()