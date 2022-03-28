import json

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b"I'm okay!"

def test_prediction_endpoint_with_valid_input(client):
    payload = {
        'features': [5.0, 3.6, 1.4, 0.2]
    }
    response = client.post('/predict', json=payload)
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert response_data == {'result': 0}