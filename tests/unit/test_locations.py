import pytest
import globalentry


@pytest.fixture
def mocked_query(mocker):
    return mocker.patch('globalentry.__get', return_value=42)


def test_get(mocked_query):
    assert globalentry.locations.__get() == 42


def test_numeric():
    assert globalentry.locations.__numeric('3') == 3
    assert globalentry.locations.__numeric('3.141') == 3.141
    assert globalentry.locations.__numeric('-.141') == -0.141
    assert globalentry.locations.__numeric('NULL') == 0

