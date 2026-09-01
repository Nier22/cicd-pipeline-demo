from app.main import app

def test_homepage():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.get_json() == {"message": "Welcome to the CI/CD demo API"}

def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json() == {"status": "OK"}

def test_add():
    with app.test_client() as client:
        response = client.get("/add/3/5")
        assert response.status_code == 200
        assert response.get_json() == {"result": 8}

def test_add_negative():
    with app.test_client() as client:
        response = client.get("/add/-2/4")
        assert response.status_code == 200
        assert response.get_json() == {"result": 2}

def test_add_zero():
    with app.test_client() as client:
        response = client.get("/add/0/0")
        assert response.status_code == 200
        assert response.get_json() == {"result": 0}