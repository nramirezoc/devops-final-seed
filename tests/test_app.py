import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app


def test_home():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200


def test_get_tasks():
    client = app.test_client()

    response = client.get('/tasks')

    assert response.status_code == 200


def test_create_task():
    client = app.test_client()

    response = client.post('/tasks', json={
        "title": "Aprender DevOps",
        "description": "Hacer pruebas unitarias"
    })

    data = response.get_json()

    assert response.status_code == 201
    assert data["title"] == "Aprender DevOps"


def test_create_task_without_title():
    client = app.test_client()

    response = client.post('/tasks', json={
        "description": "Sin título"
    })

    assert response.status_code == 400


def test_task_not_found():
    client = app.test_client()

    response = client.get('/tasks/9999')

    assert response.status_code == 404