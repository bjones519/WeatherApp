from flask import Flask, request, Response, render_template
import requests

application = app = Flask(__name__)
app.config['DEBUG']= True

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def main():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7e9f0ff1d2f7ec3616157c1995baeb21'
    city = 'Valley Stream'

    response= requests.get(url.format(city)).json()
    
    weather = {
        'city' : city,
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
    }

    print(weather)   
    
    return render_template('weather.html', weather= weather)
