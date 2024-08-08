from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Accessible"


def test_can_access_google_page_no_internet() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(
                "https://www.invalidurl.com"
            ) == "Not accessible"


def test_can_access_google_page_no_internet_and_invalid_url() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(
                "https://www.invalidurl.com"
            ) == "Not accessible"
