from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_review():
    response = client.get("/review?sentence='Món này ngon'")
    assert response.status_code == 200
    assert response.json()['Status'] == "Success"
    assert response.json()['Predict_class'] >= 1
    assert response.json()['Respone_time'] <= 3

def test_review_bad_params():
    response = client.get("/review?sen='Món này ngon'")
    assert response.status_code == 200
    assert response.json()['Status'] == "Error"
    assert response.json()['Message'] == "Invalid get parameters"

def test_test_review_list():
    data = { "sentences":["Món này khá ổn đấy" , "Món này ngon tuyệt","Thúi ","Dở", "Quá tệ, không giống với mô tả", "Tạm ổn", "Khá ngon", "Ngon, lần sau sẽ ủng hộ shop dài"] }
    response = client.get("/review/list", json = data)
    assert response.status_code == 200
    assert response.json()['Status'] == "Success"
    assert response.json()['Respone_time'] <= 10
    # assert response.json() == { "Message" : "This is a main route" }

def test_test_review_list_bad_json():
    data = { "sentence":["Món này khá ổn đấy" , "Món này ngon tuyệt","Thúi ","Dở", "Quá tệ, không giống với mô tả", "Tạm ổn", "Khá ngon", "Ngon, lần sau sẽ ủng hộ shop dài"] }
    response = client.get("/review/list", json = data)
    assert response.status_code == 200
    assert response.json()['Status'] == "Error"
    assert response.json()['Message'] == "Something went wrong"