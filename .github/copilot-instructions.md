# Copilot Instructions for AI-codyssey

## Project Overview
This project is a collection of Python scripts and small web applications, each focused on a specific algorithm, calculator, or web service. The codebase is organized by numbered files (e.g., `3_app.py`, `4_minmax_calculator.py`) and topic-based markdowns. Each file is generally self-contained, but some patterns and conventions are shared across the workspace.

## Key Components & Patterns
- **Web Service Example (`david/3_app.py`)**: Implements a Flask web server that converts text to speech using gTTS. It demonstrates:
  - Use of environment variables for configuration (e.g., `DEFAULT_LANG`)
  - Handling query parameters via `request.args.get()`
  - Streaming binary data (MP3) as HTTP response using `BytesIO` and Flask's `Response`
  - Running on all interfaces, port 80 by default
- **Algorithmic Scripts**: Files like `4_minmax_calculator.py` and `5_sort_calculator.py` are standalone CLI tools for min/max and sorting, using explicit algorithms (e.g., selection sort, bubble sort) and no built-in sort functions.
- **Input Handling**: Most scripts expect user input from the terminal, often as space-separated numbers, and use list comprehensions for parsing.
- **Error Handling**: Value errors from invalid input are caught and print a user-friendly message before exiting.

## Developer Workflows
- **Running Web Apps**: Use `python3 david/3_app.py` (ensure Flask and gTTS are installed). The app listens on port 80 and may require sudo/root privileges.
- **Running CLI Scripts**: Use `python3 <scriptname.py>`. Input is prompted via `input()`.
- **Dependencies**: Install with `pip install flask gtts` for web apps. No requirements.txt is present; dependencies are minimal and per-script.
- **No Central Build/Test**: There is no unified build or test system. Each script is run and debugged independently.

## Project-Specific Conventions
- **No Built-in Sort**: Sorting scripts must use explicit algorithms (e.g., selection or bubble sort), not Python's `sorted()` or `.sort()`.
- **Minimal External Files**: Most scripts avoid writing to disk, using in-memory buffers (e.g., `BytesIO`) when needed.
- **Self-contained Scripts**: Each numbered script is intended to be standalone, with minimal cross-file imports or dependencies.
- **User Prompts**: All CLI tools use clear, explicit prompts and expect well-formatted input.

## Integration & Extensibility
- **Adding New Calculators/Apps**: Follow the pattern of existing numbered scripts. Place new files at the root or in the `david/` subdirectory, and use clear prompts and error handling.
- **Web Apps**: Use Flask for HTTP endpoints, and prefer in-memory operations for temporary data.

## Example Patterns
- **Parsing Input**: `[float(n) for n in input().split()]`
- **Selection Sort**: See `5_sort_calculator.py` for explicit implementation.
- **Flask Route**: See `david/3_app.py` for a minimal web API with binary response.

---

For questions about conventions or extending the project, review similar numbered scripts or ask for clarification.
