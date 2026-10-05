from app import app, calculate_result


def test_total():
    total, average, result = calculate_result(80, 75, 90)
    assert total == 245


def test_average():
    total, average, result = calculate_result(80, 75, 90)
    assert round(average, 2) == 81.67


def test_pass_result():
    total, average, result = calculate_result(80, 75, 90)
    assert result == "PASS"


def test_fail_result():
    total, average, result = calculate_result(20, 30, 25)
    assert result == "FAIL"


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200