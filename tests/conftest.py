from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app

from app.config import settings
from app.database import get_db, Base
from app.oauth2 import create_access_token
from app import models



#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:salasana@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



#client = TestClient(app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)    
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email":"testi@testi.fi","password":"salasana"}
    res = client.post("/users/",json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data["password"]
    return new_user    

@pytest.fixture
def test_user2(client):
    user_data = {"email":"testi2@testi.fi","password":"salasana"}
    res = client.post("/users/",json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data["password"]
    return new_user    



@pytest.fixture
def token(test_user):
    return create_access_token({"user_id":test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}

    return client

@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title":"1 otsikko",
        "content":"1 content",
        "owner_id":test_user['id']
    },  {
        "title":"2 otsikko",
        "content":"2 content",
        "owner_id":test_user['id']
    },
        {
        "title":"3 otsikko",
        "content":"3 content",
        "owner_id":test_user['id']
    },
        {
        "title":"4 otsikko",
        "content":"4 content",
        "owner_id":test_user2['id']
    }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)

    posts = list(post_map)

    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()
    return posts