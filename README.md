# Workout Tracker

Track your workouts and log exercise details effortlessly with the Workout Tracker. 💪🏋️‍♀️

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Workout Tracker is a Python-based application that helps you record your daily workouts and exercise details. It utilizes Natural Language Processing (NLP) to extract exercise information from your input and then logs it into a Google Spreadsheet for easy tracking. 📝📈

## Features

- **Exercise Logging**: Log your daily exercises with details such as exercise name, duration, and calories burnt. 🏃‍♀️🔥

- **NLP Integration**: The application uses NLP to understand your exercise descriptions and extract relevant details. 🧠📊

- **Google Sheets**: Recorded exercises are stored in a Google Spreadsheet for convenient access and tracking. 📅📋

## Requirements

Before using the Workout Tracker, ensure you have the following:

- Python 3.x installed on your system.

- Set up environment variables for authentication:
   - **SHEETY_USER_NAME**: Your Sheety username.
   - **BEARER_TOKEN**: Bearer token for Sheety authentication.
   - **NUTRITIONIX_ID**: Your [Nutritionix API ID](https://www.nutritionix.com/business/api).
   - **NUTRITIONIX_API**: Your [Nutritionix API key](https://www.nutritionix.com/business/api).

- A Google Account for Google Sheets and Sheety integration.

## Installation

1. Clone this repository to your local machine.

2. Install the required Python packages using pip

3. Set up environment variables for authentication (as mentioned in the Requirements section).

## Usage

1. Run `main.py` to start the Workout Tracker.

2. Input the exercises you did today when prompted.

3. The Workout Tracker will extract exercise details and log them into the Google Spreadsheet.

Enjoy your workouts and happy tracking! 💪🏋️‍♀️📈

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Sheety](https://sheety.co/): For providing the Google Sheets API integration.
- [Nutritionix](https://www.nutritionix.com/business/api): For the NLP-based exercise reader.



