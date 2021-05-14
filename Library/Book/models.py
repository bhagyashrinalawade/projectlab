from django.db import models

# Create your models here.
class BookActiveManager(models.Manager):
    def get_queryset(self):
        return super(BookActiveManager,self).get_queryset().filter(is_deleteddata1='N')

class BookInActiveManager(models.Manager):
    def get_queryset(self):
        return super(BookInActiveManager,self).get_queryset().filter(is_deleteddata1='Y')

class Book(models.Model):

    #id=== by default -crate--
    name= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    qty=models.IntegerField()
    price=models.FloatField()
    is_publishied=models.BooleanField(default=False) #n---true false sathi is
    # is_deleted =models.CharField(max_length=1,default="N")
    is_deleteddata1 =models.CharField(max_length=1,default="N")
    active_objects=BookActiveManager()
    Inactive_objects=BookInActiveManager()#---show deleted data
    objects= models.Manager()

    def __str__(self):
        return f"{self.id}----{self.name}---{self.author}"

    class Meta:#data name rename karnesathi
        db_table="bookinfo"




        '''
        (denv) F:\Paythone\Django\Library>python manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver



(denv) F:\Paythone\Django\Library>python manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from Book.models import Book
>>> Book.objects.all()
<QuerySet [<Book: wings of fire---apk sir>, <Book: cpp---sdfsdf>]>





>>> b2=Book.objects.get(id=1)#---
>>> b2
<Book: wings of fire---apk sir>
>>> type(b2)
<class 'Book.models.Book'>
#----create
>>> b2=Book.objects.create(name='xyz',author='lmn',qty=12,price=320)

>>> b2
<Book: xyz---lmn>

#---create
>>> Book.objects.create(name='sdfsd',author='bnm',qty=12,price=520)
<Book: sdfsd---bnm>
#------update
>>> b5=Book.objects.get(id=1)  
>>> b5
<Book: wings of fire---apk sir>
>>> b5.qty=20
>>> b5.save()
#---------delete
>>> b6=Book.objects.get(id=3)  
>>> b6
<Book: cpp---sdfsdf>
>>> b6.delete()
(1, {'Book.Book': 1})
>>> 
'''