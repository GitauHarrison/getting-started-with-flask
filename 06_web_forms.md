# Web Forms

Now that you have learnt about [templates in Flask](05_working_with_templates.md), we are ready to build a more robust and useful application. Below is the app we shall focus on throughout the remainder of our lessons.

![Simple chat app](/images/web_forms/simple_chat_app.gif)


Throughout this tutorial, these are the reference links of the things we will be looking at. At your own convinience, you can navigate to whatever article you want to refer to:

1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates in Flask](05_working_with_templates.md)
6. [Web forms](06_web_forms.md) (this article)
7. [Database](07_database.md)


This article will cover these topics:

- [Overview](#overview)
- [Web Form Configuration](#web-form-configuration)
- [Create The Login Form](#create-login-form)
- [Render the Login Form](#render-the-login-form)
- [Receiving Form Data](#receiving-form-data)
- [Improving Form Validation](#improving-form-validation)
- [Generating Links](#generating-links)
- [Assignment: Push Updated Project to GitHub](#assignment-push-updated-project-to-github)



## Overview

Web forms are one of the fundamental building blocks of any web application. They are used primarily to collect user information. In our application example seen above, you may have noticed two forms:

- Login form
- Registration form

The Registration Form allows a new user to share their information necessary to create an account. On the other hand, the Login Form is used to allow a returning user to access their account.


## Web Form Configuration

Flask provides a package called [Flask-wtf](http://packages.python.org/Flask-WTF) which is useful in the creation of web forms. It is the first extension we will be installing, but definitely not the last one. 


### Step 1: Activate Your Virtual Environment

Before we can install this package, we have to activate our virtual environment.

![Activate VirtualEnv](images/web_forms/activate_venv.png)


### Step 2: Install Flask-WTF

To work with this extension, we need to install it in our active virtual environment.

![Install wtf](images/web_forms/install_wtf_fixed.png)


### Step 3: Create SECERET_KEY Configuration File

Flask expects certain configurations when creating an application. The first configuration that Flask expects, especially when working with web forms, is the `SECERET_KEY` configuration. To handle this new demand, let us go ahead and create a new file called `config.py` in the top-level directory.

![Create config file](images/web_forms/create_config_file_fixed.png)


### Step 4: Update Configuration File

This file shall use a class called `Config()` to define all the configurations our application will need. The first is `SECERET_KEY`. Add the following code to your `config.py` file.

![Update secret key config](images/web_forms/secret_key_config.png)

Phew! Quite a lot going on there. Let us break it down. The `SECERET_KEY` configuration that we added is crucial for any Flask application. Flask-WTF uses it to protect our forms against a nasty attack called [Cross-site Request Forgery](http://en.wikipedia.org/wiki/Cross-site_request_forgery), or CSRF in short (it is pronounced as "seasurf").

As the name implies, it is supposed to be a **secret**. Only you or the maintainer of the application should know this value. What is the value? You may ask. The value of the `SECERET_KEY` is sourced from the Operating System as an environement variable. 

```python
# config.py

SECRET_KEY = os.environ.get('SECRET_KEY') # < --- this is the OS value
```

If this value is not available, we provide a fallback value to ensure that our application does not crash.

```python
# config.py

SECRET_KEY = 'hard-to-guess' # < --- this is the fallback value
```

Combined, the application will begin by first looking for the OS generated value then revert to the fallback value if the original value is missing.


### Step 5: Register The Configuration in the Application Instance

Once we have defined our configurations, we need to tell our application how to access them. This is done in `app/__init__.py`.

![Register configurations](/images/web_forms/register_configs.png)

It might be confusing understanding what `from config import Config` means. Basically, 
- The first `config`, with a small "c", is the file `config.py`. 
- The second `Config`, with a capital "C", is the class name found inside our file `config.py`.

We are importing the class `Config()` from our new `config.py` file in order to access the value of our `SECRET_KEY`. 


### Step 6: Access the SECRET_KEY

It is always a good idea to continously test every new feature we build. In this case, it is advisable to test whether our application can access the value of the `SECRET_KEY`. To do this, we need to activate the Python Interpreter.

![Activate Python prompt](/images/web_forms/python_prompt.png)

Then run the commands below:

![Access secret key](/images/web_forms/access_secret_key.png)

You should be able to see the value "hard-to-guess" printed in the Python prompt. If not, it means your application cannot access this value. Go back and refer to the ealier lessons to find out how you can fix it.

Once you are done, type `exit()` to close the Python interpreter. Alternatively, you can press "Ctrl + Z" on your keyboard.


## Create Login Form

Flask-WTF uses classes to define the input fields we would like to have in our forms. 


### Step 1: Create a Forms Module

Let us create a new file within _app_ folder called `forms.py`. 

![Create forms module](/images/web_forms/forms_module.png)


### Step 2: Add a Login Class

As mentioned, a class is used to define the input fields we want to have in our Login Form. If you look at our Simple Chat Application, the login form has a username field, and a password field. It also features a button that allows a user to log in to their accounts.

![Login form](/images/web_forms/login_form.png)

Within the `forms.py` module, add the class below.

![Login class](/images/web_forms/login_class.png)

We begin by importing a few useful methods from Flask-WTF. We then define each field as a variable of its function. For example, the `username` variable will accept user data of type `String` hence the function `StringField`. `DataRequired()` forces a user to provide their information before pressing the `Submit` button.


### Step 3: Create a Login Template

The next step is to add the login form to a template so that it can be rendered to a web page. The good thing is that we do not have to worry about how the rendering will take place; the class `LoginForm()` will do that for us. Begin by creating a `login.html` file within the templates sub-folder.

![Create login template](/images/web_forms/login_template.png)

Then add the following HTML code that creates a form.

![Login template code](/images/web_forms/login_template_code.png)

What is going on in our `login.html` file?

- We begin by inheriting the base template using the keyword `extends`. This allows the login template to acquire all the attributes of the base template.
- We define three columns, two of which are empty while the middle one contains the actual form.
- A form is defined using the element `<form></form>`. 
- The `action` attribute is used to tell the browser what URL should be used to submit the form details. If it is empty, as seen in our case, then the browser will use the URL currently in the address bar.
- The `method` attribute is used define how the user data should be submitted. `post` method is used to send data while `get` method is used to retrieve data.
- The `novalidate` attribute tells the browser not to implement any type of validation to the form fields, which effectively leaves the task to Flask. 
- `form.hidden_tag()` is a special function from Flask-WTF which adds a token to protect the form against CSRF attacks. All you need to do to protect a form is to include this line. 

A label in a form is the text above a field that helps the user to know what information is needed in an input field. For example, a username label will contain the text "Username" so a user knows that the field requires their username.

![Labels](/images/web_forms/labels.png)

Back to our login template:

- `{{ form.username.label }}` dynamically displays the label used in the `username` variable seen in `forms.py` file.
- `{{ form.username(size=32) }}` creates the actual input field, accepting a username of size 32 characters.
- The same applies to the password label and field.
- The `remember me` radio button is structured slightly differently so that the input field comes first followed by the actual field label.
- ` {{ form.submit() }} ` is responsible for displaying the Login button

Remember, the words `username`, `password`, `remember_me` and `submit` (used in conjunction with `form`) are defined in the `forms.py` file.


## Render The Login Form

As earlier discussed, rendering means to 'make available'. Below, you will learn how to render form template.

### Step 1: Create A Login View Function

With the template clearly defined, we can create a view function to render it. This is done in `app/routes.py` file.

![Render login form](/images/web_forms/render_login_form.png)

- To access the `LoginForm()` class, we import it from the `forms` module.
- We then create a new view function called `login()` which renders the form.
- We create a new variable called `form` to define the `LoginForm()` class.
- We then pass in the word `form=form` within the `render_template()` function to ensure that the `login.html` file has access to it.


### Step 2: Add a Login Link in Base Template

How can we access this login page? Obviously, we need to create a link to it. This can be done in the base template.

![Add login link](/images/web_forms/add_login_link.png)


### Step 3: See the Output

Run your application by typing `flask run` in the terminal, if you haven't done so, then paste the localhost link http://127.0.0.1:5000/login in your favourite browser to see the output.

![Login form in browser](/images/web_forms/login_form_in_browser.png)


## Receiving Form Data

At this point, you might be curious and eager to start sending data using our login form. If you have tried to send data using our form as it currently is, you will most likely come across the 405 error below.

![Method error](/images/web_forms/method_error.png)

The reason for this error is because we have not fully completed defining our `login()` view function. This section is dedicated to making our login form partially usable.


### Step 1: Add POST and GET Methods

The first step to overcoming this error is to explictly define both `POST` and `GET` methods in our `app.route()` methods. 

![Define post and get methods](/images/web_forms/post_get_methods.png)

- `POST` method is used to send data through a form
- `GET` method is used to retrieve form data

Now, if you try to click on the submit button found in our Login form, you will not get the 405 error we experienced earlier.

![Define post and get methods](/images/web_forms/post_get_methods.gif)

Have you noticed that when we click the Submit button the form does not tell us that we need to in fill in the username and password fields? Remember we said that the constraint `DataRequired()` in our `forms.py` file is meant to force for a user's input. How come it is not working in our new form? [This is something we shall revisit in another subsection within our lesson](#step-3-flash-message).


### Step 2: Validate Form Submission

We can now process the data a user submits through our login form. This can be handled by the `form.validate_on_submit()` function. Update the `login()` view function as seen below.

![Validate form submission](/images/web_forms/validate_form_submission_fixed.png)

- The `flash()` function is used to display a user-friendly message on the website saying "You are are requesting to login as [username]".
- This function comes from flask and therefore has to be imported as seen on line #2.
- Once the user submits their data, they will be redirected to the URL `/index`.
- The `redirect()` function also comes from flask, and therefore, needs to imported too.

Let us try to fill in some user data to test how this feature works.

![Login flash and redirect](/images/web_forms/login_flash_redirect.gif)


### Step 3: Flash Message

Once the submit button is pressed, I am redirected to the index template. However, the `flash` message does not show up. It does not magically appear, we have to update our code in `base.html` file to define this small but useful little feature.

![Add flash message functionality](/images/web_forms/flash_message_functionality.png)

Now, if I try to login in as "tanya", there will be a nice little flash message.

![Flash message working](/images/web_forms/flash_message_working.gif)


## Improving Form Validation

With the flash message functionality now in place, we can further improve a user's experience when interacting with the Login form. In the event the user makes a mistake filling the form, there should be some useful feedback to guide them. 

### Step 1: Update Login Template

Let us update `login.html` file to provide user feedback.

![Improve UX login form](/images/web_forms/ux_login_form.png)

- We have used a `for` loop from Python to loop through all possible error messages.
- If there is an error message in the username form field, then the message will be displayed below the input field in "red" color.
- If there is an error message in the password form field, then the message will be displayed below the input field in "red" color.


### Step 2: Test Application on the Browser

Once again, let us test this feature. Head over to your application on the browser and try clicking the "Submit" button without filling in user information.

![Form flash message](/images/web_forms/form_flash_message.gif)


## Generating Links

Throughout the base template, we have been explictly using the URL of a page to access it. This is what we have been doing:

```html
<!-- URL to the home page -->
<div class="col-md-4">
    <h1><a href="/index">Home</a></h1>
</div>

<!-- URL to the about me page -->
<div class="col-md-4">
    <h1><a href="/about-me">About Me</a></h1>
</div>

<!-- URL to the about me page -->
<div class="col-md-4">
    <h1><a href="/login">Login</a></h1>
</div>
```

What if later we decide to change the URL to any of these pages to something else? Say we now think that the home page should no longer be accessed using `/index` but instead the URL `/home` should be used. What happens if we try to do so in our browser?

![Change URL](/images/web_forms/change_url.gif)

Obviously, we get an error because there is no URL such as `/home` anywhere in our application. To avoid such inconviniencing situations, especially when your application become bigger, it is recommended that we use a flask function called `url_for()`. 

This function uses the name of the view function instead of the URL name. It is less likely that we will change the view function name when compared to the URL name. 

### Step 1: Update All Links in Base Template

All our links exist in the base template. So, let us head over there and change a few things.

![Update base template links](/images/web_forms/update_base_template_links.png)


### Step 2: Import URL_FOR from Flask


To use this function, we need to explicitly import it from flask. This is done in `app/routes.py` file.

![Import url_for](/images/web_forms/import_url_for.png)


### Step 3: Update URL

Now, we have a bit more breathing room should we forget to change every occurrance of `/index` URL. All we need to do now is to update the `index()` view function URL to `/home` and that will apply across their entire application.

![Update index url](/images/web_forms/update_index_url.png)

In our browser, we can see the change applied.

![View function from browser](/images/web_forms/view_function_from_browser.png)


## Assignment: Push Updated Project to GitHub

Ensure you do the following before you end this lesson:

- [ ] Update your `requirements.txt` file to show that you have used `Flask-WTF`
- [ ] Update your `README.md` file to highlight as much of the changes you have made
- [ ] Push your changes to your project's GitHub repository