# Wellcome to My Project

- This project using fastapi on Python language

- It's currently working on: http://103.153.75.102:5000/ with some routes:



- Steps to follow to run the project on WINDOWS:

    // This command to install virtualenv
    pip install virtualenv

    
    cd reviewsa

    // Install virtualenv to folder venv in project
    virtualenv venv

    // Activate virtualenv
    venv\Scripts\activate

    // Install librarys
    pip install -r requirements.txt --no-cache-dir

    // Run project
    uvicorn app.main:app
    // Now your API running on http://127.0.0.1:8000
    
    // If you wanna use hot reload function, follow /// the pattern
    uvicorn app.main:app --reload
    
THANK YOU