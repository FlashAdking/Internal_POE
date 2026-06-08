

# pyrefly: ignore [import-error]
from model import add_data
import joblib
import pandas as pd


industry_encoder = joblib.load("./ML_models/target_encoder_industry.joblib")
# education_encoder = joblib.load("./ML_models/target_encoder_education.joblib")  # <-- MISSING FILE
location_encoder = joblib.load("./ML_models/target_encoder_location.joblib")


# convert raw inputs into encodings using encoders then predict the salary using the model



model = joblib.load("./ML_models/salary_predictor_model.joblib")

def predict_salary_route(experience, certifications, education_level, industry, location):  
    
    # category_encoders expect pandas DataFrames with the correct column names
    industry = industry_encoder.transform(pd.DataFrame({'industry': [industry]})).iloc[0, 0]
    
    # Temporary fallback to a float so the LinearRegression model doesn't crash on the raw string
    education_level = 0.0 
    
    location = location_encoder.transform(pd.DataFrame({'location': [location]})).iloc[0, 0]


    prediction_value = model.predict([[experience, certifications, education_level, industry, location]])[0]
    add_data(experience, certifications, education_level, industry, location, prediction_value)
    

    return prediction_value