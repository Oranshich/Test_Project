import pytest
from requests import get
from bs4 import BeautifulSoup


all_text = None


@pytest.fixture(autouse=True)
def parse_html():
    global all_text
    url = "https://the-internet.herokuapp.com/context_menu"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    all_text = html_soup.get_text()


def test_text_right_click():
    """
    The function tests if the phrase is exist in the web page
    """
    string_to_check = "Right-click in the box below to see one called 'the-internet"
    assert(string_to_check in all_text)


def test_alibaba_in_text():
    """
    The function tests if the word "Alibaba" is exist in the web page
    """
    string_to_check = "Alibaba"
    assert(string_to_check in all_text)
