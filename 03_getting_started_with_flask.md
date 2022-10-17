# Welcome to Flask

![Flask](images/getting_started_with_flask/flask.png)

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

Throughout this tutorial, these are the reference links of the things we will be looking at. At your own convinience, you can navigate to whatever article you want to refer to:


1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)   (this article)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates](05_working_with_templates.md)
6. [Web forms](06_web_forms.md)



This article will cover these topics:

- [Install Python](#install-python)
- [Flask Project Structure](#flask-project-structure)
- [Create and Activate A Virtual Environment](#create-and-activate-a-virtual-environment)
- [Install Flask](#install-flask)
- [Create a Simple Flask Application](#create-a-simple-flask-application)
- [Update Project Dependancies](#update-project-dependancies)
- [Ignore Select Files](#ignore-select-files)
- [Push Flask Project to GitHub](#push-flask-project-to-github)


## Install Python

If you are using the Windows Subsytem for Linux, ensure that you have Python running in your Operating System. We shall not be using the native Python found in Windows. However, if you do not have Python at all, consider downloading an installer from the [Python Official Website](http://python.org/download/). 

To make sure that your Python installation is working well, let us open a terminal window in VS Code and run the command `python3`:

![Start Python Interpreter](images/getting_started_with_flask/start_interpreter.png)

Once you see the `>>>`, it means that the Python interpreter is now waiting at an interactive prompt. You can enter Python commands to test it out. For example, to print your name, you can do the following:

![Run Python in Prompt shell](images/getting_started_with_flask/run_python_code_in_prompt.png)

At the moment, we shall not be using the prompt shell. We only needed to check that it is functioning well. In subsequent lessons, we will make use of it especially for the purposes of debugging. To exit, simply type `exit()` and you will be back on your normal terminal.

![Exit Python Interpreter](images/getting_started_with_flask/exit_interpreter.png)

Alternatively, you can press "Ctrl + Z" to exit the Python prompt.


## Flask Project Structure

During this lesson, and subsequent lessons, we will be installing several packages to help us develop better softwares. Python allows us to install packages in our Operating System using the terminal. To install any package to your machine, you will see us run the following command oftern:

```python
$ pip3 install <package_name>
```

`pip` is a tool that Python offers for the purposes of installation. 

In our previous lesson [Getting Started with Git and GitHub](02_git_and_github.md), we learnt about version control. We mentioned that software applications normally go through life cycles where the first iteration of an application may be called _appV1.0.0_. A followup version may be called _appV2.0.0_, and so on and so forth.


### Understanding Virtual Environments

If you find an interesting application on Python and would like to install it to your computer, you may choose to install the first version of the software, say _appV1.0.0_. Later on, the developers of your installed software come up with _appv2.0.0_, and ask that you install the latest version for a myriad of reasons. What will happen at the end of the day is you will have multiple versions of the same software application in your machine. You will have _appV1.0.0_ and _appV2.0.0_.

To avoid the probable occurance of conflict when running your installed software, Python offers something called **virtual environments**. A virtual environment, as the name suggests, is a complete copy of your Python interpreter. Your system-wide environment is not affected when you install a software in your virtual environment. Virtual environments excel at isolating the needs of one application from that of another. For example, you can install the package _flaskV1.0.0_ in one virtual environment called _venv_ and _flaskV2.0.0_ in another virtual environment called _venv2_. These two installations are completely isolated and at no one time can they cause a conflict when running them.

To begin, we will create a brand new project called **start_flask_server**. The following project structure will be utilized when creating this project.

```python
start_flask_server
    | --- main.py
    | --- .flaskenv
    | --- .gitignore
    | --- app/
           | --- routes.py
           | --- __init__.py
```

While working with Flask, we will be utilizing a defined project structure to properly run our software. Above, we have a folder called _start_flask_server_. This folder has three files:

- `main.py`
- `.flaskenv`
- `.gitignore`

The folder also features a subfolder called _app_. The _app_ subfolder has two files:

- `routes.py`
- `__init__.py`

Do not worry if you do not understand what all these files are and what they do. We will learn about them in subsequent sections. For now, keep this project structure in mind as you build your software.

### Step 1: Create Project Folder

Open VS Code and create the project folder called _start_flask_server_

![Create project folder](images/getting_started_with_flask/create_project_folder.png)

### Step 2: Add Top-level Files

Create three files called `main.py`, `.flaskenv`, and `.gitignore`.

![Create top_level files](images/getting_started_with_flask/top_level_files.png)

### Step 3: Create App Subfolder

Create a subfolder called _app_ inside our main folder _start_a_flask_server_.

![Create app subfolder](images/getting_started_with_flask/create_app_subfolder.png)

### Step 4: Update App Subfolder

Create two files inside our _app_ subfolder. These two files are `__init__.py` and `routes.py`.

![Create app files](images/getting_started_with_flask/create_app_files.png)

### Step 5: Confirm Project Structure

Confirm that your project structure is similar to the one shown below:

![Confirm project structure](images/getting_started_with_flask/confirm_project_structure.png)



## Create and Activate A Virtual Environment

As mentioned earlier, virtual environments are used to isolate the needs of one project from another to avoid dependancy conflicts. To begin using virtual environments, we need to create one.

### Step 1: Access Project Directory

Let us navigate to our current project structure in the terminal.

![Current folder in terminal](images/getting_started_with_flask/current_folder_in_terminal.png)

### Step 2: Install a Virtual Environment

Support for virtual environments is included in all recent versions of Python, so all you need to do to create one is this:

```python
$ python3 -m venv venv
```

![Attempt creating venv](images/getting_started_with_flask/attempt_creating_venv.png)

Chances are that when you run the command above in your terminal, you will be informed that you need to begin by installing another package.

![Venv error](images/getting_started_with_flask/venv_error.png)

### Step 3: Fix Installation of Virtual Environment

To fix the instruction mentioned ealier, we need to run the command `sudo apt install python3.8-venv` on the terminal. Kindly note that your version of Python may be different from mine below. Use the correct version as instructed.

![Install python3 venv](images/getting_started_with_flask/install_python3_venv.png)

When prompted, provide your user's password, type "y" for _yes_ to allow for the installation for the package.

### Step 4: Create A Virtual Environment

Now, rerun the previous command `python3 -m venv venv`

![Create venv](images/getting_started_with_flask/create_venv.png)

- The first `venv` is the command used to create a virtual environment
- The second command `venv` is the name of the virtual environment. 

You will not see anything after running the command.

### Step 5: Activate Virtual Environment

Finally, with our virtual environment created, we need to activate it. Run this command in your terminal to activate `venv`.

![Activate venv](images/getting_started_with_flask/activate_venv.png)

Notice that the first part of our terminal has changed to `(venv) harry@DESKTOP:/flask$`. This name is the name we used to create the virtual environment. If you named your virtual environment as `flask`, then the terminal will change to `(flask) harry@DESKTOP:/flask$`


## Install Flask

It is now much more convinient to install any package within our virtual environment. The first package we shall be installing is `flask`. Run he command below to install flask in your activated virtual environment.

![Install flask](images/getting_started_with_flask/install_flask.png)

We can confirm if flask was successfully installed in our system. In your python interpreter, run `import flask`.

![Check for flask](images/getting_started_with_flask/check_for_flask.png)

- If you do not see any error from the Python prompt, it means that `flask` was successfully installed.
- Exit the interpreter by typing `exit()`.


## Create a Simple Flask Application

At this point, we are ready to build our very first flask application. But before we do so, let us understand what the files we created earlier are used for.

- `__init__.py`: This is the brain or the engine of the application. Everything begins from here. When you run your project, the application will look for this file as the starting point.
- `routes.py`: This file (also known as a module) is used to create URLs. A URL is the location of a resource in an application. For exmaple, the URL `http://localhost:5000/home` will search for the home page.
- `main.py`: This acts as the entry point to the application. It is like a door that allows access to the brain of the application.
- `.flaskenv`: This file has the needed configurations (or commands) needed to start our application. Without these commands, our application will not run well.
- `.gitignore`: This file lists all the things we do not want to push to version control (or GitHub). The application will IGNORE those files listed here .

### Step 1: Create an Application Instance

We have mentioned above that `__init__.py` file is the brain of our application. So, we will begin by updating this file with the information that is needed to start our flask server. 

![Create application instance](images/getting_started_with_flask/create_application_instance.png)

- The script above simply adds an application instance of class `Flask` (capital letter) imported from the package `flask` (small letter). 
- The `__name__` variable is a Python predefined variable set to the module in which it is used. In our case above, the module is `__init__.py`.
- Flask will use the location of this module as a starting point when loading our application and its related resouces.


### Step 2: Add routes

Notice that at the bottom of our application instance we have the line `from app import routes`. 
- `app` is the application instance in our project structure
- `routes.py` is our URL module

What we need to do next is to update this module and define our very first URL (location of a resource). Click on `routes.py` and update it with the following:

![index URL](images/getting_started_with_flask/index_url.png)

A URL is defined by a leading forward slash as seen in the image above. We have created two URLs:

- `/`: it has no word after it
- `/index`: it has the word 'index' after it

On a browser, if we paste either of the URLS, for example `http://localhost:5000/` or `http:localhost:5000/index`, we will be redirected to the text "Hello, World"

### Step 3: Create an Entry Point

We mentioned that an entry point is like a door to the application which leads to the brain of our simple software. In our application, the module (or file) called `main.py` will act as the entry point. This is how you make the file an entry point:

![Entry point](images/getting_started_with_flask/entry_point.png)

Here, we are importing the `app` application instance from `__init__.py` from the `app` package. If you find this confusing, feel free to rename either the app variable or  the package to something else easily memorable.

### Step 4: Configure Environment Variables

At this point, we are almost done with creating our first application using Flask. We only need to add a few configurations before we can start our flask server. Click on `.flaskenv` file and add the following:

![Environment variables](images/getting_started_with_flask/environment_variables.png)

This is what is happening in our file above:

- `FLASK_APP=main.py`: We set our application  to the entry point, which is `main.py`
- `FLASK_ENV=development`: We ensure that our server is for development purposes only
- `FLASK_DEBUG`: This allows flask to help us debug for errors.

### Step 5: Run Environment Variables

Once we have set your environment variables, we typically need to load them when we fire up our server for the first time. Bundling all variables in our file makes it so much easier to run them instead of running one command at a time. To ensure that all environment variables are loaded on start up, let us install the `python-dotenv` package within our active virtual environment:

![Install python dotenv](images/getting_started_with_flask/install_python_dotenv.png)

### Step 6: Start Flask Server

Believe it or not, our application is now complete and we can now start our server. **Ensure that you have saved all the changes you have made in the files.** In our terminal, run this command:

![Start flask server](images/getting_started_with_flask/start_flask_server.png)

In our terminal, we are told that the application is running on https://127.0.0.1:5000. You can copy this link and paste it in your favourite web browser to see the changes.

![See flask on browser](images/getting_started_with_flask/flask_on_browser.png)

You can update the URL seen above to http://127.0.0.1:5000/index to accees the same resource.

![Update flask URL](images/getting_started_with_flask/update_flask_url.png)


## Update Project Dependancies

Before we can push to GitHub, we need to create a new file called `requirements.txt`. This file will show what packages we have installed in our Flask project. 

### Step 1: Create Requirements file

We will create a new file called `requirements.txt`. This file will be located in the top-level directory of our project. So, begin by clicking on our project folder to select it.

![Select project folder](images/getting_started_with_flask/select_project_folder.png)

Create a new file called `requirements.txt`. 

![Create requirements file](images/getting_started_with_flask/create_requirements_file.png)


### Step 2: Split Terminal

First, split the terminal so there are two of them. Begin by clicking the icon below:

![Split terminal](images/getting_started_with_flask/split_terminal.png)


Your terminal will now look like this:

![New split terminal](images/getting_started_with_flask/new_split_terminal.png)

Activate your virtual environment in the new split terminal.

![Activate venv in new split terminal](images/getting_started_with_flask/activate_venv_split_terminal.png)


### Step 3: Update Project Requirements

Now, we can run this command to update our `requirements.txt` file. Press "Enter" after typing it

![Update project requirements](images/getting_started_with_flask/update_projet_requirements.png)

You should be able to see that `requirements.txt` file has been updated with all the project dependancies.

![Project dependancies](images/getting_started_with_flask/project_dependancies.png)



## Ignore Select Files

Not all files need to be pushed to GitHub. As such, we have a file called `.gitignore` which we can use to ignore certain files from version control. 

### Step 1: Find What to Ignore

Head over to this link: https://github.com/github/gitignore/blob/main/Python.gitignore

![Find files to ignore](images/getting_started_with_flask/files_to_ignore.png)

### Step 2: Copy all Content

Click on the copy icon to copy all the contents of the file

![Copy file content](images/getting_started_with_flask/copy_file_content.png)

### Step 3: Paste the Copied Content

Right click inside the `.gitignore` file to paste the copied content

![Paste copied content](images/getting_started_with_flask/paste_copied_content.png)

Remember to save your work. If you notice that you have the white dot (`.`) at the top of the file, please press "Ctrl + S" to save.




## Push Flask Project to GitHub

With the project working as expected, we can now push it to GitHub. We saw from our last lesson [Git and GitHub](02_git_and_github.md) how to push our work to version control platforms. 

### Step 1: Create a Repository on GitHub

Head over to your GitHub account. Ensure you are logged in. Create a new repository as seen below:

![Create repository](images/getting_started_with_flask/create_repository.png)

### Step 2: Give Repository a Name and a Description

You now need to provide a repository name and description to help those interested in it to learn more.

![Create repo](images/getting_started_with_flask/create_repo.png)

You will be redirected to this page below:

![Project repo](images/getting_started_with_flask/project_repo.png)


### Step 3: Initialize Project Directory

Back to VS Code, run the `git init` command to make the project folder trackable by `git`.

![Initialize project folder](images/getting_started_with_flask/initialize_project_folder.png)

### Step 4: Check Directory Status

It is always advisable to keep checking the status of your tracked folder to note any changes. Run the command below:

![Check status](images/getting_started_with_flask/check_status.png)

You should e able to see all files from your project in 'red' color.


### Step 5: Add Project to Git

Run the command below to add all project files to version control

![Add files to git](images/getting_started_with_flask/add_files_to_git.png)

Notice the fullstop (`.`) after the command. It is used to mean add 'everything`. You are advised to use this cautiously, though. You need to be sure that you want to commit everything to version control.

### Step 6: Commit The Changes

After adding the files to version control, we now need to commit them.

![Commit files](images/getting_started_with_flask/commit_files.png)


### Step 7: Change Branch

Switch the branch name to a more modern convention called `main`.

![Main branch](images/getting_started_with_flask/main_branch.png)

### Step 7: Add to Remote Repo

We now need to add our commit(s) to a remote repository. Ensure that the link used below is SSH

![Add remote origin](images/getting_started_with_flask/add_remote_origin.png)

### Step 8: Push to GitHub

Now, we are ready to push our work to GitHub.

![Push to gitHub](images/getting_started_with_flask/push_to_github.png)

Head over to your project repository and reload the page. 

![Reload page](images/getting_started_with_flask/reload_page.png)

You should be able to see the files in GitHub.

![Project in github](images/getting_started_with_flask/project_in_github.png)

### Step 9: Add README File

Notice that our project on GitHub lacks a `README.md` file. As an assignment, I would like you to add one to your project and push it to GitHub. If you are not so sure how to go about it, kindly refer to our previous lesson [Git and GitHub](02_git_and_github.md).

See my updated repository which currently includes the `README.md` file.

![Teacher flask project](images/getting_started_with_flask/teacher_flask_project.png)