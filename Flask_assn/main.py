from flask import Flask, request, jsonify
from flask_cors import CORS
from load_model import predict_salary_route 
from db_connection import get_Connection

app = Flask(__name__)
app = get_Connection(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def health_check():
    return "We are On Server", 200

@app.route("/predict", methods=["POST"])
def predict_salary():
    data = request.json
    
    prediction = predict_salary_route(
        float(data["experience"]),
        float(data["certifications"]),
        data["education_level"],
        data["industry"],
        data["location"]
    )

    return jsonify({"prediction": prediction})

    

if __name__ == "__main__":
    app.run(host="localhost", port=8000)