from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('dashboard/',include('dashboard.urls')),
    path('',views.userLogin,name='userLogin'),
    path('admin/', admin.site.urls),
    path('logout/',views.userLogout,name='logout'),
    path('workerDash/',views.workerDash,name='workerDash'),
    path('managerDash/',views.managerDash,name='managerDash'),
   
]
