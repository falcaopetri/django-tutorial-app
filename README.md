# Django Tutorial

What I've done so far:
- Finished parts [1-2] of [Writing your first Django app](https://docs.djangoproject.com/en/1.10/intro/);
- Used [Heroku Django Starter Template](https://github.com/heroku/heroku-django-template/);
- Uploaded the project to Heroku (app available [here](django-tutorial-app.herokuapp.com));
	- Had some trouble to understand how to use Heroku's PostgreSQL vs local SQLite database
	- Tried to make my local PostgreSQL work, and failed;
	- Had some trouble to realize how I should create a superuser account on my Django app hosted on Heroku (finally found it at [Django Girls](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/heroku/#visit-your-application), just run `heroku run python manage.py createsuperuser`);
- Synced the Heroku app and the GitHub repo (automatic building on new GitHub commits);
- Finished part 3 of Tutorial
- Finished part 4 of Tutorial
	- Vote and Results working
	- Using Generic Views
