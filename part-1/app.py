from flask import Flask, jsonify
import requests

app = Flask(__name__)

store = []

@app.route('/')
def fetch_jokes():
    for _ in range(10):
        r = requests.get('http://api.icndb.com/jokes/random/')
        joke = r.json()['value']['joke']
        store.append(joke)
    
@app.route('/getJokes')
def return_jokes():
    return jsonify(store)

app.run()