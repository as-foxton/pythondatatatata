from flask import Flask
from flask_cors import CORS
from flask import Response
import felix
import jefta
import ronald
import io
from matplotlib.figure import Figure

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/felix/<landcode>")
def helloFelix(landcode):
  return felix.methodefelix(landcode)

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