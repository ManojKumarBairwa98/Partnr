from django.urls import path, include
from . import views

urlpatterns = [
    path('addProduct', views.addProduct, name = 'addproduct' ),
    path('modifyProduct', views.addProduct, name = 'addproduct' ),
    path('deleteProduct', views.addProduct, name = 'addproduct'  ),
    path('getAllProduct',views.getAllProduct, name = 'getAllProduct' )
]
