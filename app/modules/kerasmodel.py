from pyvi import ViTokenizer
from keras.models import load_model
import gensim.models.keyedvectors as word2vec

import re
import numpy as np

model_path = r'././Lib/model/'
model_sentiment = load_model(model_path+ "models.h5")

model_embedding = word2vec.KeyedVectors.load(model_path +'word.model')

word_labels = []
max_seq = 200
embedding_size = 128

for word in model_embedding.key_to_index:
    word_labels.append(word)
print (len(word_labels))
    
def comment_embedding(comment):
    matrix = np.zeros((max_seq, embedding_size))
    words = comment.split()
    lencmt = len(words)

    if lencmt > 0 :
        for i in range(max_seq):
            indexword = i % lencmt
            if (i == lencmt) or (i == max_seq):
                break
            if(words[indexword] in word_labels):
                matrix[i] = model_embedding[words[indexword]]
    matrix = np.array(matrix)
    return matrix

def pre_process(text):
    text = re.sub('[^a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ ]+', '', text)
    return ViTokenizer.tokenize(text)

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
    
    predict_data = []
    # Tokenize for Vietnamese
    for i in range(len(list_sentences)):
        list_sentences[i] = pre_process(list_sentences[i])
    # print (list_sentences)
        predict_data.append(comment_embedding(str(list_sentences[i])))
    predict_data = np.array(predict_data)

    # maxtrix_embedding = np.expand_dims(predict_data, axis=0)
    maxtrix_embedding = np.expand_dims(predict_data, axis=3)

    #Predict and scale to int [0 .. 5]
    pred = model_sentiment.predict(maxtrix_embedding)
    for y in pred:
        result.append(np.argmax(y) + 1)
    
    # print ('Run')
    return result

