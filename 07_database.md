# Database

![Database](images/database/database.jpg)
*
**A database is an organized collection of structured information, or data, typically stored electronically in a computer system**. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.

Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use structured query language (SQL) for writing and querying data.

Throughout this tutorial, these are the reference links of the things we will be looking at. At your own convinience, you can navigate to whatever article you want to refer to:

1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates in Flask](05_working_with_templates.md)
6. [Web forms](06_web_forms.md)
7. [Database](07_database.md) (this article)
8. [User Login](08_user_login.md)
9. [Profile Page and Avatars](09_profile_page_and_avatars.md)
10. [Error Handling](10_error_handling.md)
11. [Pagination](11_pagination.md)
12. [Working With Email](12_working_with_email.md)
13. [Better-looking Application](13_better_looking_application.md)
14. [Timestamp](14_timestamp.md)
15. [Deployment on Render](15_deployment_on_render.md)


### Table of Contents

By the end of this lesson, you should be able to:

- Understand what a database is
- Know what language is used to write and query a database
- Create datababase configurations
- Define a database model
- Create migration scripts
- Update a database structure
- Apply changes to a database

## Overview

Flask does not support databases natively. This is in line with its philosophy of remaining lean and extensible. As developers, we have the freedom to choose what database we want to use instead of being forced to adapt to one.

Databases are categorized into two large groups (1) relational database and (2) Non-relational databases. Databases are written and read using  the popular relational query language [SQL(Structured Query Language)](https://en.wikipedia.org/wiki/SQL). Throughout our lesson, we shall focus on using a relational database model since it is so much easier to use when you have structured data such as blog posts or even a list of users.

In [chapter 3](03_getting_started_with_flask.md), you learnt how to install a Flask extension. During this chapter, you will install a few more extensions to help us work with a database. The first extension you will install is called [Flask-SQLAlchemy](http://packages.python.org/Flask-SQLAlchemy). It provides a Flask-friendly wrapper around the popular [SQLAlchemy](http://www.sqlalchemy.org/) package. What SQLAlchemy does is that it converts high-level classes, objects and methods into tables and SQL.

We have different types of databases such as [PostgreSQL](https://www.postgresql.org/), [MySQL](https://www.mysql.com/) and [SQLite](https://www.sqlite.org/). They are all very powerful. **We shall use the SQLite database for our project**. It is not only very convinient for small applications, but it can also be extended to handle large applications.

In your terminal, you can install this application as follows (remember to activate your virtual environment):

```python
(venv)$ pip3 install flask-sqlalchemy
```
![Install flask sqlalchemy](images/database/instal_flask_sqlalchemy.png)


## Migrations

The other extension we shall be using is [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate). Migrations involve making updates to a model. For example, if we have a model that stores user information such as username and password, then at some point we decide to add an email field, this update changes the structure of our database model. What we then need to do is to update this model to our new structure (also know as schema). This update will create a new version of the model. The process of updating a model to another is what we refer to as **migration**. We are migrating our model from _versionA_ to _versionB_.

Install this extension in your active virtual environment as follows:

```python
(venv)$ pip3 install flask-migrate
```

![Install flask migrate](images/database/install_flask_migrate.png)

## Flask-sqlalchemy Configuration

As mentioned earlier, we are going to use SQLite database. This database will be stored as a single file ond disk, typically found in the top-level directory. The advantage of using SQLite is that its setup process does not require a server like MySQL or PostgreSQL. In your `config.py` file, let us do the following:

![Database configuration](images/database/db_configurations.png)

The location of our database is found from `SQLALCHEMY_DATABASE_URI` variable. We begin by sourcing its location from the environment variable called `DATABASE_URL`. If this value does not exist, then we configure a database called `app.db` in the top-level directory of the application. You can call this database anything you want, such as `database.db`. How do we know it is located in the top-level directory? We have set up a `basedir` that defines this folder.

`SQLALCHEMY_TRACK_MODIFICATIONS` is set to `False` so that it does not keep sending signals to the application everytime we make changes to the database. 

Finally, we need to create a database instance. The database configuration engine will also have an instance. These objects are to be created in `app/__init__.py` as follows:

![Database objects](images/database/db_objects.png)

The `db` object represents the database. Additionally, we have created a migration object. To wrap up the configurations, we make sure we import `models` at the bottom of the file. This module is a database schema found in the `app` sub-directory. So ensure that you create a brand new file called `models.py`.

