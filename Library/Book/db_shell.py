from Book.models import Book
# to run pythone fill in db shell
# exec(open(r'F:\Paythone\Django\Library\Book\db_shell.py').read())
# all data.
'''
all_data= Book.objects.all()
print(all_data)
print("-"*50)

#single data
sid=1
b2=Book.objects.get(id=sid)
print(b2)
print("-"*50)

#create

b3=Book.objects.create(name="html",author="aaa",qty=30,price=300)
print(b3.id)
print("-"*50)

#update data
sid=5
b4=Book.objects.get(id=sid)
b4.name="python"
b4.author="ert"
b4.qty=20
b4.price=600
b4.save()
print("-"*50)
#delete

b5=Book.objects.get(id=4)
b5.name="python"
b5.delete()
'''


# all_data=Book.objects.all()
# print(all_data)
#o/p==<QuerySet [<Book: wings of fire---apk sir>, <Book: python---ert>, <Book: html---aaa>, <Book: html---aaa>, <Book: html---aaa>, <Book: html---aaa>]>


# all_data=len(Book.objects.all())
# print(all_data)

# o/p==6

'''
all_data=Book.objects.all()

for book in all_data:
    print("--------Details for id number------",book.id,"----------------")
    print("Book name",book.name)
    print("Book author",book.author)
    print("Book quantity",book.qty)
    print("Book price",book.price)

--------Details for id number------ 9 ----------------
Book name html
Book author aaa
Book quantity 30
Book price 300.0
'''

#-----update
# all_data= Book.objects.all()

# for book in all_data:
#     book.qty=30
#     book.save()

#-------------delete
# all_data= Book.objects.all()

# for book in all_data:
#     book.delete()




# all_data= Book.objects.all()

# for book in all_data:
#     print(book.__dict__)



# all_data= Book.objects.all().values("id","name","qty")
# print(list(all_data))
# for book in all_data:
#     print(book)


# all_data= Book.objects.values_list()
# # print(all_data)
# for book in all_data:
#     print(book[0])



#------------Filter
# import random#--------------record display
# for i in range(1,36):
#     b=Book.objects.create(name=chr(random.randint(64,90)) *5,author="nnbb",qty=random.randint(15,85),price=random.randint(200,900))
#     b.save()

# grater than=__gt
# grater than equal=__gte
# less than=__lt
# less thanequal=__lte


# books=Book.objects.filter(id__lte=15)
# for i in books:
#     print(i.id)


# books=Book.objects.filter(id__lte=15).values("id","name") #---id name print honar
# for i in books:
#     print(i)


#---name start with j   
# built in function(double underscore use karne)
#built in function sthi __startswith
#case sensitive sathi small kiva capital sathi (i) use karnse
# books=Book.objects.filter(name__iendswith="j").values("id","name") #---id name print honar
# # books=Book.objects.filter(name__istartsswith="j").values("id","name")
# for i in books:
#     print(i)


#----ascending
# b=Book.objects.all().order_by("name")
# print(b)

#-----decending
# b=Book.objects.all().order_by("-name")
# print(b)


# b=Book.objects.all().count()
# b=Book.objects.count()
# print(b)


# b=len(Book.objects.all())#--().len()
# print(b)



# b=Book.objects.all()[0]#-----positive index

# print(b.id)


# b=Book.objects.all()[34]#-----negative index

# print(b.id)



# b=Book.objects.all()[0:5]#-----negative index

# print(b)

# l=[i for i in range(12,20)]
# b=Book.objects.filter(id__in=l)#-----12 to 20 madile data print honar

# print(b)



# l=[i for i in range(12,20)]
# b=Book.objects.all().exclude(id__in=l)#-----12 to 20 madile data print honar

# print(b)



# l=[i for i in range(12,20)]
# b=Book.objects.exclude(id__in=l)#-----12 to 20 madile data print honar

# print(b)


l=[i for i in range(12,20)]
b=Book.objects.all().filter(id__in=l)#-----12 to 20 madile data print honar

print(b)

#-------bulk   for loop peksya bulk kami velat  run honar
Book.objects.bulk_create([
Book(name="java",author="aaa",qty=30,price=300),
Book(name="physics",author="fgh",qty=34,price=300),
Book(name="chem",author="xcs",qty=56,price=300),
Book(name="math",author="cds",qty=50,price=300),
Book(name="mechanical",author="vfdd",qty=56,price=300)

])


Book.objects.filter(id__in=[41,42,43,44,45,46]).update(price=900)#----only list madile value update karnesathi