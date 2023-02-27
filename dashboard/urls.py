from django.urls import path
from dashboard import views

urlpatterns = [
    path('registerWorker/',views.registerWorker,name='registerWorker'),
    path('registerManager/',views.registerManager,name='registerManager'),
    path('',views.userLogin,name='userLogin'),
]
