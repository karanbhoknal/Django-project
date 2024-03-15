

# Project Name : 
# Python Knowledge Share site
				


# INTRODUCTION OF PYTHON DJANGO PROJECT 

Django is especially helpful for database driven websites.
Django is a Python framework that makes it easier to create web sites using Python
Django is a Python-based web framework that allows you to quickly 
create web applications without all of the installation or dependency 
problems that you normally will find with other frameworks. 
When you’re building a website, you always need a similar set of
components: a way to handle user authentication(signing up, signing in, 
signing out),a management panel for your website,forms,a way to upload 
files,etc.

# Python Django

Django is used in many popular sites like Disqus, Instagram, Knight 
Foundation, MacArthur Foundation, Mozilla,National Geographic, etc. 
There are more than 5k online sites based on the Django framework.
Source ) Sites like Hot Frameworks assess the popularity of a framework 
by counting the number of GitHub projects and StackOverflow questions for
each platform, here Django is in 6th position.Web frameworks often refer
to themselves as “opinionated” or “un-opinionated” based on opinions about 
the right way to handle any particular task.Django is somewhat opinionated, 
hence delivering thein both worlds( opinionated & un-opinionated ).



It’s very easy to switch databases in the Django framework.
It has a built-in admin interface which makes it easy to work with it.
Django is a fully functional framework that requires nothing else.
It has thousands of additional packages available.
It is very scalable.

# Features of Django

The versatility of Django: Django can build almost any type of website. 
It can also work with any client-side framework and can deliver content 
in any format such as HTML,JSON, XML, etc. Some sites which can be built 
using Django are wikis, social networks, new sites etc.


# Security:
Since the Django framework is made for making web development easy,
it has been engineered in such a way that it automatically do the right things
to protect the website. 
For example, In the Django framework instead of putting a password in cookies, 
the hashed password is stored in it so that 
it can’t be fetched easily by hackers.



# Scalability:
Django web nodes have no stored state, they scale horizontally – 
just fire up more of them when you need them. Being able to do this is the 
essence of good scalability. Instagram and Disqus are two Django based products
that have millions of active users,this is taken as an example of the scalabilit
of Django.

# Portability:
All the codes of the Django framework are written in Python, which 
runs on many platforms.Which leads to run Django too in many platforms such as
Linux, Windows and Mac OS.

# Django Architecture

Django is based on MVT (Model-View-Template) architecture which has the 
following three parts –

# Model:
The model is going to act as the interface of your data. It is 
responsible for maintaining data. It is the logical data structure behind 
the entire application and is represented by a database
generally relational databases such as MySql, Postgres).

# View: 
The View is the user interface that you see in your browser when 
you render a website. It is represented by HTML/CSS/Javascript and Jinja files.

# Template:
A template consists of static parts of the desired HTML output as well as some special 
syntax describing how dynamic content will be inserted. To check more, visit – Django Templates
Django Architecture



--------------------------------------------------------------------
 # Installation and Setup of Django
--------------------------------------------------------------------

1. Install python3 if not installed in your system 
 Try to download the latest version of python it’s python 3.11.0 this time.

Note: Installation of Django in Linux and Mac is similar, here I am showing it in windows for 
Linux and mac just open terminal in place
of command prompt and go through the following commands.

--------------------------------------------------------------------
# Install pip: Open command prompt and enter following command-
--------------------------------------------------------------------------------------
   python -m pip install -U pip

--------------------------------------------------------------------
3.Setting up the Virtual Environment
--------------------------------------------------------------------
Create virtual environment in django: We should first go the directory
where we want to createthe virtual environment then we type the following 
command to create virtual environment in django

Command=> python -m venv env_site


4. Activate the virtual environment => Run the activation script located 
in the bin directory within the virtual environment folder

For Windows:
env_site\Scripts\activate.bat

For MacOs/Linux:
source env_site/bin/activate
--------------------------------------------------------------------
# .Install Django: Install django by giving following command
--------------------------------------------------------------------
Command => pip install django


--------------------------------------------------------------------
#. Start a project by following command
--------------------------------------------------------------------
django-admin startproject django_proj


----------------------------------
#.Change directory to django_proj
----------------------------------
cd django_proj


--------------------------------------------------------------------
#.Start the server- Start the server by typing following command in cmd-
--------------------------------------------------------------------
python manage.py runserver

--------------------------------------------------------------------
# On vs code hit this command [folder name =Django project]
--------------------------------------------------------------------

python manage.py startapp projectApp



