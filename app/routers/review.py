from fastapi import APIRouter, Request
from typing import Optional

from ..modules.sentiment import predict_data

import time

router = APIRouter()

@router.get("/review", tags = ["review"])
async def check_review(sentence: Optional[str] = None):
    start_time = time.time()
    try:
        
        if sentence:
            # print (sentence)
            clasify = await predict_data([sentence])
            # print (clasify)

            if clasify:
                result = { 'Predict_class:' : int(clasify[0]),
                            'Sentence' : sentence,
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
        result['Respone_time'] = end_time - start_time
        return result

@router.get("/review/list")
async def predict_list(request : Request = {'sentences' : []}):
    start_time = time.time()
    try:
        request = await request.json()
        list_sentences = request['sentences']
        # print('list_sentences')
        result = {}
        pred = await predict_data(list_sentences)
        result_list = []
        for x in range(len(list_sentences)):
            result_list.append( { "Predict_class" : pred[x], "sentence" : list_sentences[x] } )

        result['data'] = result_list

    except:
        result =  { 'Status' : 'Error',
                    'Message' : 'Something went wrong' } 
    finally:
        end_time = time.time()
        result['Respone_time'] = end_time - start_time
        return result