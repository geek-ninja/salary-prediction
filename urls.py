"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from pages.views import home_view,contact_view
from products.views import product_detail_view,product_create_view,render_initial_data,dynamic_lookup_view,product_delete_view,product_list_view
from upload.views import upload_view
from djangoMl.views import home_view,result_view
from simpleLinerRegression.views import home_view,result_view
from graph.views import main_view
from heartattack.views import input_view,res_view
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slr/',home_view,name = 'slr'),
    path('slr_result/',result_view,name = 'slr_result'),
    path('graph/',main_view,name = 'graph'),         
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
