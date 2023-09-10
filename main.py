from sheety_api import add_workout
from nlp_api import get_exercise_details

# Constants for user information
GENDER = "MALE"
WEIGHT_KG = 71
HEIGHT_CM = 175.00
AGE = 34

# Ask the user for exercise input
exercise_input = input("What exercise did you do today?: ")

# Iterate through the exercise details obtained from the NLP API
for element in get_exercise_details(exercise_input, GENDER, WEIGHT_KG, HEIGHT_CM, AGE):
    # Define workout inputs
    exercise = element['name'].title()
    duration = element['duration_min']
    calories = element['nf_calories']
    # Add the workout to the Workout Tracker Google Spreadsheet
    add_workout(exercise, duration, calories)
