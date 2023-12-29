# py-poc

## Python poc for testing

### Environment

```bash
# list of paths added to the sys.path, the search paths for imports
PYTHONPATH


```

### Create Virtual Environment

```bash
python -m venv venv
source venv/scripts/activate
#deactivate
```

### VSCODE

- CTRL + ALT + P => Python: Select Interpreter => (venv)

### Install online packages

```bash
pip install requests
```

### [Package manager - `pipenv`](https://packaging.python.org/en/latest/tutorials/managing-dependencies/)

```bash
pip install pipenv

pipenv install requests #install package and save it to Pipfile

pipenv install #install dependencies
```

### Docker

```bash
docker build -t py .

docker run py
```

### Pytest

```bash
# run the tests
python -m pytest

# list available fixtures
python -m pytest --fixtures

# list all markers
python -m pytest --markers
```

### Playwright tests

```bash
python -m pytest --headed --browser chromium -m ui
```
