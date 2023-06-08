# TaskBuddy

Task Manager Application

TaskBuddy is a simple and efficient task management application built with Django. It allows users to create, update, and track their tasks, helping them stay organized and boost productivity.

I designed and implement a task management application that satisfies the following requirements:

## Features:

- Task Creation: Users can easily create tasks by providing a task name, description, and due date.
- Task Update and Completion: Users can update task details such as name, description, and due date. Tasks can also be marked as completed.
- Task Listing and Sorting: Users can view a list of all tasks, sorted based on their due dates. Recently added tasks are displayed first.
- Task Search and Filtering: Users can search for specific tasks by their names or descriptions. Tasks can also be filtered based on their completion status.
- Tagging: Tasks can be organized and filtered using tags, allowing users to categorize their tasks effectively.

## Installation

1. Clone the repository:

    git clone https://github.com/jhansiKaranam64/Task_Buddy-app/

2. Install the required dependencies:

    pip install -r requirements.txt

3. Set up the database:

    python manage.py migrate

4. Run the development server:

    python manage.py runserver

5. Access TaskBuddy in your web browser at http://localhost:8000.
