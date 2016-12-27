#########################
Setting Up a Project
#########################
* Generally, write a spec, saying what the purpose of the app is
	as well as keeping you on track.
*Creating a Virtual Environment
	--This isolates django from other python packages.
	--Create a directory with name of project
	$ python -m venv <name_of_environment>
*Activate the Virtual Environment
	$source <env>/bin/activate
	--On Windows:
	$ <env>\Scripts\activate
	-- Stop with simple 'deactivate'
*Installing Django
	$ pip install Django
*Creating a project in Django
	$ django-admin.py startproject <singularProjectName> .
	--Singular meaning overarching theme name, as in pizzeria or blog or
		games.
	-- the '.' is very important and keeps the directories cleaner
*Creating the Database
	--Change the settings.py in order to change the driver.  Google is our
	friend here in finding out different configurations for different DBs
	$ python manage.py migrate
	--run this any time you want to bring over changes from the DB
* Viewing the project/ Running the server
	$ python manage.py runserver
#########################
Starting an App
#########################
--Each project has a group of individual apps that work together to make the
project work as a whole (one for a log, one for users, etc.)
	$ source <env>/bin/activate
	$ python manage.py startapp <pluralAppName>
	--Plural as in a Pizzeria project where you make pizzas, and the model
	is called pizza OR a learning log project with learning Logs app and an
	Topic model.
*Defining Models
	----------------------models.py-----------------------
	from django.db import models

	class Topic(models.Model):
	"""A topic the user i slearning about"""
	text = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text
    ---------------------models.py-----------------------
    --go to docs.djangoproject.com/en/1.8/ref/models/fields to learn more about
    fields
    test

