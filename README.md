# Task Tracker Web Application

A simple and intuitive web application to manage and track tasks. Users can create tasks, set due dates, and monitor their progress. This application is built using Django, with a focus on providing a smooth user experience for task management.

## Features

- **User Authentication**: Users can sign up, log in, and manage their tasks securely.
- **Task Creation**: Users can create tasks by entering a title, description, due date, and task progress (In Progress or Completed).
- **Task Progress Tracking**: The app allows users to monitor the progress of their tasks in real-time.
- **User Dashboard**: A personalized task list view displaying the tasks assigned to each user along with their progress.
- **Attractive and Responsive UI**: The application has a visually appealing, user-friendly interface with a responsive design.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (Default for Django projects)
- **Version Control**: Git

## Installation

To run the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/task-tracker.git
cd task-tracker
2. Create and Activate a Virtual Environment
For Windows:
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
For macOS/Linux:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Apply Migrations
bash
Copy
Edit
python manage.py migrate
5. Run the Development Server
bash
Copy
Edit
python manage.py runserver
Now, visit http://127.0.0.1:8000/ in your browser to view the application.

Usage
Signup: Register a new account using the Signup page.
Login: After signup, log in using the Login page.
Create Task: Once logged in, you can create a new task from the Create Task page.
Task List: After creating tasks, you can view them along with their due dates and progress on the Task List page.



Contributing
If you'd like to contribute to the project, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to your branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Thanks to Django for providing a robust framework for web development.
Inspired by modern web application design principles to create an intuitive user experience.
