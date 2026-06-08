from fastapi import FastAPI
import uvicorn
from load_model import predict_loan_approval
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Message": "Im your fastapi server"}


@app.post("/predict")
async def predict(request: Request):
    data = await request.json()

    prediction = predict_loan_approval(
        data["CreditScore"],
        data["Income"],
        data["LoanAmount"],
        data["LoanTerm"],
        data["EmploymentStatus"],
        data["HasDefaults"]
    )

    return {"prediction": int(prediction)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)