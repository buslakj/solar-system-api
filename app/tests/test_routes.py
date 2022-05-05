def test_get_all_planets_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == []

 
def test_get_one_planet(client, two_save_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == {
    "id": 1,
    "name":"Earth",
    "description" : "Home planet",
    "color" : "Blue and green"
    }