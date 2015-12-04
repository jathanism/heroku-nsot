###########
heroku-nsot
###########

Deploy NSoT to Heroku with ease.

Instructions
============

These instructions assume that you know your way around Heroku and already have
the heroku-toolbelt installed.

You'll need a fresh a Heroku app with the Heroku Postgres add-on enabled.

1. Clone this repo and change to the directory::

   $ git clone https://github.com/jathanism/heroku-nsot.git
   $ cd heroku-nsot
  
2. Add the ``heroku`` Git remote::

   $ git remote add heroku https://git.heroku.com/yourappname.git

3. Push this repo to Heroku::

   $ git push heroku master

4. After it's deployed, create a superuser::

   $ heroku run 'nsot-server --config=settings.py createsuperuser'

5. Fire up your web browser and use the API interface to login with your
   superuser::

   https://yourappname.herokuapp.com/api/api-auth/login/'

End.

To Do
=====

+ Get rid of hard-coded ``SECRET_KEY``.
+ Account for upgrading NSoT.
