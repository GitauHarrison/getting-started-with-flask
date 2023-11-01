# Deploy Your Application

![Render](images/deployment/render.png)

All the while, we have been running and testing our application running in our local machine. There has been no (better) way for us to share our work with anyone else except ourselves. It defeats the logic that we have built a chat application that no other user can access. This chapter is dedicated to us learning how to share our work with the world on the internet.

Throughout this tutorial, these are the reference links for the things we will be looking at. At your convenience, you can navigate to whatever article you want to refer to:

2. [Getting Started with HTML and CSS](02_getting_started_with_HTML_and_CSS.md)
3. [Git and GitHub](03_git_and_github.md)
4. [Collaboration Using GitHub](04_collaboration_using_github.md)
5. [Introduction to Bootstrap](05_bootstrap_intro.md)
6. [Getting Started with Flask](06_getting_started_with_flask.md)
7. [Working with Templates](07_working_with_templates.md)
8. [Web forms](08_web_forms.md)
9. [Database](09_database.md)
10. [User Login](10_user_login.md)
11. [Profile Page and Avatars](11_profile_page_and_avatars.md)
12. [Error Handling](12_error_handling.md)
13. [Pagination](13_pagination.md)
14. [Working With Email](14_working_with_email.md)
15. [Facelift](15_better_looking_application.md)
16. [Timestamp](16_timestamp.md)
17. [Deployment on Render](17_deployment_on_render.md) (this article)


### Lesson Objectives

By the end of this lesson, you should be able to:

- Understand what deployment is
- Make your application ready for deployment by installing the necessary dependencies
- Create an account on Render
- Configure your application on Render
- Access your application on a publicly-accessible link on the internet

### Table of Contents

- [Deployement platforms](#deployment-platforms)
- [Render](#render)
    - [Why Render](#why-render)
- [Prepare The Application For Deployment](#prepare-the-application-for-deployment)
    - [Development Server Versus Production Server](#development-server-versus-production-server)
    - [Gunicorn](#gunicorn)
    - [Update Dependency File](#update-dependancy-file)
    - [Push Your Work To GitHub](#push-your-work-to-github)
- [Deploy On Render](#deploy-on-render)
- [Assessment](#assessment)
- [Quiz](#quiz)


## Deployment Platforms

To **deploy** in English means to _move into position_. In computing terms, it means to make something available. So, when we say we want to deploy our chat application, we mean that we want to make it available for use. There are several approaches we can use to deploy an application. 

- You can deploy a static site (pure HTML, CSS, and JavaScript) on [Netlify](https://app.netlify.com/drop/) by dragging and dropping
- You can deploy your backend-powered application on [Python Anywhere](https://help.pythonanywhere.com/pages/Flask/) with minimal setup requirements
- You can deploy your Python-powered in Linux servers such as [Linode](https://www.linode.com/) manually

There are so many platforms we can use to make our chat application available for use. Flask authoritatively recommends [several hosting platforms](https://flask.palletsprojects.com/en/3.0.x/deploying/#hosting-platforms). The use of a platform largely depends on your skill level. 

- The easiest platforms are the likes of [Python Anywhere](https://help.pythonanywhere.com/pages/Flask/) and [Render](https://render.com/) (our focus). They are mostly free, and they do the hard work in the background for us. 
- On the hardest end of the spectrum, we have Linux servers such as [Linode](https://www.linode.com/) and [Digital Ocean](https://www.digitalocean.com/) which require us to manually set up everything. 
- Currently, the world is mostly **cloud-based**. Companies and individuals alike store their resources online. One popular cloud platform is [Docker](https://www.docker.com/) which uses the **container** technology to package software. Here, part of the setup work is done for us while we are tasked with doing the other half.


## Render

Render has lately become one of the most popular hosting platforms around. It is free when you choose the lowest package which has minimal features. If you would like to get more features, such as quick server spin times, you will have to upgrade to a paid version. We are going to utilize the free version in this chapter.

### Why Render

- It is very suitable for beginners
- The setup process and deployment procedure is simple
- There is a free tier version, which is great for prototyping
- Render has a fantastic customer support

To get started, visit [render.com (click here)](https://render.com/). You will be redirected to their landing page. From there, sign up for an account by clicking on the "GET STARTED" button seen in the image below. Alternatively, click this link: [Get Started](https://dashboard.render.com/register).

![Get started](images/deployment/get_started.png)

Render provides us with four options to create an account. Click on the "GitHub" button to create one.

![GitHub signup](images/deployment/github_signup.png)

You will need to authorize GitHub to accept Render by clicking on "Authorize Render".

![GitHub authorize render](images/deployment/github_authorize_render.png)

Complete the signup process by clicking on the "COMPLETE SIGN UP" button

![Complete sign up](images/deployment/complete_sign_up.png)

Check your email (the email used during registration) for a verification link. Click on it.

![Verify email](images/deployment/verify_email.png)

Render will expect you to fill in some extra information about yourself. Please do so to complete the setup process.

![More signup info](images/deployment/more_signup_info.png)

And that is it. We have successfully created a new Render account.  The redirection takes you to your dashboard.


## Prepare The Application For Deployment

With our new account set up, it is time to learn how to host our application. The Render user interface is extremely simple and it has great `git` integration, allowing us to run our application in minutes. Thankfully, Render supports several languages including Python.


### Development Server Versus Production Server

During development, we have been using the `development` server to test our application. You probably saw countless times Flask warned us that the environment we have been using is for **development**. 

![Flask dev server warning](images/deployment/flask_dev_server_warning.png)

In production (this means when the app is being used publicly), we need to switch to a **production web server gateway interface (WSGI)** server. This is because the local development server cannot handle user traffic (the number of people using the application). When we are live, we expect that there may be several users, and therefore, a server capable of handling huge traffic is needed so that the application does not crash.


### Gunicorn

[Gunicorn](https://gunicorn.org/) is a Python web server gateway interface, fantastic when you want to host an application that has Python code. We will need to download and install it in our virtual environment.

![Install gunicorn](images/deployment/install_gunicorn.png)


### Update Dependancy File

We have been installing a lot of Flask packages throughout our development. You probably have noticed, and maybe occasionally interacted, with the `requirements.txt` file. This file is very important as it **lists all the extensions needed to create our chat application**. Think of it as a "menu" of the things needed to build the app. We need to update it so that all our installed packages, including the latest `gunicorn`, are listed there.

![Update requirements](images/deployment/update_requirements2.png)

You will notice that the list will be updated automatically for us. When we deploy, Render will look at this file and use it to install the same dependencies in the live version of our chat application.

### Push Your Work To GitHub

As soon as we update the `requirements.txt` file, we need to push our changes to GitHub. Render will use the repository containing our code to host our application. Kindly do so.

```python
(venv) git status
(venv) git add .
(venv) git commit -m 'Dev: Update app for deployment'
(venv) git push origin main
```

You should see all your work in GitHub. Remember to include an updated `README.md` file exhaustively describing what the project is about and how to use it.

![Project in GitHub](images/deployment/project_in_github.png)


## Deploy On Render

Render will utilize our project's repo in GitHub (that is partly why we signed up using it) to quickly host the application for us. To get started with hosting, click on the "New" button in your Render dashboard.

![New web service](images/deployment/create_web_service.png)

Select "Web Service".

![Select web service](images/deployment/select_web_service.png)

Choose to build and deploy from a Git repository.

![Select git repo](images/deployment/select_git_repo.png)


From the list shown, click on the button called "Connect" which is linked to your chat application's repo. Often, it is the repo with the latest changes.

![Click connect](images/deployment/click_connect.png)

The new web service will need us to configure (set up) a few things. For instance, we need to give our new service a **Name**. We also need to ensure that the "Start Command" input field is correctly set as `gunicorn main:app`. We have replatced `app:app` to `main:app` because our entry file into the application is the `main.py`. Hence the name `main` in the Startup Command.

![Configure web service](images/deployment/configure_web_service.png)

Scroll down to the very bottom of the web service page. Click on **Advanced**.

![Click advanced](images/deployment/click_advanced.png)

You will see a new section show up. What we are interested in is the button that says "Add Environment Variable".

![Add environment variable button](images/deployment/add_env_variable_btn.png)


In [Chapter 13: Error Handling](/12_error_handling.md#secret-configuration-values), we learned about the `.env` file. This file is very sensitive as it contains secret values about our application. We said that his file should NEVER be committed to version control. If you check your GitHub repo, it does not exist. 

![Email values](images/handling_errors/secret_email_values2.png)

Render expects the values in `.env` to fully set up our application for us. Within the secret environment variable fields, we are going to add each one of them.

![Add environment variable values](images/deployment/add_env_variable_values.png)

> For Flask to work, you will need to add the following environment variable:
>
> `PYTHON_VERSION 3.8.10`

Once done, scroll to the very bottom and click on the "Create Web Service" button.

![Create web service finally](images/deployment/create_web_service_finally.png)

You will be redirected to the following page.

![Deployment logs](images/deployment/deployment_logs.png)

Hopefully, everything works well without any errors. Render does a good job of letting us know if a deployment was successful or not. For a failed deployment, you will see a "red" cloud; for a successful deployment, you will see a "green" cloud.

Should the latest deployment indicate "Deploy live ...", then you can click on your web service link to access the page.

![Click live link](images/deployment/click_live_link.png)

And there you have your publicly accessible live link that can handle user traffic! Congratulations! Feel free to share this link with other people. Begin by sharing it in the "Explore Community" chat feature of our eLearning app.

## Assessment


Add a link to your GitHub repo redirecting to your live application. 

![Add live link](images/deployment/add_live_link.png)

Then, share the link to your GitHub repository in the quiz section below.

## Quiz

1. Which of the following packages can you use for your production application? 

- [ ] Nginx
- [x] Gunicorn
- [ ] Requirements.txt
- [ ] Render

2. What can you use to isolate the needs of your application from another during installation?

- [x] Virtual environment
- [ ] pip3
- [ ] Python
- [ ] Flask

3. Which among the following can be used to deploy and host your Python-powered application?

- [ ] Gunicorn
- [ ] GitHub
- [x] Microsoft Azure
- [ ] Google

4. Which platform is the hardest when you want to host your Python application?

- [ ] Render
- [ ] Google App Engine
- [ ] Python Anywhere
- [x] Linode

5. What is to deploy?

- [x] To make something available for use
- [ ] To send troops to war
- [ ] To create a cloud platform
- [ ] To add environment variables on Render