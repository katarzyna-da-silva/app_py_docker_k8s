# app_py_docker_k8s
The application consists of HTML, CSS, and utilizes Python, Flask, Kubernetes, and Docker image + flask and chart.


***ToDo List Web Application***

This is a simple ToDo list web application built using Flask, Python, HTML, and CSS. The application allows users to add, mark as in progress, mark as done, and remove tasks. It also utilizes Kubernetes for container orchestration and Docker for containerization.

## ***Features***

    Add tasks with names, descriptions, and categories.
    Mark tasks as in progress and done.
    Remove tasks from the list.
    View tasks organized by categories: to do, in progress, and done.

## ***Technologies Used***

    Python
    Flask
    HTML
    CSS
    Kubernetes
    Docker
    AWS

### ***Usage***

## ***python app.py***

*********************

## ***DOCKER***

Running the Application with Docker
Building the Docker Image:

***docker build -t myapp .***

Replace myapp with the desired name for your image.
Running the Docker Container:

***docker run -it --rm -p 5001:5001 myapp***

This command will run the container on port 5001 on your host. The -it option allows for interactive operation in the container, and --rm removes the container after it's stopped.

Accessing the Application:

Once the container is running, you can access the application at ***http://localhost:5001*** in your web browser.

***DOCKER IMAGE :***
***application in docker: docker pull katarzynadasilva/myapp-k8s-py:latest***

## ***Kubernetes & AWS***

### Deployment on AWS

### Elastic Beanstalk

1. Create an Elastic Beanstalk application in the AWS Management Console.
2. Configure the EB CLI with `eb init`.
3. Deploy the application with `eb deploy`.

### Amazon EKS

1. Set up your Amazon EKS cluster in the AWS Management Console or using the AWS CLI.
2. Install and configure the `kubectl` CLI tool for managing Kubernetes clusters.
3. Deploy your application to the Amazon EKS cluster using Kubernetes manifests with `kubectl apply -f <manifests_directory>`.

```
kubectl create namespace <namespace_name>
kubectl get all -n <namespace_name>
kubectl delete pod <pod_name> -n <namespace_name>
kubectl describe pod <pod_name> -n <namespace_name>
kubectl get pods -n <namespace_name>
kubectl rollout restart deployment <deployment_name> -n <namespace_name>
kubectl logs <pod_name> -n <namespace_name>
```
