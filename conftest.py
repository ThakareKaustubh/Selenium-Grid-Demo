import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def driver(request):
    browser = request.param
    grid_url = os.getenv("GRID_URL", "http://selenium-hub:4444/wd/hub")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(command_executor=grid_url, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(command_executor=grid_url, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

