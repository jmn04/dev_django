# Note-taking application (+image posting function) development by Django

To run it, enter the following command under the django project folder first.<br>
*If this is not done in the current directory where manage.py exists, an error will occur.<br>
$ python manage.py migrate<br>
$ python manage.py makemigrations<br>
<br>
*This is only for those who have not created a super user.<br>
$ python manage.py createsuperuser<br>

When you submit a post with an image attached, an images folder is automatically created and the posted image is saved in it.
If you do not need blog.html and flatpages.html in the templates folder, you can delete them.
In that case, please delete the description about (blog) and (flatpages) in urlpatterns in myapp/urls.py.
