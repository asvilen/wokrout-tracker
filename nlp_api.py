import requests, os

# Retrieve environment variables
NUTRTIONIX_ID = os.environ.get("NUTRTIONIX_ID")
NUTRTIONIX_API = os.environ.get("NUTRTIONIX_API")

# Nutritionix NLP API endpoint
NLP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_exercise_details(user_input_text, gender, weight, height, age):
    # Define headers with Nutritionix API credentials
    header = {
        "x-app-id": NUTRTIONIX_ID,
        "x-app-key": NUTRTIONIX_API
    }

    # Define parameters for the NLP API request
    parameters = {
        'query': user_input_text,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age
    }

    # Send a POST request to the NLP API
    response = requests.post(url=NLP_ENDPOINT, json=parameters, headers=header, verify=False)

    # Parse the response and return exercise details
    result = response.json()
    return result['exercises']
