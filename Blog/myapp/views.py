from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return render(request, "myapp/index.html")

def blogs(request):
    return render(request, "myapp/blogs.html")

def blog_details(request, id):
    return render(request, "myapp/blog-details.html", {
        "id" : id
        #string içerisine alınan şekliyle gönderilir html sayfasına. Yani "a" yazsaydık, html sayfasının içerisinde {{a}} ile çağırmak gerekecekti.
    })