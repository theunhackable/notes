# Creating a project

To create a project we have to create a developent environment.

make sure that you have `pipenv` installed by the following command:

> ```
> pip3 install pipenv
> ```

Now we could make a devlopment environment

## Creating Development environment

open the terminal in the folder where you want to make the project and type the following command:

> ```
> pipenv install django
> ```

It will create a development enviornment. The file structure looks like :
```
    main/
        /Pipfile
        /Pipfile.lock
```

To initiate the development environment we can use the following command:
> ```
> pipenv shell
> ```

Now to open the folder in `vscode` use the following command:
>```
> code .
>```
## Starting Django Project
To create the app use the following command


> ```
> django-admin startproject projectName
> ```


`projectName` can be anything. I have used `MyCP` as project name.

> ```
> django-admin startproject MyCP
> ```

It will create a project. The folder structure looks like
```
    Main/
        MyCP/
            
            MyCP/
                __init__.py
                asgi.py
                settings.py
                urls.py
                wsgi.py
            
            db.sqlite3
            manage.py
            
        Pipfile
        Pipfile.lock
            
```
inorder to stop creating the folder again we could use the following command
> ```
> django-admin startproject MyCP .
> ```

Now the folder looks like this.
```
Main/
    
    MyCP/        
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    
    db.sqlite3
    manage.py
    Pipfile
    Pipfile.lock
```

- `__init__.py` defines that the directory is a package.
- `settings.py` where we define application settings.
- `urls.py` where we define urls of our applications.
- `wsgi.py` and `asgi.py`  are used for deployment.
  
`manage.py` is a wrapper arround the `django-admin`. We will use `manage.py` instead of `django-admin` as `manage.py` keeps track of the `settings` of our project

- To check whether we have done this correctly run the following command.
> ```
> python3 manage.py runserver
> ```
<strong>Output :-</strong>
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 30, 2022 - 12:57:56
Django version 3.2.13, using settings 'MyCP.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


```

- You will get a development server running. If not try changing the port adding the port number at the end.

> ```
> python3 manage.py runserver 1729
> ```
<strong>Output :-</strong>
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly
 until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 30, 2022 - 12:59:19
Django version 3.2.13, using settings 'MyCP.settings'
Starting development server at http://127.0.0.1:1729/
Quit the server with CONTROL-C.
```

- Go to the `http://127.0.0.1:1729/` and see whether the following screen is appearing or not. 
  
![/imgs/successful.png](imgs/successful.png)

## Starting the django app


In `django` an `app` provides certain functionality same like apps in our mobile. A django project can have multiple apps.

To create or start an app use the following command.

> ```
> django-admin startapp appname
> ```

`appname` can be anything. In my case I have used `todo_list` as an app. The file structure looks like this.

```
Main/
    MyCP/        
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    
    todo_list/
        migrations/__init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py

    db.sqlite3
    manage.py
    Pipfile
    Pipfile.lock
```

- `migrations` is used for generating database tables
- `admin.py` is a module that defines how the admin interface of the app looks like.
- `apps.py` where we configure this app.
- `models.py` module is useful for defining model classes for this app
- `views.py` is a request handler.
  
`Note:` Everytime we create an app go to the `settings.py` file of the project and add name of the app we created in the variable `INSTALLED_APPS`.

## Writing Hello World app

Go to the `todo_list` folder and open the `views.py` file.

We create `view functions` which takes `request` as input and sends a `response` as output.

- Initiallly `views.py` file looks like this.

### file: todo_list/ views.py

```py
from django.shortcuts import render

# Create your views here.

```

- Inorder to send a Http Response to the client we need the `HttpResponse` module so import it.

### file: todo_list/ views.py
```py

from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

```

- Now define a `view function` and return the `HttpResponse`

I have defined it as `index` which takes `request` as an `input parameter` and returns `response` as the `output`.

### file: todo_list/ views.py

```py
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello World!</h1>')
```
- We have successfully created the view which returns `Hello World!`.
  
#### We have created the view but how could django know that this view exists?

- Django looks for a specific variable called `urlpatterns` in `urls.py` file in our app which is not created automatically while the app was created. 
- So go to the app folder and create `urls.py` file.
- The `todo_list` app folder should look like this:

```
Main/
    MyCP/        
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    
    todo_list/
        migrations/__init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
    ->  urls.py
        views.py

    db.sqlite3
    manage.py
    Pipfile
    Pipfile.lock
```

- We need to import the `path` that django offers whenever we need to add a new path.
  
### file: todo_list/ urls.py

```py
# imports

from django.urls import path
```
- In order t reference our `view function(index)` we have to import `views file` to `urls.py` file 

### file: todo_list/ urls.py

```py
# imports

from django.urls import path
from . import views
```

- Now we could add `urlpatterns` (list variable) to the file that is needed for the django to access the view we have created.

```py
# imports

from django.urls import path
from . import 

urlpatterns = [
    
]

```

- Now we could add path to the `list`.

The path function that we have imported takes 
2 inputs.
   1. the route from the main project through user can access the view.
   2. the view function name
   add them. 

### file: todo_list/ urls.py

```py
# imports

from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.index)
]
```
  - Next, we should add the `todo_list` app url to the main project which gives access of `todo_list` app to the user.
  
  The instructions for doing this step are mentioned in the `main/urls.py` file itself.
### file: MyCp/urls.py
```py
  """MyCP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_list/', include('todo_list.urls')),
]
```
- Now open the following link : `http://127.0.0.1:1729/todo_list/say_hello/`

We will get teh following screen:
![helloworld.png](imgs/hello%20world.png)
    
## It Works but How?

whenever the url `http://127.0.0.1:1729/todo_list/say_hello` entered the `Django` server looks for the first part of the url in the `MyCP/urls.py` file. If it is found then the found part is chopped off and the remaining path is sent

#### Example:-

- Say input = `http://127.0.0.1:1729/todo_list/say_hello/`

- Look for the "todo_list" part of the url in the `MyCP/urls.py` file.
  ### file: MyCp/urls.py

    ```py
    .
    .
    .

    urlpatterns = [
                    ..., 
                    path('todo_list/', include('todo_list.urls'))
                ]
    .
    .
    .
    ```

- As there is a path included in the `MyCP/urls.py` file send the remaining path to the included path i.e. `todo_list.urls`

- Now `todo_list/urls.py` takes input from the main project and looks for the remaining path of the url. i.e    `say_hello/` 
  
### file: MyCp/todo_list/urls.py

```py
# imports

from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.index)
]
```
we can see that `say_hello` route is having the connection with the view we have written.

Thus, `Django` sends the `HttpResponse` to the client.
















