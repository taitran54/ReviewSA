# Wellcome to Review SA API Project

- The main goal of this project for predict review about agricultural in 5 starts boundary. :melon::ear_of_rice::grapes:
- This project using fastapi on Python language, The model was trained for Sentiment Analysis problem.
- Unit tests are also consisted.
- You can find postman JSON test file in [https://github.com/taitran54/ReviewSA/blob/main/ReviewSA.postman_collection.json] which will have 2 test route with sample data.

- It's currently working on: https://reviewsa.space with some routes:
    - "/review" **GET** method: get a prediction for one review.
     Require parameter:
     ```JSON
     { "sentence": "a review in Vietnamese language." }
     ```
     Result: a JSON which consist a result.
     Here is fast test link [https://reviewsa.space/review?sentence="không ngon"]
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
        
        // (Optional) Run unit tests - check all things are stay in form.
        pytest
        
        // Run project
        uvicorn app.main:app
        // Now your API running on http://127.0.0.1:8000

        // If you wanna use hot reload function, follow /// the pattern
        uvicorn app.main:app --reload
    ```   
 
 - To run unit tests, make sure virtualenv was installed
    ```
        venv\Scripts\activate
        
        pip install -r requirements.txt --no-cache-dir
        
        pytest
    ```
- Currently, unit tests consist 5 units for 3 route:
    - "\" **GET** 1-unit (1 positive)
    - "\review" **GET** 2-unit (1 positive, 1 negative)
    - "\review\list" **GET** 1-unit (1 positive, 1 negative)
 

```diff
- NOTE THAT: if unit tests do not going through with high reponse_time json reponse
-            your hardware device may be not enough for working with Neural Network model.
```

***THAT ALL, THANK YOU FOR YOUR VISITING :slightly_smiling_face:***
