import pytest

from datetime import datetime

from homeassistant.util.dt import (parse_datetime)

from custom_components.harvest_time_tracker.coordinators import calculate_week_start

@pytest.mark.parametrize("week_start,current,expected_date",[
  ("Saturday", parse_datetime("2023-06-03T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),
  ("Saturday", parse_datetime("2023-06-04T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),
  ("Saturday", parse_datetime("2023-06-05T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),
  ("Saturday", parse_datetime("2023-06-06T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),
  ("Saturday", parse_datetime("2023-06-07T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),
  ("Saturday", parse_datetime("2023-06-08T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),
  ("Saturday", parse_datetime("2023-06-09T10:00:00Z"), parse_datetime("2023-06-03T00:00:00Z")),

  ("Sunday", parse_datetime("2023-06-04T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),
  ("Sunday", parse_datetime("2023-06-05T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),
  ("Sunday", parse_datetime("2023-06-06T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),
  ("Sunday", parse_datetime("2023-06-07T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),
  ("Sunday", parse_datetime("2023-06-08T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),
  ("Sunday", parse_datetime("2023-06-09T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),
  ("Sunday", parse_datetime("2023-06-10T10:00:00Z"), parse_datetime("2023-06-04T00:00:00Z")),

  ("Monday", parse_datetime("2023-06-05T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
  ("Monday", parse_datetime("2023-06-06T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
  ("Monday", parse_datetime("2023-06-07T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
  ("Monday", parse_datetime("2023-06-08T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
  ("Monday", parse_datetime("2023-06-09T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
  ("Monday", parse_datetime("2023-06-10T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
  ("Monday", parse_datetime("2023-06-11T10:00:00Z"), parse_datetime("2023-06-05T00:00:00Z")),
])
def test_when_calculate_week_start_is_called_then_relative_date_is_returned(week_start: str, current: datetime, expected_date: datetime):
    # Act
    result = calculate_week_start(current, week_start)

    # Assert
    assert result == expected_date