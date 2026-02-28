KENYA HOUSE PRICE PREDICTION

A machine learning project that predicts house prices in Kenya using real estate data sourced from Kaggle.
The project follows a full end-to-end workflow used in real-world data science roles, including data cleaning, feature engineering, model building, evaluation, and deployment-ready prediction scripts.

📌 Project Overview

The Kenya real estate market is rapidly growing, and accurate house price prediction is valuable for:

Buyers & sellers

Real estate agencies

Property developers

Investment analysts

This project builds a Random Forest regression model to estimate house prices based on property features such as:

Location

Bedrooms

Bathrooms

Size (sqft)

Property type

The goal is to demonstrate strong skills in:

Python (Pandas, NumPy, Scikit-Learn)

Data preprocessing

Machine learning

Evaluation metrics

Feature importance analysis

Production-ready pipelines

📊 Key Components
1️ Exploratory Data Analysis (EDA)

eda.py explores:

Missing values

Price distribution

Feature correlations

Outliers

Categorical & numeric variable patterns

This step gives insight into trends within the Kenya housing market.

2️ Data Preprocessing Pipeline

preprocess.py includes:

Numeric feature scaling (StandardScaler)

Categorical feature encoding (OneHotEncoder)

Train/test splitting

Pipeline saving for reuse

A clean, modular preprocessing workflow—required in professional ML projects.

3️ Model Training

train_model.py trains a RandomForestRegressor and evaluates it with:

MAE (Mean Absolute Error)

R² Score

The trained model and preprocessing pipeline are saved to the models/ directory using Joblib.

4️ Prediction Script

predict.py loads the saved model to predict prices for new properties.
Allows real-time business use cases such as:

Estimating fair prices

Property valuation tools

Real estate platform automation

5️ Feature Importance

Feature importance helps explain which variables most influence house prices, supporting data-driven decision making.

Examples of typical top predictors:

Location

Size (sqft)

Bedrooms

Bathrooms

Property type

HOW TO RUN THE PROJECT

1 Clone the repository

git clone https://github.com/geeNova7/nairobi_house_price_prediction.git
cd kenya_house_price_prediction

2 Install requirements

pip install -r requirements.txt

FUTURE IMPROVEMENTS

- Add geospatial mapping using GeoPandas

- Streamlit or Flask web app for deployment

- Hyperparameter tuning (GridSearchCV)

- Interactive dashboards (Power BI / Tableau)

- Better feature engineering using Kenya-specific data

- Automated web scraping for up-to-date listings
