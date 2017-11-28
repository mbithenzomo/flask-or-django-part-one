![featured-image](https://raw.githubusercontent.com/mbithenzomo/flask-or-django-part-one/master/flask-or-django-1.jpg)

The code for Part One of my two-part article, *Flask Or Django? An In-Depth Comparison*.

Have you just gotten started with Python for the web, and are wondering which Python framework to learn or use for your next project? Then you've probably heard of [Django](https://www.djangoproject.com/), [Flask](http://flask.pocoo.org/), or both. Although there are other Python web frameworks, such as [Pyramid](https://trypyramid.com/), [web2py](http://www.web2py.com/), and [TurboGears](http://turbogears.org/), Django and Flask remain the most popular.

This series will offer an in-depth comparison of Flask and Django, looking at various factors. In Part One, we will compare their:

1. Popularity
2. Documentation and ease of getting started
3. Routing system
4. Templating system

# Installation and Set Up

To see the demos for both Flask and Django on your machine, begin by cloning this repo:

```
git clone https://github.com/andela-mnzomo/flask-bucketlist-api
```

## Flask

To set up Flask, navigate to the `flask` directory:

```
cd flask
```

Install the required packages:

```
pip install -r requirements.txt
```

And finally, run the app:

```
export FLASK_APP=app.py
flask run
* Serving Flask app "app"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Navigate to `http://127.0.0.1:5000/` to see the Flask app in your browser.

## Django

To set up Django, navigate to the `django/mysite` directory:

```
cd django/mysite
```

Install the required packages:

```
pip install -r requirements.txt
```

And finally, start the Django server:

```
cd mysite
python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
November 27, 2017 - 12:21:45
Django version 1.10.6, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Navigate to `http://127.0.0.1:8000/` to see the Django app in your browser.
