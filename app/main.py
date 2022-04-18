from fastapi import FastAPI, Request
from joblib import load
from pyvi import ViTokenizer
from typing import Optional
import time

model_path = r'./Lib/model/'
sample_sentence = r'Sản phẩm này tệ quá.'
# print(ViTokenizer.tokenize(sample_sentence)) #Test done

#import model tokenize
word2vec_model = load(model_path + 'to_vector.pkl')
word2vec_model.decode_error = 'ignore'
# temp = word2vec_model.transform([sample_sentence]) #Test done

#Import model classify
classify_model = load(model_path + 'my_modelSA.pkl')
# print (classify_model.predict(temp)) #Test done

async def predict_data(list_sentences):
    '''
    Function predict list of sentence, consist steps:
        . Re-process
        . Vietnamese Tokenize
        . Word to vec using TfidfVectorize
        . Predict with SVR model
    - Input: list of sentences
    - Output: list of redict result (with result in range [0, 5] (int))
    '''
    result = []
    
    # Tokenize for Vietnamese
    for i in range(len(list_sentences)):
        list_sentences[i] = ViTokenizer.tokenize(list_sentences[i])
    print (list_sentences)
    # Word to Vec
    X = word2vec_model.transform(list_sentences)

    #Predict and scale to int [0 .. 5]
    pred = classify_model.predict(X)
    for y in pred:
        if y > 5:
            result.append(5)
        elif y < 0 :
            result.append(0)
        else:
            result.append(int(round(y, 0)))
    
    return result

app = FastAPI()

@app.get("/reviewsa")
async def check_review(sentence: Optional[str] = None):
    start_time = time.time()
    try:
        
        if sentence:
            # print (sentence)
            clasify = await predict_data([sentence])
            # print (clasify)

            if clasify:
                result = { 'Predict class:' : int(clasify[0]),
                        'Status': 'Success' }
            
            else:
                result = { 'Status' : 'Error' }
        else:
            result =  { 'Status' : 'Error',
                        'Message' : 'Invalid get parameters' }
    except:
        result =  { 'Status' : 'Error',
                    'Message' : 'Something went wrong' } 
    finally:
        end_time = time.time()
        result['Respone time'] = end_time - start_time
        return result

@app.get("/reviewlist")
async def predict_list(request : Request = {'sentences' : []}):
    start_time = time.time()
    try:
        request = await request.json()
        list_sentences = request['sentences']
        print('list_sentences')
        result = { 'Message' : list_sentences }

    except:
        result =  { 'Status' : 'Error',
                    'Message' : 'Something went wrong' } 
    finally:
        end_time = time.time()
        result['Respone time'] = end_time - start_time
        return result

@app.get("/test")
async def test(list_test : Request):
    print(await list_test.json())
    return { "Message" : "Test done" }

@app.get("/")
async def root():
    return {"Message" : "This is an instruction",
            "Function" : "Predict stars of review",
            "Route" : "/reviewsa",
            "Full link" : "https://reviewsafastapi.et.r.appspot.com/reviewsa",
            "Method" : "GET",
            "Query Params" : 
                { "sentence" : 
                    { "type" : "String", 
                      "note" : "Your review which need to predict"} } }
    # return { "Message" : "Hello World" }