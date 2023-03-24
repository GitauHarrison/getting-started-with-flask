# Handling Errors

![Chapter 10 intro image](images/handling_errors/sample_error.jpg)

During this lesson, we are going to take a break from adding new features to our application, and instead focus on how to deal with possible bugs which usually come about as we build. So far, can you find any bug in our project?


Throughout this tutorial, these are the reference links for the things we will be looking at. At your convinience, you can navigate to whatever article you want to refer to:

1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates in Flask](05_working_with_templates.md)
6. [Web forms](06_web_forms.md)
7. [Database](07_database.md)
8. [User Login](08_user_login.md)
9. [Profile Page and Avatars](09_profile_page_and_avatars.md)
10. [Error Handling](10_error_handling.md) (this article)
11. [Pagination](11_pagination.md)
12. [Working With Email](12_working_with_email.md)
13. [Better-looking Application](13_better_looking_application.md)
14. [Timestamp](14_timestamp.md)
15. [Deployment on Render](15_deployment_on_render.md)


### Lesson Objectives

By the end of this lesson, you should be able to:

- Know when your application has a possible bug
- You should be able to understand an error message
- Appreciate the DEBUG MODE in Flask
- Create and display custom error pages
- Log errors from the application
- Send error emails to admins
- Log error messages to a file
- Fix the errors currently in the application

### Table of Contents



## What Happens When There Is A Bug?

Let us think about it for a moment. What happens when an error occurs in our Flask application? As an exercise, did you find any bug in our current aplication? To give you a taste of a bug, or an error, let us do the following (head over to your VS Code):

- Remove the line `FLASK_DEBUG=True` from your `.flaskenv` file
- Start your flask server by running `flask run` in the root directory of the project
- Register two more users in the application, for example with the following usernames, `njeri` and `wangari`
- Log in as one of the newly registered users, for example, as `njeri`
- Open the profile page and click on the "Edit Profile" link
- In the profile editor, try to change the username of `njeri` to `wangari`
- Press the button on the editor page to save the changes

What do you encounter? Is it something familiar? How do you get out of it? Is there even a way to get out of it? Imagine a regular user of your application coming across such an error. It will scare them for sure.

When I made the changes mentioned above, my application returned the following error.

![Internal server error](images/handling_errors/internal_server_error.png)

Since we are the developers of our application, we should not panic. Instead, we should learn what this error is about, then try to fix it. If we look at our terminal window where our application is running, you will see a [stack trace](https://en.wikipedia.org/wiki/Stack_trace) of the error. The jargon "stack trace", also known as a traceback, is basically a report of our program at a certain point in time during execution. Stack traces are extremely helpful in debugging errors, because they not only show the sequence of the call in that stack, but they also show the exact line that produced the error.

![Terminal stack trace](images/handling_errors/terminal_stack_trace.png)

In the illustration above, the error points to a failure of SQLAlchemy not validating our changes. Notice that the error says `sqlite3.IntegrityError: UNIQUE constraint failed: user.username`. The issue stems of the `username` column of the `User` model. If we go back to the `models.py` file, we can see that we set the `username` column to `unique=True`.

![Unique constraint in username column](images/handling_errors/unique_constraint.png)

SQLAlchemy strongly rejects our input because we initially set our database NOT TO HAVE DUPLICATE USERNAMES. Each username in the database should be UNIQUE, meaning, there should not be another username similar to an existing one. Any attempt that undermines this instruction will be expressly rejected by the application.

The stack trace presented to us, or to the user, does not provide much information about the error, which is good. We definitely do not want users to learn that the error was a result of a database error. We do not want the user to know what database we are using (the stack trace revealied that our database was SQLite). We, also, do not want to reveal what fields are in our database.

The big issue at hand is how we can present a fairly informative report to the user that is less revealing. And, of course, we have a bug we need to fix.


## The Debug Mode

The stack trace shown above is really useful to a developer on a production server (when your application is live and accessible over the internet). Flask provides a really nice interface, called a debugger, that is displayed on the browser rather than on a terminal window. To activate debug mode, stop the application by pressing "Ctrl + C". Then let us update our `.flaskenv` file as follows (you had this line earlier but we removed it):

```python
# .flaskenv

FLASK_DEBUG=True
```

After that, let us restart our flask server by running `flask run` on our root directory. The output on the terminal is going to be slightly different from what we saw earlier.

![Debug mode enabled](images/handling_errors/debug_mode_enabled.png)

You can see that the terminal output reveals our debug mode is on. Now, let us make the application crash again by [repeating the steps we followed earlier](#what-happens-when-there-is-a-bug). You will see the interactive debugger in your browser.

![Interactive debugger on browser](images/handling_errors/interactive_debugger.png)
