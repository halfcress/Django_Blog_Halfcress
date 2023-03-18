
from django.urls import path
from . import views


urlpatterns = [

    path("", views.index),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blogs/<int:id>", views.blog_details), #blog details başlı başına bir url değil, sadece blogs url in sonuna id eklenirse çağrılabilen bir url konumunda şuan. Kafa karıştırmasın.

]
