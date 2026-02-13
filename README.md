# flight_ticket_price_predictor

Predict flight ticket prices using machine learning based on flight details such as airline, source, destination, stops, journey time, and duration.

## Features

### Predict prices based on multiple inputs:

Airline – Select from popular airlines (IndiGo, Air India, Jet Airways, etc.)

Source & Destination – Airports like Mumbai, Delhi, Bangalore, Kolkata

Total Stops – 0, 1, 2, 3

Journey Day & Month – Travel date

Weekday Number – Day of the week

Journey Hour & Minute – Departure time

Duration – Flight duration in minutes

Built with a scikit-learn pipeline including preprocessing (encoding and scaling) and a Decision Tree Regressor.

Web interface using Flask for easy predictions.

Fully responsive HTML/JS front-end with dropdowns for categorical inputs.

## Technologies Used

Python 3.x

Flask

Pandas, NumPy

Scikit-learn (Pipeline, ColumnTransformer, DecisionTreeRegressor)

HTML, CSS, JavaScript

## Future Improvements

Add support for multiple regression models (XGBoost, Random Forest).

Add dynamic pricing analysis based on real-time flight data.

Deploy on Heroku or AWS for public access.
