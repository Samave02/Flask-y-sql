from flask import Flask
app = Flask(__name__)
with open("file.json","r") as file:
    datos = file.read()
@app.route('/proyecto/id_proyecto')
def jsonFile():
    return datos
