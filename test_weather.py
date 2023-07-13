import pytest
from app import app
import json


def test_hello():
    response = app.test_client().get('/hello')
    assert response.status_code == 404


def test_get_weather():
    response = app.test_client().get('/weather/New York')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert 'temperature' in data
    assert 'weather' in data
    assert data['temperature'] == 20
    assert data['weather'] == 'Sunny'


def test_add_weather():
    data = {
        'city': 'Chicago',
        'temperature': 18,
        'weather': 'Cloudy'
    }
    response = app.test_client().post('/weather', json=data)
    result = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert 'message' in result
    assert result['message'] == 'Weather added successfully'

def test_update_weather():
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    response = app.test_client().put('/weather/New York', json=data)
    result = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert 'message' in result
    assert result['message'] == 'Weather updated successfully'

def test_delete_weather():
    response = app.test_client().delete('/weather/New York')
    result = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert 'message' in result
    assert result['message'] == 'Weather deleted successfully'
