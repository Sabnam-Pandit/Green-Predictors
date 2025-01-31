# Green-Predictors
# BDA 602 Final Project : Energy Consumption and Generation Prediction based on Weather Conditions 
# Energy Consumption and Generation Prediction Based on Weather Conditions

## Project Overview

This project focuses on predicting energy consumption and generation in Spain based on weather conditions and historical data. The goal is to explore the relationship between weather factors (such as temperature, humidity, and wind speed) and energy generation from renewable and nonrenewable sources. Additionally, the project aims to predict energy prices and analyze the impact of temporal patterns on energy consumption and generation.

The dataset used in this project is the **Hourly Energy Demand Generation and Weather** dataset from Kaggle, which includes hourly weather data from five cities in Spain (Barcelona, Madrid, Valencia, Bilbao, and Seville) and energy generation/consumption data from 2015 to 2018.

## Team Members

- **Anastasia Kurakova**  
- **Sabnam Pandit**  
- **Alexandra Nguyen**  
- **Yu-Chieh (Jason) Tu**  
- **Wanjing (Anna) Yan**

## Key Objectives

1. **Predict Energy Consumption**: Analyze the impact of weather conditions and temporal factors on energy consumption using machine learning models.
2. **Predict Renewable Energy Generation**: Explore the relationship between weather conditions (e.g., temperature, wind speed) and renewable energy generation (solar, wind, hydro).
3. **Predict Nonrenewable Energy Generation**: Investigate the relationship between weather conditions and nonrenewable energy generation.
4. **Predict Energy Prices**: Forecast energy prices based on historical data and weather conditions.
5. **Time Series Analysis**: Attempt to predict renewable energy generation using only historical data to understand the limitations of time-based predictions.

## Methodology

### Data Preprocessing
- Merged weather and energy datasets based on date and time.
- Removed unused columns and handled missing values.
- Performed feature engineering to extract temporal features such as previous day's average energy consumption and generation.

### Feature Engineering
- Extracted temporal features like previous day's average energy consumption and generation.
- Converted date/time stamps into year, month, day, and hour for better correlation analysis.

### Machine Learning Models
- **Consumption Prediction**: Gradient Boosting Regressor, Random Forest Regressor, Elastic Net Regression.
- **Renewable Energy Generation Prediction**: Random Forest Regressor, Gradient Boosting Regressor, Voting Regressor.
- **Nonrenewable Energy Generation Prediction**: Linear Regression, Support Vector Regression, Random Forest Regressor, XGBoost Regressor.
- **Price Prediction**: Linear Regression, Random Forest Regressor.
- **Time Series Analysis**: XGBoost Regressor, Prophet, SARIMAX.

### Evaluation Metrics
- **R² Score**: Used to evaluate the performance of regression models.
- **Root Mean Squared Error (RMSE)**: Used to measure the prediction error.
- **Mean Absolute Error (MAE)**: Used to evaluate time series predictions.

## Results

### Energy Consumption Prediction
- **Gradient Boosting Regressor** and **Random Forest Regressor** outperformed the baseline **Elastic Net Regression** model.
- Including temporal features (e.g., previous day's average consumption) significantly improved model performance.

### Renewable Energy Generation Prediction
- **Random Forest Regressor** and **Voting Regressor** achieved high accuracy (R² score of 0.9886) in predicting solar energy generation.
- Solar energy generation showed a strong correlation with temperature, peaking during summer months.

### Nonrenewable Energy Generation Prediction
- **Random Forest Regressor** performed best when predicting nonrenewable energy generation using weather data.
- Models struggled to predict future nonrenewable energy generation when the training and testing data were split by time.

### Price Prediction
- **Random Forest Regressor** slightly outperformed **Linear Regression** in predicting energy prices.

### Time Series Analysis
- **SARIMAX** performed best in terms of MAE and RMSE but had a poor R² score.
- Predicting total renewable energy generation based solely on historical data was challenging due to external factors like seasonality and weather conditions.
- When focusing on a single energy source (e.g., solar) and aggregating data by month, the **XGBoost Regressor** achieved a high R² score of 0.78.

## Limitations
- Weather data was limited to five major cities in Spain, which may not accurately represent the conditions at renewable energy generation sites.
- External factors such as population density and urbanization were not considered in the analysis.

## Conclusion
This project demonstrates that combining weather conditions and historical data can effectively predict energy consumption, generation, and prices. However, predicting renewable energy generation based solely on historical data is challenging due to the influence of external factors like seasonality and weather conditions.

## Repository Structure
- **Data**: Contains the dataset used for the project.
- **Notebooks**: Includes Jupyter notebooks for data preprocessing, model training, and evaluation.
- **Results**: Contains visualizations and performance metrics for each model.
- **Reports**: Includes the final project report and presentation.

