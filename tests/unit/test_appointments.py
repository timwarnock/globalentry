import json
import pytest
import globalentry


@pytest.fixture
def mocked_urllib(mocker):
    mocker.patch('globalentry.locations.__LOCATION_LIST__', new=json.load(open('tests/unit/mocked_locations.json')))
    return mocker.patch('globalentry.appointments.by_location_id', return_value=json.load(open('tests/unit/mocked_appointments.json')))


def test_california(mocked_urllib):
    assert len(globalentry.appointments.by_locations(['CA'])) == 2
    assert globalentry.appointments.by_locations(['CA'])[0]['id'] == 5002



