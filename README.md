# cursor-repo-awareness

A comprehensive Python project with CI/CD pipeline implementation.

## Features

- Discount calculation system
- Comprehensive test suite
- CI/CD pipeline with GitHub Actions
- Code quality tools (linting, formatting, type checking)
- Security scanning
- Automated testing and deployment

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Amankumar50/cursor-repo-awareness.git
cd cursor-repo-awareness
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Usage

### Running the Application

```bash
python main.py
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test file
pytest tests/test_case.py
```

### Code Quality Checks

```bash
# Linting
flake8 .

# Formatting
black .

# Type checking
mypy .
```

## CI/CD Pipeline

This project includes a comprehensive CI/CD pipeline with GitHub Actions:

### Continuous Integration (`.github/workflows/ci.yml`)

- **Multi-Python Testing**: Tests on Python 3.8, 3.9, 3.10, and 3.11
- **Code Quality**: Flake8 linting, Black formatting, MyPy type checking
- **Security Scanning**: Bandit and Safety checks
- **Test Coverage**: Pytest with coverage reporting
- **Package Building**: Automatic package building for releases

### Deployment (`.github/workflows/deploy.yml`)

- **Manual Deployment**: Trigger deployments to staging/production
- **Release Deployment**: Automatic deployment on releases
- **Environment Management**: Separate staging and production environments

### Pipeline Features

- ✅ Automated testing on multiple Python versions
- ✅ Code quality checks (linting, formatting, type checking)
- ✅ Security vulnerability scanning
- ✅ Test coverage reporting
- ✅ Package building and distribution
- ✅ Manual and automated deployment
- ✅ Environment-specific deployments

## Project Structure

```
cursor-repo-awareness/
├── .github/workflows/     # CI/CD pipeline configurations
├── tests/                 # Test files
├── main.py               # Application entry point
├── models.py             # Data models
├── service.py            # Business logic
├── utils.py              # Utility functions
├── validators.py         # Validation logic
├── exceptions.py         # Custom exceptions
├── constants.py          # Constants
├── logger.py             # Logging configuration
├── requirements.txt      # Python dependencies
├── setup.py             # Package configuration
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## Development

### Adding New Features

1. Create a feature branch
2. Implement your changes
3. Add tests for new functionality
4. Run the test suite
5. Submit a pull request

### Code Style

This project uses:
- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking

### Testing

- Write unit tests for all new functionality
- Maintain test coverage above 80%
- Use pytest for testing framework

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue on GitHub or contact the maintainers.
