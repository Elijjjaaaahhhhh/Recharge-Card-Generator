### `README.md`


# Recharge Card Generator

A simple web application to generate recharge card numbers using the Middle Square Algorithm. This application is built using Flask.

## Features

- Generates 20 unique recharge card numbers each time.
- Supports different card amounts: 100, 200, 500, and 1000.
- Uses the Middle Square Algorithm to generate pseudo-random numbers.
- Interactive web interface using Bootstrap for styling.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Elijjjaaaahhhhh/recharge_card_generator.git
    cd recharge_card_generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    ```

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. Install the required packages:
    ```bash
    pip install Flask
    ```

## Running the Application

1. Ensure the following environment variables are set:
    - For Windows CMD:
      ```cmd
      set FLASK_APP=app.py
      set FLASK_ENV=development
      ```

    - For Windows PowerShell:
      ```powershell
      $env:FLASK_APP = "app.py"
      $env:FLASK_ENV = "development"
      ```

    - For macOS/Linux:
      ```bash
      export FLASK_APP=app.py
      export FLASK_ENV=development
      ```

2. Start the Flask application:
    ```bash
    flask run
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
recharge_card_generator/
|-- app.py
|-- templates/
|   |-- index.html
|-- static/
|   |-- style.css
|-- venv/
|-- README.md
```

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the application.
- `static/style.css`: Custom CSS for styling the application.
- `venv/`: The virtual environment directory.
- `README.md`: Project documentation.

## Middle Square Algorithm

The Middle Square Algorithm is a method of generating pseudo-random numbers. It involves squaring the number and extracting the middle digits to form the next number in the sequence.

## Example

To generate recharge cards, select an amount from the dropdown menu and click "Generate". The application will display 20 unique recharge card numbers below the form.

## License

This project is licensed under the MIT License.
```

