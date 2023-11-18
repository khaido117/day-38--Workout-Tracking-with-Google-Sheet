import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GENDER = "MALE"
WEIGHT_KG = "80"
HEIGHT_CM = "175"
AGE = "28"

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_params = {
    "query": "Run 3 miles",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"]
}
response = requests.post(url=excercise_endpoint, json= user_params, headers= header)
result = response.json()

sheet_endpoint = "https://api.sheety.co/471c9050080704bde09788f6ffc48608/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%H:%M:%S")

exercise_params = {
    "Date": "21/07/2020",
    "Time": "15:00:00",
    "Exercise": "Running",
    "Duration": "50",
    "Calories": "220"
}

header_auth = {
    "Authorization": os.environ["AUTHORIZATION"]
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=header_auth)

