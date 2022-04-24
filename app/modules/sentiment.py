# from joblib import load
# from pyvi import ViTokenizer

# model_path = r'././Lib/model/'
# sample_sentence = r'Sản phẩm này tệ quá.'
# # print(ViTokenizer.tokenize(sample_sentence)) #Test done

# #import model tokenize
# word2vec_model = load(model_path + 'to_vector.pkl')
# word2vec_model.decode_error = 'ignore'
# # temp = word2vec_model.transform([sample_sentence]) #Test done

# #Import model classify
# classify_model = load(model_path + 'my_modelSA.pkl')
# # print (classify_model.predict(temp)) #Test done

# async def predict_data(list_sentences):
#     '''
#     Function predict list of sentence, consist steps:
#         . Re-process
#         . Vietnamese Tokenize
#         . Word to vec using TfidfVectorize
#         . Predict with SVR model
#     - Input: list of sentences
#     - Output: list of redict result (with result in range [0, 5] (int))
#     '''
#     result = []
    
#     # Tokenize for Vietnamese
#     for i in range(len(list_sentences)):
#         list_sentences[i] = ViTokenizer.tokenize(list_sentences[i])
#     # print (list_sentences)
#     # Word to Vec
#     X = word2vec_model.transform(list_sentences)

#     #Predict and scale to int [0 .. 5]
#     pred = classify_model.predict(X)
#     for y in pred:
#         if y > 5:
#             result.append(5)
#         elif y < 0 :
#             result.append(0)
#         else:
#             result.append(int(round(y, 0)))
    
#     # print ('Run')
#     return result
