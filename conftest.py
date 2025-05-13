import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, fr, ru, es etc.")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print(f"\n[Browser] Starting Chrome with language = {language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n[Browser] Quitting...")
    browser.quit()