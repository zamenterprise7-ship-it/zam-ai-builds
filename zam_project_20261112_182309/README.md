# zam_project_20261112_182309

## Description
This is a simple Python calculator project that supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Usage

### Running from the command line
```bash
python main.py <operation> <num1> <num2>
```

**Example:**
```bash
python main.py add 5 3
# Output: Result: 8.0
```

Supported operations:
- `add`
- `subtract`
- `multiply`
- `divide`

### Running tests
```bash
python -m unittest discover
```

## Project Structure
- `main.py`: CLI entry point.
- `calculator.py`: Core calculator logic.
- `tests/test_calculator.py`: Unit tests.
- `README.md`: Documentation.
- `.gitignore`: Git ignore patterns.

## License
MIT