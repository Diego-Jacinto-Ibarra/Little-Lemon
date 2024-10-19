# Little-Lemon

I developed this project to showcase my backend skills, including Python, Django, MySQL, RESTful API development, and deployment practices, during the Meta Back-End Developer course.

## Table of Contents

-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)
-   [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/little-lemon.git
    cd little-lemon
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```sh
    python manage.py runserver
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Project Structure

-   **app/**: Contains the main application code.

    -   `admin.py`: Admin site configurations.
    -   `apps.py`: Application configuration.
    -   `migrations/`: Database migrations.
    -   `models.py`: Database models.
    -   `tests.py`: Unit tests.
    -   `views.py`: View functions.

-   **config/**: Contains the project configuration.

    -   `settings.py`: Project settings.
    -   `urls.py`: URL routing.
    -   `wsgi.py`: WSGI configuration for deployment.

-   `manage.py`: Command-line utility for administrative tasks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
