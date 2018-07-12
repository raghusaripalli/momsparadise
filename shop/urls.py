from django.conf.urls import url
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thanks/', views.thank_you, name="thank_you"),
    path('shop/', views.product_list, name='product_list'),
    path('shop/<slug:category_slug>', views.product_list, name='product_list'),
    path('shop/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]
