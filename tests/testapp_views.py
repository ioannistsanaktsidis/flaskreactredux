from flask import url_for


def test_ping(app):
    with app.test_client() as client:
        res = client.get(url_for('testapp_api.ping'))

        assert res.status_code == 200
