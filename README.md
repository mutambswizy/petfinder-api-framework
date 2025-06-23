
# 🐾 Petfinder API Test Automation Framework

A lightweight REST-assured-style API automation framework written in Python to test the [Petfinder API](https://www.petfinder.com/developers/v2/docs/). This framework supports functional testing, OAuth 2.0 authentication, reporting, performance testing, and CI/CD integration.

## 📁 Project Structure

```
petfinder_api_framework/
├── api/                        # API client wrapper and endpoints
├── tests/                      # Test suites and test cases
├── performance/                # Performance test scripts
├── assets/                     # Screenshots, videos, or sample payloads
├── .github/workflows/         # GitHub Actions CI/CD pipeline
├── .env                        # Contains API credentials (excluded from Git)
├── requirements.txt            # Dependencies list
├── report.html                 # Sample test report
├── setup.py                    # Package setup
├── pytest.ini                  # Pytest configuration
```

## ⚙️ Setup Instructions

> **Pre-requisites**:
> - Python 3.11+
> - `pip` (Python package installer)
> - A valid Petfinder API key & secret (from [here](https://www.petfinder.com/developers/))

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/petfinder_api_framework.git
cd petfinder_api_framework
```

### 2. Setup a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and include:

```env
PETFINDER_API_KEY=your_api_key
PETFINDER_API_SECRET=your_api_secret
BASE_URL=https://api.petfinder.com/v2
```

## ▶️ How to Run the Tests

### Functional Tests

```bash
pytest tests/ -m "smoke" --maxfail=5 --disable-warnings --html=report.html
```

### Performance Tests

```bash
python performance/test_response_time.py
```

### CI/CD

Tests run automatically on push/pull requests via GitHub Actions. See `.github/workflows/ci.yml`.

## ✅ Example Report Output


![image](https://github.com/user-attachments/assets/5b7c699e-cf9b-4d69-956e-7d792e4b7d85)

![image](https://github.com/user-attachments/assets/fde2e9b3-909f-4603-8489-195b6c07b0fa)


## 🎥 Sample Test Run (Video)


https://github.com/user-attachments/assets/19ce71a3-66d1-40d5-81cd-6e76a062e88d




## 💡 Assumptions & Decisions

- OAuth token is cached in memory per session.
- API base URL is configurable via `.env`.
- Test categories (e.g. smoke, regression) are marked using pytest markers.
- Response validation includes status code, schema, and key field checks.

## 🧰 Tools & Resources Used

- **Python 3.11**
- **Requests** – For HTTP calls
- **Pytest** – Test framework
- **pytest-html** – HTML reporting
- **python-dotenv** – Load environment variables securely
- **GitHub Actions** – CI/CD
- **Locust / custom timers** – For performance testing (WIP)


## 👨‍💻 Author

**Wisdom Mutambirwa**  
[LinkedIn](#) | [GitHub](https://github.com/yourusername)
