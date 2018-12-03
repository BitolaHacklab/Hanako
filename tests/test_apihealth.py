def test_health(client):
    rv = client.get('/health')
    print(str(rv))
    assert b'Health OK' in rv.data