# Working with Templates in Flask

![Templates Hero image](images/flask_templates/template.jpg)

A template is basically an HTML file. In our previous lesson [Getting Started With Flask](03_getting_started_with_flask.md), we learnt how to display the text "Hello, world" on a browser. 

![See flask on browser](images/getting_started_with_flask/flask_on_browser.png)

What if you want to add more structure to your application, like paragraphs and images? How can you do that in Flask? This is where templates come in. They allow us to achieve all the structural features we may want added to our application.

Throughout this tutorial, these are the reference links of the things we will be looking at. At your own convinience, you can navigate to whatever article you want to refer to:

1. [Getting Started with HTML and CSS](01_getting_started_with_HTML_and_CSS.md)
2. [Git and GitHub](02_git_and_github.md)
3. [Getting Started with Flask](03_getting_started_with_flask.md)
4. [Introduction to Bootstrap](04_bootstrap_intro.md)
5. [Working with Templates in Flask](05_working_with_templates.md)   (this article)
6. [Web forms](06_web_forms.md)
7. [Database](07_database.md)



This article will cover these topics:

- [Getting Started With Templates](#getting-started-with-templates)
- [Separate Presentation from Business Logic](#separate-presentation-from-business-logic)
- [Smarter Templates](#smarter-templates)
- [Template Inheritance](#template-inheritance)
- [Assignment: Push To GitHub](#assignment-push-to-github)


## Getting Started With Templates

Building on our initial app, _hello flask_, let us see how we can add HTML files in Flask. First ensure you have your application ready.

### Step 1: Navigate to Your Application Directory

In the terminal, change the directory to our application's.

![Current project directory](images/flask_templates/current_directory.png)


### Step 2: Activate Your Virtual Environment

It is always important to be working in an active virtual environment. So make sure you have it active.

![Activate venv](/images/flask_templates/activate_venv.png)


## Separate Presentation from Business Logic

Presetation, as we now know, is handled by HTML files. Flask, on the other hand, has extra Python files that do not necessarily 'present' anything. They are used to do other tasks. These 'other tasks' is what we are calling 'business logic'. They are important in the running of our application.


### Step 1: Create a templates sub-folder

To ensure that our application maintains a proper structure, we will create a new sub-folder called _templates_ inside our existing _app_ folder.

![Templates subfolder](/images/flask_templates/templates_subfolder.png)

This folder will hold ALL our HTML files.


### Step 2: Create a new HTML file

Let us create our first HTML file called _index.html_.

![Create index file](images/flask_templates/index_file.png)

### Step 3: Update Index File

As we have done before, we can now populate our template with content.

![Update index file](images/flask_templates/update_index_file.png)

Notice that the `index.html` file contains Bootstrap. You learnt about Bootstrap in our previous lesson [Responsive Web Pages](04_bootstrap_intro.md). Make sure to refer to that lesson if you cannot recall the details. To point out, these are the Bootstrap specials used:

- Viewport Meta Tag
- Bootstrap CSS
- Bootstrap JS
- Rows and Columns


### Step 4: Update Route with Template

The next step to display our web page will now be to update the `routes.py` file to render the template _index.html_.

![Render index template](/images/flask_templates/render_index_template.png)

This is called 'rendering'. It means to 'make'.

- First, we import the function `render_template()` from `flask`
- Then, we return it by providing its name in speech marks
- We optionally include the `title` in the return statement

### Step 5: Run The Application

On the terminal, we can start our flask server.

![Start flask server](/images/flask_templates/start_flask_server.png)


### Step 6: Navigate to URL

Paste the URL http://127.0.0.1:5000 on your favourite browser to see the output.

![Template output](/images/flask_templates/templates_output.png)


Congratulations for coming this far! That is all you need to do to use templates in your Flask application.


## Smarter Templates

If you look carefully at the output of our application, you will notice that the title found on the tab head in your browser says "About Me Boostrap Demo".

![Static title](/images/flask_templates/static_title.png)

When we were defining our `index()` view function, we explictly provided a `title`. The title name was "Index Page".

![Route title](/images/flask_templates/title.png)

However, this new title is not being displayed in the final output. If we want to implement this change and make the title output more dynamic (dynamic means "it can change"), we will need to modify `index.html` file a bit more.

![Conditional title](/images/flask_templates/conditional_title.png)

So what is going on here? To begin, notice that we are using curly braces (`{}`). **Curly braces are used to allow for dynamic content**.

```html
{% if title %}
    <title> {{ title }} - Flask Templates</title>
{% else %}
    <title> Flask Templates Demo</title>
{% endif %}
```

The `if - else` conditional statement has been used to generate a title based on its availability.

- If the `index()` view function in `routes.py` has the word `title`, then Flask will replace the dynamic `{{ title }}` Jinja command with the title name. In our case, the title is "Index Page". You will see this in your browser.
![Dynamic title](/images/flask_templates/dynamic_title.png)

- If the `index()` view function in `routes.py` does not have the word `title`, then Flask will default to the second element within the `else` part of the conditional statement.
![Fallback title](/images/flask_templates/fallback_title.png)

That is how you can create more interesting and slightly more intelligent templates.


## Template Inheritance

If you have been to a website such as [spotify.com](spotify.com), you will notice that it there are some reusable elements sprinkled throughout the website.

![Spotify](/images/flask_templates/spotify.png)

If you click on any of the links in the navigation bar, the navigation bar, for instance, does not change regardless of what link or page you are on. We can say that the navigation bar is a reusable element.

Template Inheritance is the ability of other HTML files to acquire the attributes of the parent template. Below, let us see how we can implement template inheritance.

### Step 1: Create a Parent Template With Reusable Elements

Let us create a new template called `base.html` which will define all the reusable elements we may want.

![Base template](images/flask_templates/base_template_fixedd.png)

Of importance are:

- The "Home" link
- The block `content`


### Step 2: Update Index Template

Since we have moved our presentation to the `base.html` file, we need to update our original `index.html` with content specific to it.

![Child index template](/images/flask_templates/child_index_template.png)

At the top of the file, we have used the word `extends`. This keyword is used to inherit the base template within the index template. It is specially put within curly braces and percent signs.

What we have done here is to create content that we want displayed only in the index page, that is, two columns each with a paragraph with the sentence "I am a column".

### Step 3: Check the Output on the Browser

Let us see how the changes look like on the browser.

![Inheritance output](/images/flask_templates/inheritance_output.png)


### Step 4: Add Another Child Template

There isn't any observable difference in our output. To clearly see inheritance at work, we will need to add another template. For example, we can add a template called `about_me.html` as seen below.

![Add about me template](/images/flask_templates/about_me_template_file.png)


### Step 5: Add Link To New Template

With `about_me.html` file in place, we need to add a navigational link in our base template.

![Update base template](/images/flask_templates/update_base_template_fixed.png)


### Step 5: Render the About Me Page

We have added a link to the "About me" page, though it does not exist. To complete the process, we need to create a view function in `routes.py` to render the `about_me.html` file.

![Render about me page](/images/flask_templates/render_about_me_page.png)


### Step 6: View Output

Check your browser to see the new output.

![Mulitple pages](/images/flask_templates/multiple_pages.gif)


## Assignment: Push To GitHub

With the lesson project complete, you are required to push your project to GitHub.

- [ ] Update your README.md file to clearly describe your current  project
- [ ] Push the changes to GitHub