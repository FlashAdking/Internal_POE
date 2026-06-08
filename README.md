## Setup Instructions
Before you can run these projects, you MUST satisfy these dependencies:

1. **Python Version**: It is highly recommended to use **3.14.4**. (If you use Python 3.14+, you may experience `pandas` or `numpy` C-compilation errors because pre-compiled wheels are not always available for pre-release versions).
2. **MySQL Database**: You MUST have a local MySQL server installed and running on port 3306. 
   - You need to create a database named `internal_poe`.
   - Your local MySQL credentials must match the `.env` file, or you must update the `.env` file to match yours.
3. **Environment Variables**: You must copy the `.env.sample` files to `.env` inside both the `Flask_assn` and `FastAPI` folders.

---

### How to setup Git in Windows to clone the project locally
*(Minimal steps, no login required for public repos)*

1. Download Git for Windows from: https://git-scm.com/download/win
2. Install it using the default settings.
3. Open "Git Bash" or "Command Prompt" on your Windows machine.
4. Clone the project using the HTTPS URL (No login needed!):
```bash
git clone https://github.com/FlashAdking/Internal_POE.git
```

5. Enter the project folder:
```bash
cd Internal_POE
```

6. Setup your single global virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

7. Install all dependencies for the entire workspace:
```bash
pip install -r req._all.txt
```

8. Run the projects! 
  *(Refer to the `script.txt` inside each individual folder for their exact run commands).* 
