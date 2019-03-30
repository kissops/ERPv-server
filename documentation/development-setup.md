# Development Setup

1. Create a `.env` file with the required SECRETKEY setting, and optional [DATABASE_URL](https://github.com/kennethreitz/dj-database-url#url-schema) setting (Note: only tested with SQLite and PostgreSQL).

    ```
    DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/NAME"
    SECRETKEY="testing"
    ```

2. Install requirements with [pipenv](https://pipenv.readthedocs.io/en/latest/).

    ```sh
    pipenv install --dev
    ```

3. Generate staticfiles.

    ```sh
    pipenv run python manage.py collectstatic
    ```

4. Migrate the database.

    ```sh
    pipenv run python manage.py migrate
    ```

5. Create a superuser.

    ```sh
    pipenv run python manage.py createsuperuser
    ```
6. Run the development server.

    ```sh
    pipenv run python manage.py runserver
    ```

7. Login to the application on [http://127.0.0.1/admin/](http://127.0.0.1/admin/) with the superuser you just created.
