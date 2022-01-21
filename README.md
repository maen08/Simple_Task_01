# Simple_Task
Assigned to build a To-do app API with these features:
- Register user 
- Login user
- User can create a task
- User can view all the tasks
- User can categorize tasks (add task into a group)
- List all user

## Install the project
- Clone a repo and install all dependencies
```
$ git clone https://github.com/maen08/Simple_Task.git

$ cd Simple_Task

$ pip install -r requirements.txt 
```

## Run the project
```
$ cd todo_app
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

- Project will be running on 127.0.0.1:8000


## Endpoints
API Endpoints:

- /user                  GET                => shows all registered users
- /accounts/signup       POST               => signup endpoint  
- /accounts/login        POST               => login endpoint
- /                      GET                => list all tasks
- /                      POST               => create a task
- /admin                 POST               => admin page (create a super user to login as admin)


## NB:
- Dont forget to create a superuser so as you can access the database panel 
AKA admin panel hahaha ):

- Stop the server then create a superuser
```
$ python manage.py createsuperuser [ANY-NAME-HERE]
```

- Start back the server
```
$ python manage.py runserver
```


### Thanks
-  [maen08](https://github.com/maen08/)