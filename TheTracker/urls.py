from django.contrib import admin
from django.urls import path
from django.urls import include
from expenseTracker import views as etrack
from todo_app import views as tViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
   # path("test/", tViews.test, name="test"),
    path('', etrack.home, name='home'),
    path('todo_app/', include('todo_app.urls')),
    path('index/', etrack.index, name='index'),
    path('register/',etrack.register,name='register'),
    path('handleSignup/',etrack.handleSignup,name='handleSignup'),
    path('handlelogin/',etrack.handlelogin,name='handlelogin'),
    path('handleLogout/',etrack.handleLogout,name='handleLogout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "home/reset_password.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="home/reset_password_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ="home/password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetView.as_view(template_name ="home/password_reset_done.html"),name='password_reset_complete'),
    path('addmoney/',etrack.addmoney,name='addmoney'),
    path('addmoney_submission/',etrack.addmoney_submission,name='addmoney_submission'),
    path('charts/',etrack.charts,name='charts'),
    path('tables/',etrack.tables,name='tables'),
    path('expense_edit/<int:id>',etrack.expense_edit,name='expense_edit'),
    path('<int:id>/addmoney_update/', etrack.addmoney_update, name="addmoney_update") ,
    path('expense_delete/<int:id>',etrack.expense_delete,name='expense_delete'),
    path('profile/',etrack.profile,name = 'profile'),
    path('expense_month/',etrack.expense_month, name = 'expense_month'),
    path('stats/',etrack.stats, name = 'stats'),
    path('expense_week/',etrack.expense_week, name = 'expense_week'),
    path('weekly/',etrack.weekly, name = 'weekly'),
    path('check/',etrack.check,name="check"),
    path('search/',etrack.search,name="search"),
    path('<int:id>/profile_edit/',etrack.profile_edit,name="profile_edit"),
    path('<int:id>/profile_update/',etrack.profile_update,name="profile_update"),
    path('info/',etrack.info,name="info"),
    path('info_year/',etrack.info_year,name="info_year"),


    # path('fityfeed/', efitty.home, name="fityfeed"),
]