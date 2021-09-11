from flask import Flask, request, Response, render_template
import requests

application = app = Flask(__name__)
#enables debug mode
app.config['DEBUG']= True



#route to return the weather for "Valley Stream"
@app.route('/')
def main():
    #api endpoint with the query blank for the city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7e9f0ff1d2f7ec3616157c1995baeb21'
    city = 'Valley Stream'

    #inputs the city into the query in the url and gives the json output
    response= requests.get(url.format(city)).json()
    
    #dictionary to hold the city, temp, description and icon
    weather = {
        'city' : city,
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
    }

    print(weather)   
    
    return render_template('weather.html', weather = weather)
