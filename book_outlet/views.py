from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def index(req):
    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_books = books.aggregate(Avg("rating"))
    
    return render(req, 'book_outlet/index.html', {
        'books': books,
        "totalBooks": num_books,
        "average_rating": avg_books
        })


def book_detail(req, slug):
    # try:
    #     books = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    books = get_object_or_404(Book, slug=slug)
    return render(req, 'book_outlet/book_detail.html', {
        'title': books.title,
        'author': books.author,
        'rating': books.rating,
        'isBestSeller': books.isBestSelling})
