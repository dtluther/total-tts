## More postgres madness
This time, when I ran `psql postgres` or `sudo -u postgres psql`, I was getting this error: psql: error: could not connect to server: could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket "/tmp/.s.PGSQL.5432"
To fix it this time, I followed Nelu's solution (which was a few down from the top solution on the SO post) on https://stackoverflow.com/questions/12472988/postgresql-error-could-not-connect-to-server-no-such-file-or-directory.
Solution had me update and upgrade brew, and upgrade postgres database (I think). These were the commands:
```
brew update
brew upgrade
brew postgresql-upgrade-database
```

### Setting up the database
Then, I could get into postgres with `psql postgres`.
1. I created a new database `tts` as my superuser, and then I allowed user01 access to the new database by running `grant all privileges on database tts to user01;`
2. Updated settings.py in top level project
   1. added the app `backend.apps.BackendConfig` to apps
   2. Also added `rest_framework`
3. Seeded the database with the data. Tried running `python upload_data.py`, but kept getting the following error:
   ```
   ❯ python upload_data.py                   
   Traceback (most recent call last):
     File "upload_data.py", line 2, in <module>
       from backend.models import TtsEntry
     File "/Users/lex/Documents/coding/python/hellometer-project/total_tts/backend/models.py", line 4, in <module>
       class TtsEntry(models.Model):
     File "/Users/lex/Documents/coding/python/hellometer-project/lib/python3.8/site-packages/django/db/models/base.py", line 108, in __new__
       app_config = apps.get_containing_app_config(module)
     File "/Users/lex/Documents/coding/python/hellometer-project/lib/python3.8/site-packages/django/apps/registry.py", line 253, in get_containing_app_config
       self.check_apps_ready()
     File "/Users/lex/Documents/coding/python/hellometer-project/lib/python3.8/site-packages/django/apps/registry.py", line 136, in check_apps_ready
       raise AppRegistryNotReady("Apps aren't loaded yet.")
   django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
    ```
    * Not sure what caused it, but when I copied and pasted it in the the shell (`python manage.py shell`), it worked.

to do aggregates when querying:
<!-- https://micropyramid.com/blog/aggregation-in-django-minumum-and-maximum-values-from-django-model/ -->