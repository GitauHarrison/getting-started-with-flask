# Adding User Profile Page and Avatar

During this lesson, we are going to learn how to add a profile page for the user. A profile page allows a user to see his or her personal details. It is in this page that the user can update or modify personal information.

![Chapter 9 final app](images/profile_page_avatars/profile_page_avata.gif)

Throughout this tutorial, these are the reference links of the things we will be looking at. At your own convinience, you can navigate to whatever article you want to refer to:

1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates in Flask](05_working_with_templates.md)
6. [Web forms](06_web_forms.md)
7. [Database](07_database.md)
8. [User Login](08_user_login.md)
9. [Profile Page and Avatars](09_profile_page_and_avatars.md) (this article)
10. [Error Handling](10_error_handling.md)
11. [Pagination](11_pagination.md)
12. [Working With Email](12_working_with_email.md)
13. [Better-looking Application](13_better_looking_application.md)
14. [Timestamp](14_timestamp.md)
15. [Deployment on Render](15_deployment_on_render.md)


### Lesson Objectives

By the end of this lesson, you should be able to:

- Add a comment form in the home page
- Create a new page for a user's profile
- Update your models to ensure that a user's post is saved in the database
- Display a user's information found in the database
- Extend the database to include additional useful fields such as _timestamp_ and _about_me_
- Add an avatar for a user
- Display all users' comments in the home page
- Display all the comments by a user in their profile page

### Table of Contents

- [Overview](#overview)
- [User Profile Page](#user-profile-page)
- [Display User Profile Link](#display-user-profile-link)
- [Add User Email Field In The Database](#add-user-email-field-in-the-database)
- [Update User Registration Form](#update-user-registration-form)
- [Store User Email Address In The Database](#store-user-email-address-in-the-database)
- [Avatars](#avatars)
- [Display User Information In The Profile Page](#display-user-information-in-the-profile-page)


## Overview

Profile pages are a crucial part in any software application. A profile page allows a user to interact with his or her personal information as they please. You have the freedom to decide what user information can be altered and what cannot be altered as you build a profile page. 

In our [previous lesson](08_user_login.md), you learnt how to create a basic user authentication system. This system is used to indentify a user before they can access certain pages of our application. In the lesson, we had a page called **About Me**. This page had dummy content that we used as placeholder data. In this lesson, we are going to transform this page into a true **Profile** page. In it, we shall allow a logged-in user to see the following:

- The user's avatar
- The user's username
- The user's email
- All the posts made by the logged in user

Remember the final application we have in mind? It is a simple chat application (see the image below. It is also what we discussed in the overview of [chapter 6](06_web_forms.md#overview)).

![Simple chat app](images/web_forms/simple_chat_app.gif)

In this lesson, we are going to make several modifications to our existing application, namely:

- We shall rename the **About Me** page to the **Profile** page
- We shall transform the new **Profile** page into a true profile page with personal user data
- We shall update our `User` model to allow for an `email` field during user registration
- We shall display a user's avatar in the **Profile** page
- We shall modify the home page to include a **Post form** where any user can leave a comment
- We shall display all users' comments in the home page
- We shall display the current user's posts (who is logged in) in their profile page
- We shall update a user's profile page to include a timestamp of when they were last seen
- We shall also include an ** About me** field in the user's profile page


## User Profile Page

Let us begin by updating our current view function `about_me()`  by renaming it to `profile()`. This view function is found in the `routes.py` file. We shall also add a few more functions to it as seen in the image below.

![Profile page view function](images/profile_page_avatars/profile_view_function.png)

Because the **Profile** page is specific to a user, it would be best to have it display the name of the current user. This is achieved by passing in `<username>` in the `@app.route()` decorator. Notice that this variable is also passed as an argument to the view function as `def profile(username)`. 

When a user such as `muthoni` logs into her account, the URL will change to `http://127.0.0.1/muthoni/profile`. If another user called `gitau` logs into his account, then the URL will change to `http://127.0.0.1/gitau/profile`. This is made possible by our query below:

```python
# app/routes.py


@app.route('/<username>/profile')
@login_required
def profile(username):
    # ...
    user = User.query.filter_by(username=username).first_or_404
    # ...
```

We query our `User` model using `User.query`. Since we want to get a specific user from the database, SQLAlchemy (the tool that allows us to interact with the database) provides the `.filter_by()` function in which we pass the `username` variable. It is a variable because the value stored in it will keep changing depending on the logged in user. The first `username` is the field seen in the `User` model.

```python
# app/models.py


class User(UserMixin, db.Model):
    # ...
    username = db.Column(db.String(64), index=True, unique=True)
    # ...
```

The second `username` in the query is the actual username of the logged in user. In this case, it could be `muthoni` or `gitau`. Combined, we are querying the database to find a user whose username is stored in the variable `username`.

The `.first_or_404()` function is used to get the first occurance of the user (hence `first`). If this user does not exist, we tell the database to return a `404` error, which means "The user was not found". This is a neat way to ensure that our application does not crash in the event a user does not exist.

The result is then stored in a variable called `user`. We pass this variable to our templates by adding it to the `render_template()` function as seen below (you have this already, as seen in the image above)

```python
@app.route('/<username>/profile')
@login_required
def profile(username):
    # ...
    return render_template( ..., user=user)
    
```

This allows us to interact with the `user` object as retrieved from the database. For example, if we want to get the user's username, we will do `user.username`. But before we can display this user in our application, we need to rename the `about_me.html` file to `profile.html` file.

![Rename profile template](images/profile_page_avatars/rename_profile_template.png)

Once you have renamed it, you will have a new template called `profile.html` in your _templates_ subdirectory.

![Profile template](images/profile_page_avatars/profile_template.png)


## Display User Profile Link

With the view function in place, we can now update our `base.html` file to show a link to the **Profile** page.

![Profile page link](images/profile_page_avatars/profile_page_link.png)

The column sizes have been modified to `col-md-4`. A new link called **Profile** has been added to the list of links once a user has been authenticated. Unlike all other links, the **Profile** page link is slightly different. It includes an additional section ` {{ (..., username=current_user.username) }}`. This is so because we are passing the current user's username into the URL. Every time we have a view function that requires a variable in the URL, we shall always be adding this section to it.

![Profile page](images/profile_page_avatars/profile_page.gif)


## Add User Email Field In The Database

In [chapter 7](07_database.md), you learnt how to store a user's information in a database. In particular, you learnt how to store a user's usename and password in a database. In this section, we are going to extend the `User` model to allow for the storage of a user's email address. Why an email address? We shall need it to generate a user's avatar as seen in a subsequent section. Modify your `User` model as seen below (If you already have this section completed, then there is no need for you to do this. Skip to the next section):

![Email field in user model](images/profile_page_avatars/email_field_user_model2.png)

Since this addition causes a change in the structure of our `User` model, we need to run our migrations to apply the changes. In your terminal, run the commands below (ensure you are in the root folder of the project and your virtual environment is activated):

```python
(venv)$ flask db migrate -m 'email field'
(venv)$ flask db upgrade
```

![Email migrations](images/profile_page_avatars/email_migrations.png)


As soon as you run those, you should see a new migration script in the _migrations_ subdirectory called `...email_field.py`.

## Update User Registration Form

With the new email field in place, we need to provide a means for the user to fill in their email address during registration. First, let us update our `RegisterForm()` to include an `email` field.

![Email form field](images/profile_page_avatars/email_form_field.png)

This new `email` field is not so different from the `username` field. It only adds the `Email()` validator from `flask-wtf` which is used to check if the data keyed in by a user has an email format (it does not verify if the email is real or not). To ensure that this `Email()` validator works, we need to install the `email-validator` extension in our virtual environment as seen below:

![Email validator extension](images/profile_page_avatars/email_validator_extension.png)

Now, we can modify our `register.html` template to add an `email` field as follows:

![Email field in template](images/profile_page_avatars/email_field_in_template.png)

You should see an email field being displayed in your **Register** page.

![Email](images/profile_page_avatars/email.png)


## Store User Email Address In The Database

The registration form now allows a user to add their email address. To ensure that this email is saved in the database, we will modify the `register()` view function which handles all user registration functionality.

![Save email in db](images/profile_page_avatars/save_email_in_db.png)

With that, every registration will update our database to include a user's email address.


## Avatars

An avatar is an icon or a figure representing a particula person. Given that we are building a chat application, wouldn't it be nice if each user post had an avatar of the author of a post? Besides, being able to see one's own avatar in the **Profile** page makes the page a lot more attractive, and less boring. Look at the image below; it shows each post having an avatar of the author.

![User](images/profile_page_avatars/user_avatar.png)

We shall take a shortcut here. Instead of allowing users to upload their own avatars and, in the process, strain the application with handling large collections of uploaded images, I would like to introduce you to the [Gravatar](http://gravatar.com/) service. We shall use this service to provide images for all users.

To request an image for a given user, a URL with the format `https://www.gravatat.com/avatar/<hash>`, where `<hash>` is the MD5 hash of the user's email address. Remember above where we mentioned that we shall use a user's email address to generate an avatar for them? Below is how it can be achieved. Enter into an active Python prompt in your terminal and run the commands below:

![Avatar link](images/profile_page_avatars/avatar_link.png)

The result is a link that points to a user's avatar (an image). If you would like to see one of your teacher's avatar, you can paste the link https://www.gravatar.com/avatar/aa4d7225b5276efcfbbf556ff1b5676f in a browser.

The default size of an avatar is 80 by 80 pixels. We are not limited to this size. If we would like a different size, we can request it by adding `s` argument to the URL query string. For example, to obtain your teacher's avatar as a 160 by 160 pixel image, the URL will be https://www.gravatar.com/avatar/aa4d7225b5276efcfbbf556ff1b5676f?s=160. **Add `?s=<size>` to the end of the query string.**

The teacher's link above is an actual image because he has uploaded an actual image as his gravatar. Besides an actual image, we instruct the Gravatar service to choose for us an image of its choice. Gravatar has several options to choose from. A favourite for many is the `identicon`. To use it, just like the `size` argument, we pass the `d` query string. Every email address will have its unique avatar. If you are wondering what other options Gravatar has, refer to this [Gravatar documentation](http://en.gravatar.com/site/implement/images/). You will see `404`, `monsteroid` among others.

Because avatars are tied to a user's email address, it, therefore, makes sense to tie it to the `User` model. This model is associated with users. Add the following logic in the `User` class.

![Avatar logic](images/profile_page_avatars/avatar_logic.png)

The new `avatar()` method of the `User` class returns a URL of the user's avatar image, scaled to the requested size in pixels. For users without an avatar registered, and "identicon" image will be generated for them. To generate the MD5 hash, we begin by converting a user's email address to lower case (using the `.lower()` method). This is required by the Gravatar service. Since md5 in Python works on bytes and not on strings, we encode the string as bytes before passing it to the hash function.


## Display User Information In The Profile Page

As soon as a user is registered and logged in, they will have access to the **Profile** link in the navigation bar. Once this link is clicked, let us display a user's personal information in their profile page.

![Update profile template](images/profile_page_avatars/update_profile_template.png)

The first column (`col-md-5`) has an `<img>` tag with a dynamic link to a user's avatar. We use the double curly braces (`{{  }}` ) to indicate that the data here can change. In this case, the data to change is dependant on what `user` has logged in. We call the `avatar()` method on each user to apply an avatar.

The second column (`col-md-7`) has been used to display the logged-in user's username and email address. Once again, the double curly braces indicate that the values presented here can change, it it does, automatically. At the end, our profile page will now look like this:

![Profile page 1](images/profile_page_avatars/profile_page1.png)
