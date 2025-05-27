import pytest
from app import schemas
from jose import jwt
from app.config import settings




# def test_root(client):
#     res = client.get("/")
#     assert res.json().get('message') == "Joo joo testiiii!!!"
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email":"testi@testi.fi","password":"salasana"})
    
    new_user = schemas.UserOut = schemas.UserOut(**res.json())
    assert new_user.email == "testi@testi.fi"
    assert res.status_code == 201 

def test_login_user(test_user, client):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algrithm])
        
    id = payload.get("user_id") 
    assert id == test_user['id']   
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200


@pytest.mark.parametrize("email,password,status_code",[
    ('wrong@gmail.com','salasana',403),
    ('testi@testi.fi','wrongpswd',403),
    ('wrong@gmail.com','wrongpswd',403),
    (None,'salasana',422),
    ('testi@testi.fi',None,422)])

def test_incorrect_login(test_user,client, email, password,status_code):
    res = client.post("/login", data={"username": email, "password":password})

    assert res.status_code == status_code
    #assert res.json().get('detail') == 'Invalid Credentials'
