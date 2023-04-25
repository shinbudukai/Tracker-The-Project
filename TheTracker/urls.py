from django.contrib import admin
from django.urls import path
from django.urls import include
from expenseTracker import views as eViews
from Fityfeed import views as fViews
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    #expenseTracker views
    path('admin/', admin.site.urls),
    path('', include('expenseTracker.urls')),
    path('Fityfeed/', include('Fityfeed.urls')),
    path('login/', eViews.home,name='login'),
    path('logout/',eViews.handleLogout,name='logout'),

    # #fityfeed views (this for test)
    # path('Fityfeed/', include('Fityfeed.urls')),
    # path('test/', fViews.fooditem, name='test'),
]