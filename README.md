# app_py_docker_k8s
The application consists of HTML, CSS, and utilizes Python, Flask, Kubernetes, and Docker image + flask and chart.


***ToDo List Web Application***

This is a simple ToDo list web application built using Flask, Python, HTML, and CSS. The application allows users to add, mark as in progress, mark as done, and remove tasks. It also utilizes Kubernetes for container orchestration and Docker for containerization.

***Features***

    Add tasks with names, descriptions, and categories.
    Mark tasks as in progress and done.
    Remove tasks from the list.
    View tasks organized by categories: to do, in progress, and done.

***Technologies Used***

    Python
    Flask
    HTML
    CSS
    Kubernetes
    Docker

***Usage***

    Clone the repository.
    Navigate to the project directory.
    Build the Docker image: docker build -t todo-list-app .
    Run the Docker container: docker run -p 5000:5000 todo-list-app
    Access the application in your web browser at http://localhost:5000.