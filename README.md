# Ad Sales Prediction App

This project presents a machine learning application that predicts product sales based on advertising budgets across TV, Radio, and Newspaper channels. It provides a simple and effective way to understand how marketing spend influences sales performance.

## Project Overview

The application is built using a Linear Regression model trained on historical advertising data. The trained model is deployed as an interactive web application using Streamlit, allowing users to input advertising costs and instantly obtain predicted sales values.

## Model Performance

The Linear Regression model achieved an R² score of 0.90, indicating that approximately 90% of the variance in sales is explained by the advertising features. This reflects a strong relationship between ad spending and sales outcomes.

For example, when the actual sales value was 22.1, the model predicted 21.37, demonstrating high prediction accuracy and reliability.

## Algorithm Used

Linear Regression is used to model the linear relationship between advertising budgets and sales. Its interpretability and strong performance make it well suited for this prediction task.

## Input Features

- TV Advertising Cost  
- Radio Advertising Cost  
- Newspaper Advertising Cost  

## Output

- Predicted Sales Value  

## Application Workflow

The project follows an end-to-end machine learning workflow, including data preprocessing, model training, evaluation, and deployment. The trained model is saved and reused within the Streamlit application for real-time predictions.

## Web Application

The Streamlit web interface allows users to enter advertisement spending values for different media channels and instantly receive predicted sales results through a clean and user-friendly interface.

## Business Impact

This project demonstrates how data-driven insights can support businesses in optimizing marketing budgets. By analyzing the impact of different advertising channels, organizations can make informed decisions to maximize sales performance and return on investment.


