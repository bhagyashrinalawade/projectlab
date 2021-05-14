from django.shortcuts import render,redirect
from django.http import HttpResponse
from Book.models import Book

# Create your views here.
def homepage(request):  # view - function based View(FBV)   # request -- http request   # user defined func
    # all_books = Book.objects.all().filter(is_deleteddata1='N')
    all_books=Book.active_objects.all()
    # print(all_books)
    return render(request, template_name='home.html', context={"books": all_books})


def save_book(request):
    # print("In Save Book")
    print(request.POST) # <WSGIRequest: POST '/save-book/'>

    b_name = request.POST.get("name")
    b_author = request.POST.get("auth")
    b_price = request.POST.get("price")
    b_qty = request.POST.get("qty")
    b_pub = request.POST.get("pub")

    if b_pub=='on':
        flag=True
    else:
        flag=False
    if request.POST.get("id"):
        # try:
        book_obj=Book.objects.get(id=request.POST.get("id"))
        
        book_obj.name=b_name
        book_obj.author=b_author
        book_obj.price=b_price
        book_obj.qty=b_qty
       
        book_obj.is_publishied=flag
        book_obj.save()
        return redirect('welcome')

    else:
        # b_name = request.POST.get("name")
        # b_author = request.POST.get("auth")
        # b_price = request.POST.get("price")
        # b_qty = request.POST.get("qty")
        # b_pub = request.POST.get("pub")   # 'pub': 'on'     -- None
      

        # if b_pub =='on':
        #     flag=True
        # else:
        #     flag=False
        b=Book(name=b_name,author=b_author,qty=b_qty,price=b_price,is_publishied=flag)
        b.save()
        return redirect('welcome')


def edit_book(request,id):
    try:
        book_obj=Book.objects.get(id=id)
        #
    except Book.DoesNotExist:
        # 
        msg=f"no book found for id:{id}"
        return HttpResponse(msg)
    # book_obj=Book.objects.get(id=id)
    # all_books = Book.objects.all().filter(is_deleteddata1='N')
    # all_books=Book.Inactive_objects.all()
    # all_books=Book.active_objects.all()
    all_books=Book.objects.all()
    return render(request, template_name='home.html', context={"book":book_obj,"books": all_books})
    # return redirect('welcome')

def delete_book(request,pk):
    book_obj=Book.objects.get(id=pk)
    # book_obj.delete()
    book_obj.is_deleteddata1='Y'
    book_obj.save()
    return redirect('welcome')

def hard_delete_book(request,pk):
    book_obj=Book.objects.get(id=pk)
    book_obj.delete()
    
    return redirect('welcome')

def restore_book(request,id):
    book_obj=Book.objects.get(id=id)
    book_obj.is_deleteddata1='N'
    book_obj.save()
    return redirect('welcome')

def show_deleted_data(request):
    all_deleted_books=Book.Inactive_objects.all()
    return render(request,template_name='home.html', context={"books": all_deleted_books})