
from django.shortcuts import render

# Task 2: Helper function to get list of books
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

# Task 1 & Task 2: View to display form and handle form submission
def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        filtered_books = [book for book in books if
                          (isTitle and keyword in book['title'].lower()) or
                          (isAuthor and keyword in book['author'].lower())]
        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})
    return render(request, 'bookmodule/search.html')
