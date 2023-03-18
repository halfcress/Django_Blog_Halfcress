"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')) #Burası önemli. Projeye myapp i tanıttıktan sonra, myapp url lerinin tamamını burada include ettiğim için, artık direk myapp url içerisindeki index, root index e karşılık geliyor.
    #eğer path('myapp/',include('myapp.urls')) şeklinde include etseydim root a değil, myapp url leri myapp/index şeklinde çağrılacaktı.
    #böylece bütün appleri birbirinden ilerleyen zamanlarda ayrıştırabilirim.
]
