
import joblib
from db_conn import insert_data

employee_status_encoder = joblib.load("./ML_models/loan_employment_status_label_encoder.joblib")
loan_approval_model = joblib.load("./ML_models/loan_approval_model.joblib")


def predict_loan_approval( CreditScore, Income, LoanAmount, LoanTerm, EmploymentStatus, HasDefaults ) :

    cs = CreditScore[0] if isinstance(CreditScore, list) else CreditScore
    inc = Income[0] if isinstance(Income, list) else Income
    la = LoanAmount[0] if isinstance(LoanAmount, list) else LoanAmount
    lt = LoanTerm[0] if isinstance(LoanTerm, list) else LoanTerm
    emp = EmploymentStatus[0] if isinstance(EmploymentStatus, list) else EmploymentStatus
    hd = HasDefaults[0] if isinstance(HasDefaults, list) else HasDefaults

    Emp_status_encoded = int(employee_status_encoder.transform([emp])[0])
    
    # One-hot encode the EmploymentStatus feature manually based on LabelEncoder output
    emp_1 = 1 if Emp_status_encoded == 1 else 0
    emp_2 = 1 if Emp_status_encoded == 2 else 0

    # scikit-learn expects a 2D array, we construct the 7 features
    X_pred = [[cs, inc, la, lt, hd, emp_1, emp_2]]

    prediction = loan_approval_model.predict(X_pred)

    pred_val = int(prediction[0])
    insert_data(cs, inc, la, lt, Emp_status_encoded, hd, pred_val)

    return pred_val




    