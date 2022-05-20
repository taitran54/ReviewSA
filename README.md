# Wellcome to Review SA API Project

- The main goal of this project for predict review about agricultural in 5 starts boundary. :melon::ear_of_rice::grapes:
- This project using fastapi on Python language, The model was trained for Sentiment Analysis problem.

- It's currently working on: http://103.153.75.102:5000/ with some routes:
    - "/review" **GET** method: get a prediction for one review.
     Require parameter:
     ```JSON
     { "sentence": "a review in Vietnamese language." }
     ```
     Result: a JSON which consist a result.
    - "/review/list" **GET** method: get a prediction for list of reviews.
      Require a raw text body which is formed in JSON { "sentences" : ["Review A, "Review B"] }
      Result: a JSON which consist predict starts for per sentences in form: 
    ```JSON
    { "data" : [
        { "predict_class" : 5,
          "sentences" : "Review A" },
        { "predict_class" : 1,
          "sentences" : "Review B" }]}
    ```

- Steps to follow to run the project on WINDOWS:
    ```
        //This command to install virtualenv
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
    ```   
***THAT ALL, THANK YOU FOR YOUR VISITING :slightly_smiling_face:***
