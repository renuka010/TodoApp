from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('notes/', views.notes, name='notes'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('complete/<int:note_id>', views.complete, name='complete')
]