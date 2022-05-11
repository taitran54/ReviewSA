from pyvi import ViTokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle

import re
import numpy as np

model_path = r'././Lib/model/lstm/'

with open(model_path + 'tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

loaded_model = load_model(model_path + 'modelsLSTM.h5')

loaded_model.build()
loaded_model.summary()

def removeBackLoop(word):
    # print ("WORD TAG",word)
    x = 0
    #     word = word.replace(' ', '_')
    for ch in range(len (word) - 1):
        if word[len(word) - ch - 1] != word[len(word) - ch - 2]:
            break
        else:
            x += 1
    return word[:len(word) - x]

def pre_process(text):
    temp = str(text)
    temp = ViTokenizer.tokenize(str(temp))
    # print ("TAG 2" ,temp)
    temp = re.sub('[^a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ_ ]+', '', temp)
    temp = temp.split()
    # print ("TAG 3" ,temp)
    for x in range(len(temp)):
        temp[x] = removeBackLoop(temp[x])

    st = str(' '.join(temp) )
    temp = st.strip()

    result = temp.split()

    word_to_remove = []
    # print ("TAG 4.1", word_to_remove)    
    for word in result:
        if (len(word) > 13) and ('_' not in word):
            word_to_remove.append(word) 
            count += 1

        elif len (word) == 1 :
            word_to_remove.append(word) 
            count += 1
    # print ("TAG 4.2", word_to_remove)    

    for x in word_to_remove:
        result.remove(x)

    # print ("TAG 5", result)   
    result = str(' '.join(result))
    # print ("FINAL PREPROCESS CHECK: ", result)
    return result

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
    max_sequences = 266
    # print ("TAG CHECK 1")
    # Tokenize for Vietnamese
    for i in range(len(list_sentences)):
        list_sentences[i] = pre_process(list_sentences[i])
        # print ("Preprocess success: ", list_sentences[i])
    # print (list_sentences)
    predict_data = tokenizer.texts_to_sequences(list_sentences)

    # maxtrix_embedding = np.expand_dims(predict_data, axis=0)
    predict_data = pad_sequences(predict_data, maxlen=max_sequences, dtype='int32', value=0)

    #Predict and scale to int [0 .. 5]
    pred = loaded_model.predict(predict_data)
    for y in pred:
        result.append(np.argmax(y) + 1)
    
    print ('Thanks for using LSTM model')
    return result