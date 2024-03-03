from django.urls import path
from django.contrib.auth.views import *
from django.contrib.auth.decorators import *
from .views import *


urlpatterns = [
    
    path('register/', register, name='register'),
    path('logout_user/',logout_user,name='logout_user'),
    path('', login_user, name='login_user'),
    path('home/', home, name='home'),
    path('representative/', representative, name='representative'),
    path('activity_news/', activity_news, name='activity_news'),
    path('report_issue/', report_issue, name='report_issue'),
    path('Income_expenses/', income_expenses, name='income_expenses'),
    path('Donation_reportform/', donation_reportform, name='donation_reportform'),
    
    path('admin/login/', LoginView.as_view(), name='admin_login'),
    path('admin/logout/', LogoutView.as_view(), name='admin_logout'),
    path('admin/add_edit/add_representative/', add_representative, name='add_representative'),
    path('admin/add_edit/', edit_view, name='admin_edit'),
    path('admin/add_edit/add_income_expenses/', add_income_expenses, name='add_income_expenses'),
    path('admin/add_edit/add_villagepublic/', add_villagepublic, name='add_villagepublic'),
    path('admin/add_edit/add_activity_news/', add_activity_news, name='add_activity_news'), 

    
    path('admin/add_edit/edit_representative/<int:representative_id/', edit_representative, name='edit_representative'),
    path('admin/edit_villagepublic/<int:villagepublic_id>/', edit_villagepublic, name='edit_villagepublic'),
    path('admin/edit_activity_news/<int:activity_news_id>/', edit_activity_news, name='edit_activity_news'),
    path('edit_income_expenses/<int:income_expenses_id>/', edit_income_expenses, name='edit_income_expenses'),

    
]