from django.shortcuts import render_to_response
from book.models import Book

def latest_book(request):
    book_list = Book.objects.order_by('pub_date')[:10]
    return render_to_response('latest_book.html',{'book_list':book_list})
