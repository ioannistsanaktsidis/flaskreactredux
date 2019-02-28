Prerequisites
=============

* Node>=8.0.0

* Docker(in case you want to use Postgresql)


Installation
============

Flask + Postgresql
==================

To use this boilerplate application you need to do the following steps.

Firt clone the repository

```bash
    $ git clone https://github.com/ioannistsanaktsidis/flaskreactredux.git
```

I personally run the application in a Python virtual environment, but it is not necessary.

```bash
    $ mkvirtualenv <name-for-your-virtual-env>
```

If you want to use Postgresql as a database

```bash
    docker-compose up
```

In order to initialize the database you can do

```bash
    $ flask db create
```

To drop the database you can do 

```bash
    $ flask db drop
```

Finally 

```bash
    $ export TESTAPP_SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://testapp:testapp@localhost:5432/testapp
 
    $ export FLASK_APP=testapp/app.py

    $ export FLASK_ENV=development

    $ cd flaskreactredux/

    $ pip install -e.['all']

    $ flask run --reload
    
```

React+Redux+Grommet
===================

```bash
    $ cd test-ui/

    $ npm install

    $ npm start
```

And you are ready to go [http://localhost:3000](http://localhost:3000)


Happy hacking :)


