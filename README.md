# Crop Recommendation System

This is a web application built with Django that recommend the most suitable crop based on various environmental factors such as Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall. Farmers can input these parameters, and the system will provide a recommendation for the best crop to cultivate.

## Features

- Predicts the most suitable crop based on environmental parameters.
- User-friendly interface for inputting data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AnkithShetty397/crop_recommendation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd crop_recommendation
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application in your web browser at [http://localhost:8000/predict](http://localhost:8000/predict).

## Usage

1. Access the web application in your browser.
2. Fill in the required parameters for Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.
3. Click the "Recommend Crop" button.
4. The system will display the recommended crop based on the provided parameters.

