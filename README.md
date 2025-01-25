Pastebin Project

This is a test project created to improve knowledge of Python web development, specifically using FastAPI and SQLAlchemy for building web applications. The application serves as a minimalistic version of a "Pastebin" where users can create and share short text snippets ("pastes") via unique URLs.

Features

Create Pastes: Users can submit text through a form, and the server generates a unique URL for each paste.

View Pastes: Each paste can be accessed using its unique URL.

HTML Templates: Uses Jinja2 templates to render a simple web interface.

Database Integration: Stores pastes in a PostgreSQL database using SQLAlchemy.

Async Support: Built with FastAPI and asynchronous database handling for better performance.

Goals

This project is intended to:

Improve understanding of FastAPI for building APIs.

Practice working with asynchronous database operations using SQLAlchemy.

Gain experience with templating using Jinja2.

Experiment with deploying and testing a small web application.

Installation

To run this project locally, follow these steps:

Prerequisites

Python 3.9+

PostgreSQL

Steps

Clone the repository:

git clone https://github.com/HHamlet/pastebin
cd pastebin

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up your .env file:
Create a file named .env in the root directory and add your database configuration:

DATABASE_USER=your_username
DATABASE_PASS=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=pastebin

Run migrations (if using Alembic for database management):

alembic upgrade head

Start the application:

uvicorn app:app --reload

Open your browser and navigate to:
http://127.0.0.1:8090

Project Structure

.
├── app.py             # Main FastAPI application
├── db.py              # Database connection setup
├── models.py          # SQLAlchemy models
├── config.py          # Configuration for database connection
├── templates/         # HTML templates
│   ├── index.html     # Main page template
│   └── paste.html     # Paste display template
├── static/            # Static files (CSS, JS, etc.)
└── .env               # Environment variables (not included in repo)

Future Improvements

Add Markdown Support: Render pastes with Markdown formatting.

Syntax Highlighting: Use a library like Highlight.js for code snippets.

Expiration Time: Allow users to set expiration times for pastes.

User Authentication: Add a login system to manage personal pastes.

Dockerization: Simplify setup with Docker Compose.

Contributions

This project is meant for learning purposes, but contributions are welcome! If you'd like to suggest improvements or add features, feel free to open an issue or submit a pull request.

License

This project is open-source and available under the MIT License.

Disclaimer

This project is not production-ready. It is a learning tool designed for educational purposes and personal experimentation.

