import pytest
import allure

@allure.title("Verify Google Page Title")
@allure.description("This test verifies that the title of the Google homepage contains 'Google'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_google_title(driver):
    with allure.step("Open Google homepage"):
        driver.get("https://www.google.com")

    with allure.step("Verify title contains 'Google'"):
        assert "Google" in driver.title

