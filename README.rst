###########
heroku-nsot
###########

Deploy NSoT to Heroku with ease.

Deploying
=========

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

5. Generate a ``SECRET_KEY`` to make your install more secure::

   $ heroku config:set SECRET_KEY=`openssl rand -base64 32`

6. Fire up your web browser and use the API interface to login with your
   superuser::

   https://yourappname.herokuapp.com/api/api-auth/login/'

End.

Upgrading
=========

So you want to update NSoT to the latest version on Heroku? No problem:

1. Install the `heroku-repo <https://github.com/heroku/heroku-repo.git>`_ plugin::

   $ heroku plugins:install https://github.com/heroku/heroku-repo.git

2. Reset your repo state and do a fresh push::

   $ heroku repo:reset --app=yourappname
   $ git push heroku master

3. Restart your dyno::
   
   $ heroku ps:scale web=1

To Do
=====

+ Nothing at this time.
