from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ca618f2a666a24bacaf3473f287b5717"  

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            weather_data = {"error": "City not found!"}

    return render_template("weather.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
