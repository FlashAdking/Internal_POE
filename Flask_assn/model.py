# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class salary_predictor(db.Model):
    id = db.Column( db.Integer , primary_key = True , autoincrement = True)
    experience = db.Column(db.Float)
    certifications = db.Column(db.Float)
    education_level = db.Column(db.Float)
    industry = db.Column(db.Float)
    location = db.Column(db.Float)
    prediction = db.Column(db.Float)



def add_data(experience, certifications, education_level, industry, location, prediction):
    db.session.add(salary_predictor(experience = experience, certifications = certifications, education_level = education_level, industry = industry, location = location, prediction = prediction))
    db.session.commit()