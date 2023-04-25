from django.contrib import admin
from django.urls import path
from django.urls import include
from expenseTracker import views as eViews
from Fityfeed import views as fViews
from django.contrib.auth import views as auth_views
 
"""TheTracker URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    #expenseTracker views
    path('admin/', admin.site.urls),
    path('', include('expenseTracker.urls')),
    path('Fityfeed/', include('Fityfeed.urls')),
    path('todo_app/', include('todo_app.urls')),
    path('login/', eViews.home,name='login'),
    path('logout/',eViews.handleLogout,name='logout'),

    # #fityfeed views (this for test)
    # path('Fityfeed/', include('Fityfeed.urls')),
    # path('test/', fViews.fooditem, name='test'),
]