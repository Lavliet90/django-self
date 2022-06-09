### Famous women
*(This page was made for educational purposes.)*

  To start the installation, clone the repository, then go to the directory
```cd coolsite```

  Next, install the required packages:
```
python3 -m pip install -r req.txt

```

  Create new migrations
```
python3 manage.py makemigrations
```


  Now apply the migrations
```
python3 manage.py migrate
```

  And we start the server locally with the command:
```
python3 manage.py runserver
```
![This is an image main page](https://sun6.userapi.com/sun6-21/s/v1/ig2/eJTzvBmfEqngK2XF0BeZbshBqUrPq2PzcwdqZgBD6rmazgpooYpcKG2YEh8U15yK2FbCou4R8TiQUyF9hDKGHufP.jpg?size=1278x653&quality=96&type=album)
  On the main page on the left we have a menu with a specialization of women. 
At the top right is registration and authorization. With the debug enabled mode, we have ***debug toolbar***. 
In the contact section, we can send some information, there is also a captcha attached.
If you are authorized. then you can add an article via ***"Add article"***.

### There is also an admin panel for management:

#### [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

![image admin page](https://sun9-west.userapi.com/sun9-46/s/v1/ig2/6xMQmUWnlQhhhukGnUxuuDUOWgZKX3wY94z_-yxnx6EA5PFtz8BnRdQW5a6DtL9qvv2DA4eX0A-0ExAB-dijIf4X.jpg?size=1276x654&quality=96&type=album)

but before using it, you need to create an administrator with the command:
```
python3 manage.py createsuperuser
```
Then you will be asked to enter:
- nickname
- email (optional) 
- password
