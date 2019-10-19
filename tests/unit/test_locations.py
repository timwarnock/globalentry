import json
import pytest
import globalentry


@pytest.fixture
def mocked_urllib(mocker):
    return mocker.patch('globalentry.locations.__LOCATION_LIST__', new=json.load(open('tests/unit/mocked_locations.json')))


def test_get(mocked_urllib):
    assert len(globalentry.locations.list()) == 25


def test_san_diego(mocked_urllib):
    assert globalentry.locations.by_id(5002)['city'] == 'San Diego'
    assert globalentry.locations.by_id(5002)['address'] == '2500 Paseo Internacional'


def test_california(mocked_urllib):
    assert len(globalentry.locations.filter('CA')) == 2


def test_numeric():
    assert globalentry.locations.__numeric('3') == 3
    assert globalentry.locations.__numeric('3.141') == 3.141
    assert globalentry.locations.__numeric('-.141') == -0.141
    assert globalentry.locations.__numeric('NULL') == 0

