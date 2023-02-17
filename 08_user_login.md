# Handling User Logins

In [chapter 6](06_web_forms.md), you learnt how to create web forms. You saw how to create login form as well as a registration form. In this chapter, you will learn how to combine these concepts to create a simple user login system.

![Chapter 7 Assessment project](images/user_login/user_login.gif)

Throughout this tutorial, these are the reference links of the things we will be looking at. At your own convinience, you can navigate to whatever article you want to refer to:

1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates in Flask](05_working_with_templates.md)
6. [Web forms](06_web_forms.md)
7. [Database](07_database.md)
8. [User Login](08_user_login.md) (this article)
9. [Profile Page and Avatars](09_profile_page_and_avatars.md)
10. [Error Handling](10_error_handling.md)
11. [Pagination](11_pagination.md)
12. [Working With Email](12_working_with_email.md)
13. [Better-looking Application](13_better_looking_application.md)
14. [Timestamp](14_timestamp.md)
15. [Deployment on Render](15_deployment_on_render.md)


### Lesson Objectives

By the end of this lesson, you should be able to:

- Create both login and register forms
- Create a view function that handles user login
- Create a view function that handles user registration
- Add a user to the database during registration
- Query the database for an existing user
- Display a useful message when a user registers or logs into their account
- Redirect a user to a relevant page once registered or logged in
- Render relevant web templates


## Table of Contents


## Password Hashing

In the last chapter on [database](07_database.md), we saw that one of the fields we may choose to add to a model is the _password_hash_. This field, we mentioned, stores a user's password not in its raw form but as a represention of itself. This process of converting a user's password into a hash is a complicated concept, but thankfully, there are simpler ways to implement it. 

The [Werkzeug](http://werkzeug.pocoo.org/) package is installed when we install `flask`, and it is one of the core dependancies. Below, let us see how it works. Ensure you have activated your virtual environment and are working in a flask shell:

![Password hash](images/user_login/password_hash.png)

Above, I begin by importing `generate_password_hash` from `werkzeug.security`. As mentioned, simple functions such as this one allow us to easily interact and implement the complex concept of passworh hashing. We then pass our password, `muthoni` to this function and save it in a variable called `hash`. When we run `hash`, we see an strange long cryptographic value which represents our earlier password `muthoni'.