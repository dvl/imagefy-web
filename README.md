# Imagefy

This project is pre-configured with some facilities for a quick project start using
Django.

## Instalation:

### With Docker

    $ make install
    $ make up

### ...and without

    $ cp .env-example .env
    ** now create your database and configure it on `.env` file. **
    $ python manage.py migrate
    $ python manage.py runserver
    
If you want to use `bower` install it via `npm` (install node.js first) and then:

    $ bower install
    
And stop copying and paste third-party libraries direct into your project. :)

