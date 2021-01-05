
from django.urls import path
from app.views.index import index
from app.views.expenses import create_expense,edit_expense,delete_expense
from app.views.profiles import profile_index,profile_edit,profile_delete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    #index
    path('',index,name='home' ),
    #expenses
    path('create/',create_expense,name='create expense' ),
    path('edit/<int:pk>',edit_expense,name='edit expense' ),
    path('delete/<int:pk>',delete_expense,name='delete expense' ),
    #profile
    path('profile/',profile_index,name='profile index' ),
    path('profile/edit',profile_edit,name='profile edit' ),
    path('profile/delete',profile_delete,name='profile delete' ),
  
]
urlpatterns += staticfiles_urlpatterns()