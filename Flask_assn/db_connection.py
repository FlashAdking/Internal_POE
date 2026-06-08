from model import db
from dotenv import load_dotenv
import os
load_dotenv()

# db_name = internal_poe

def get_Connection(app):
    db_url = os.getenv("MYSQL_URL")    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    return app