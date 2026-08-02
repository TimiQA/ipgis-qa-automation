# IPGIS - Test Automation Framework

An automated testing framework for the IPGIS network analytics platform, built with Python, Playwright, and Pytest. This project demonstrates a hybrid testing approach, covering both the FastAPI backend and the React frontend.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **UI Automation:** Playwright
* **API Testing:** Requests
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM) + API Client Layer
* **Reporting:** Allure
* **CI/CD:** GitHub Actions

## 🏗 Framework Architecture
* `api_clients/`: Custom HTTP clients for interacting with backend endpoints, including error handling and response validation.
* `pages/`: UI abstractions using the Page Object Model.
* `tests/api/`: Backend integration tests verifying JSON schemas, status codes, and database lookup accuracy.
* `tests/ui/`: End-to-end tests checking layout rendering, mobile viewport responsiveness, and widget (iframe) integration.
* `data/`: Parameterized data sets for edge-case testing (e.g., IPv6, invalid IPs, Tor exit nodes).

## 🚀 Installation & Setup

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```



## 🧪 Running Tests

**Execute all API tests:**

```bash
pytest tests/api/ -v

```

**Execute UI tests in headless mode:**

```bash
pytest tests/ui/ -v

```

**Run in parallel with Allure reporting:**

```bash
pytest -n auto --alluredir=allure-results
allure serve allure-results
```

## 📊 CI/CD & Reporting

The repository includes a GitHub Actions workflow (`qa_pipeline.yml`) that triggers on every push to the `main` branch. It executes the full test suite across multiple workers and generates an Allure report, accessible via GitHub Pages.

---

**Author:** Artem Berestov
QA Automation Engineer | Python • Playwright • Pytest
