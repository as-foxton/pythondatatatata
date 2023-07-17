from flask import Flask, render_template
from flask_cors import CORS
from flask import Response
# import felix
import jefta
# import ronald
import io
from matplotlib.figure import Figure
# from dotenv import load_dotenv
import os
# import requests
# load_dotenv()



app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

# @app.route("/felix/<landcode>")
# def helloFelix(landcode):
#   return felix.methodefelix(landcode)

@app.route("/ronald")
def helloRonald():
  return ronald.methoderonald()

@app.route("/jefta")
# jobid=int(jobid)
def helloJefta():
  fig, ax = jefta.methodejefta()  # Assuming this generates a plot and returns the figure and axes

  output = io.BytesIO()
  fig.savefig(output, format='png')

  return Response(output.getvalue(), mimetype='image/png')

@app.route('/')
def home():
    with open('api_key.txt', 'r') as f:
        api_key = f.read().strip()
    return render_template('vacature1.html', api_key=api_key)

