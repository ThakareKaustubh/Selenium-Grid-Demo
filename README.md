# 🚀 Selenium Grid Demo with Pytest, Docker, and GitHub Actions

This repository demonstrates a containerized Selenium Grid setup using Docker and Pytest to run cross-browser UI tests in parallel across Chrome and Firefox. 
It also includes GitHub Actions CI workflow for test execution. Generates an artifact after execution using allure to generate results for the run.


## 🧰 Tech Stack

- **Python 3.10**
- **Selenium 4**
- **Pytest**
- **pytest-xdist** (parallel test execution)
- **Docker + Docker Compose**
- **Selenium Grid (Hub + Chrome/Firefox Nodes)**
- **GitHub Actions** (CI/CD pipeline)
- **Allure CLI** (pre-installed for future reporting)

---

## 📁 Project Structure

├── Dockerfile # Test runner Docker image

├── docker-compose.yml # Sets up Selenium Grid and runner

├── requirements.txt # Python dependencies

├── conftest.py # Pytest fixtures for browser setup

├── tests/

│ └── test_grid.py # Parametrized test on Google

├── .github/

│ └── workflows/

│ └── selenium-grid-demo.yml # GitHub Actions workflow


## 🧪 Test Scenario

```python
import pytest

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

```

---------- Running Tests with Docker Compose------------------------------

docker-compose up --build --abort-on-container-exit

#This will spin up Selenium Hub, Chrome, Firefox nodes, and execute tests inside the test-runner container.

--------------------------------------------------------------------------

⚙️ GitHub Actions

This project includes a GitHub Actions workflow to:

Spin up Selenium Grid using service containers

Run tests on push/pull to main

Execute the same browser matrix as locally

Path: .github/workflows/selenium-grid-demo.yml



🧼 Clean Up

To stop and remove containers:

docker-compose down
