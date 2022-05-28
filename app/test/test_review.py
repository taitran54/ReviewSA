from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_test_review():
    response = client.get("/review?sentence='Món này ngon'")
    assert response.status_code == 200
    assert response.json()['Status'] == "Success"
    assert response.json()['Predict_class'] >= 1

def test_test_review_list():
    data = { "sentences":["Món này khá ổn đấy" , "Món này ngon tuyệt","Thúi ","Dở", "Quá tệ, không giống với mô tả", "Tạm ổn", "Khá ngon", "Ngon, lần sau sẽ ủng hộ shop dài"] }
    response = client.get("/review/list", json = data)
    assert response.status_code == 200
    assert response.json()['Status'] == "Success"
    # assert response.json() == { "Message" : "This is a main route" }