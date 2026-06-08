# connect mysql db sqlalchemy or pymysql

# pyrefly: ignore [missing-import]
import os
import dotenv
from sqlalchemy import create_engine, text

dotenv.load_dotenv()


try:
    conn = create_engine(os.getenv("MYSQL_URL"))
    
    # Ensure the table exists before attempting to insert
    with conn.begin() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS loan_approvals (
                id INT AUTO_INCREMENT PRIMARY KEY,
                CreditScore FLOAT,
                Income FLOAT,
                LoanAmount FLOAT,
                LoanTerm INT,
                EmploymentStatus INT,
                HasDefaults INT,
                prediction INT
            )
        """))
    print("Connected to MySQL database and verified table exists")
except Exception as err:
    print(f"Database initialization error: {err}")



def insert_data( CreditScore, Income, LoanAmount, LoanTerm, Emp_status_encoded, HasDefaults, prediction ):

    # insert into loan_approvals table
    try:
        with conn.begin() as connection:
            connection.execute(
                text("INSERT INTO loan_approvals (CreditScore, Income, LoanAmount, LoanTerm, EmploymentStatus, HasDefaults, prediction) VALUES (:cs, :inc, :la, :lt, :emp, :hd, :pred)"), 
                {"cs": CreditScore, "inc": Income, "la": LoanAmount, "lt": LoanTerm, "emp": Emp_status_encoded, "hd": HasDefaults, "pred": prediction}
            )
        print(f"Data inserted successfully {CreditScore} {Income} {LoanAmount} {LoanTerm} {Emp_status_encoded} {HasDefaults} {prediction}")
    except Exception as e:
        print(f"Database insertion error: {e}")

