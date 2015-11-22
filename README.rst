======================
Real Madrid prediction
======================

RMPrediction is a simple Django app to predict any Real Madrid Liga FP match using Bigml API.


Quick start
-----------

1. Add "rmpredictions" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'rmprediction',
    )

2. Include the rmpredictions URLconf in your project urls.py like this::

    url(r'^rmprediction/', include('rmprediction.urls')),

3. Run `python manage.py migrate` to create the rmpredictions models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to checkout your predictions. It'll be empty initially.

5. Visit http://127.0.0.1:8000/ to predict your first match.
