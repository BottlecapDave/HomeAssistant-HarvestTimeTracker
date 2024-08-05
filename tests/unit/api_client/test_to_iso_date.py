import pytest

from datetime import datetime

from homeassistant.util.dt import (parse_datetime)

from custom_components.harvest_time_tracker.api_client import to_iso_date

@pytest.mark.parametrize("date,time,expected_date_time",[
  ("2023-06-03", "8:24", parse_datetime("2023-06-03T08:24:00")),
  ("2023-06-03", "10:00", parse_datetime("2023-06-03T10:00:00")),
  ("2023-06-03", "20:00", parse_datetime("2023-06-03T20:00:00")),
  ("2023-06-03", "8:24am", parse_datetime("2023-06-03T08:24:00")),
  ("2023-06-03", "10:00am", parse_datetime("2023-06-03T10:00:00")),
  ("2023-06-03", "08:00pm", parse_datetime("2023-06-03T20:00:00")),
  ("2023-06-03", "8:00pm", parse_datetime("2023-06-03T20:00:00")),
])
def test_when_to_iso_date_is_called_then_correct_date_is_returned(date: str, time: datetime, expected_date_time: datetime):
    # Act
    result = to_iso_date(date, time)

    # Assert
    assert result == expected_date_time