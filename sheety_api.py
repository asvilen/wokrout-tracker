import requests, os
from datetime import datetime

# Retrieve environment variables
USER_NAME = os.environ.get("SHEETY_USER_NAME")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

# API endpoints
SHEETY_ENDPOINT = "https://api.sheety.co/"
PROJECT_NAME = "workoutTracker"
SHEET_NAME = "workouts"
URL = f"{SHEETY_ENDPOINT}{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}/"


def add_workout(exercise_name, duration_time, calories_burnt):
    # Define the workout parameters
    parameters = {
        "workout": {
            "date": datetime.today().strftime('%Y-%m-%d'),
            "time": datetime.now().time().strftime('%H:%M:%S'),
            "exercise": exercise_name,
            "duration": duration_time,
            "calories": calories_burnt
        }
    }

    # Set the Bearer token in the headers
    bearer_header = {
        "Authorization": BEARER_TOKEN
    }

    # Send a POST request to add the workout
    response = requests.post(url=URL, json=parameters, headers=bearer_header)

    # Print the response details
    print(f"Workout details: {response.json()}")
