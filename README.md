# Agile Task Manager

A simple task management web application developed as an individual assessment for **Agile & DevOps in Practice**. The project demonstrates Agile planning, iterative development, automated testing, version control, continuous integration, and basic monitoring.

## 1. Product Vision

Build a simple application that allows users to manage daily tasks efficiently while applying Agile and DevOps practices to deliver reliable software.

## 2. Features

- Add new tasks.
- View all tasks.
- Mark tasks as completed.
- Delete tasks.
- Validate task input.
- Monitor application health through a health endpoint.
- Log important application actions.
- Run automated tests using GitHub Actions.

## 3. Technologies Used

- **Python** — programming language.
- **Flask** — web framework.
- **pytest** — automated testing.
- **Git and GitHub** — version control and code hosting.
- **GitHub Actions** — continuous integration.
- **VS Code** — development environment.

## 4. Project Structure

```text
agile-task-manager/
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
└── docs/
    ├── agile-plan.md
    ├── sprint1-review.md
    ├── sprint1-retro.md
    ├── sprint2-review.md
    └── sprint2-retro.md
```

## 5. Installation and Setup

### Prerequisites

Install Python 3.12 or a compatible Python version, Git, and VS Code.

### Clone the repository

```bash
git clone https://github.com/Kamandathe3rd/agile-task-manage.git
cd agile-task-manage
```



### Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 6. Run the Application

Start the Flask development server:

```bash
python app.py
```

Open the application in your browser:

http://127.0.0.1:5000

### Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the home page |
| GET | `/tasks` | View all tasks |
| POST | `/tasks` | Create a task |
| POST | `/tasks/<id>/complete` | Complete a task |
| DELETE | `/tasks/<id>` | Delete a task |
| GET | `/health` | Check application health |

Tasks can be created through the home page form or by sending a POST request with a task title.

## 7. Automated Testing

Run the test suite:

```bash
python -m pytest -v
```

The tests check the home page, task creation, empty-task validation, task completion, deletion, and application health.

## 8. Continuous Integration

GitHub Actions is configured in `.github/workflows/ci.yml`.

The workflow runs automatically when code is pushed or a pull request is opened. It installs the dependencies and executes the automated tests.

To check the results, open the repository on GitHub and select **Actions**.

## 9. Agile Methodology

The project is organized into two simulated sprints.

### Sprint 1

- Create and view tasks.
- Write automated tests.
- Configure the CI workflow.

### Sprint 2

- Complete and delete tasks.
- Add logging and a health endpoint.
- Improve test coverage and review the sprint outcomes.

The product backlog, story estimates, acceptance criteria, Definition of Done, sprint reviews, and retrospectives are documented in the `docs/` directory.

## 10. Monitoring and Limitations

The application logs important task operations and provides a `/health` endpoint.

Tasks are currently stored in memory, so they are lost when the application restarts. The application is a learning prototype and is not configured for production deployment.

## 11. Future Improvements

- Persist tasks in a database.
- Add user authentication.
- Improve the user interface.
- Deploy the application to a hosting platform.
- Add more integration tests and production monitoring.

## 12. Author

**Individual Assessment — Agile & DevOps in Practice**

This project demonstrates the practical application of Agile planning, iterative delivery, automated testing, continuous integration, and continuous improvement.