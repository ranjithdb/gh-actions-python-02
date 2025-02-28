# gh-actions-python-02

## Python Joke App with GitHub Actions  

This project is a simple Python app that fetches random jokes using an API. It demonstrates GitHub Actions for automating dependency installation, linting, and testing.  

## Features  

- **Dependency Management**: Installs required packages via `pip` from `requirements.txt`.  
- **Linting with Flake8**: Ensures code quality by detecting syntax errors and style violations.  
- **Testing with Pytest**: Verifies the app’s functionality.  
  

## Run Locally

```bash
pip3 install -r requirements.txt
flake8 app.py
pytest app.py
```

## Auto-formatting (Optional): Use `autopep8` to automatically fix linting issues

```bash
pip3 install autopep8
autopep8 --in-place --aggressive app.py
```
