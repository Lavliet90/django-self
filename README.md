###Famous women

(This page was made for educational purposes.)

To start the installation, clone the repository, then go to the directory
cd coolsite

Next, install the required packages
```
python3 -m pip install -r req.txt
```
And we start the server locally with the command:
```
python3 manage.py runserver
```
On the main page on the left we have a menu with a specialization of women. 
At the top right is registration and authorization. With the debug enabled mode, we have debug_toolbar. 
In the contact section, we can send some information, there is also a captcha attached.
If you are authorized. then you can add an article via "Add article".



There is also an admin panel for management:
```
http://127.0.0.1:8000/admin/
```
but before using it, you need to create an administrator with the command:
```python3 manage.py createsuperuser```
Then you will be asked to enter a nickname, email (optional), password.