from flask import Flask
from flask_cors import CORS
import felix
import jefta
import ronald

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/felix")
def helloFelix():
  return felix.methodefelix()

@app.route("/ronald")
def helloRonald():
  return ronald.methoderonald()

@app.route("/jefta")
def helloJefta():
  return jefta.methodejefta()