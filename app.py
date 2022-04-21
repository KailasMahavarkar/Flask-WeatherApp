from flask import Flask, render_template, request, redirect, jsonify
import os
import requests 
import json

rootPath = os.path.abspath(os.path.dirname(__name__))
app = Flask(__name__)

def endpoint(cityname):
    return f'https://weatherdbi.herokuapp.com/data/weather/{cityname}'

@app.route('/')
def index():
    return jsonify({
        "msg": "Weather Api is running"
    })


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    weatherDemo = {
        'dayhour': 'Thursday 12:00 PM',
        'temp': {'c': 11, 'f': 52},
        'precip': '14%',
        'humidity': '84%',
        'wind': 
            {'km': 6, 'mile': 4},
            'iconURL': 'https://ssl.gstatic.com/onebox/weather/64/cloudy.png',
            'comment': 'Cloudy'
    }
    regionDemo = "Metropolitan City of Turin, Italy"
    if request.method == 'POST':
        formData = request.form
        query = str(formData.get('query'))
    
        if len(query) > 3:
            result = requests.get(endpoint(query))
            if result.status_code == 200:
                jsonRes = result.json()
                weather = jsonRes["currentConditions"]
                region = jsonRes["region"].replace("None, ", "")
                return render_template('app.html', region=region, weather=weather)
                               
    return render_template('app.html', region=regionDemo, weather=weatherDemo)
        

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
