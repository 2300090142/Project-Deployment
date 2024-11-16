from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reg/', views.reg, name='sign up'),
    path('settings/', views.settings, name='Settings'),
    path('he/', views.he, name='Help'),
    path('editor/', views.editor, name='Terminal'),
    path('about/', views.about, name='About'),
    path('notes/', views.notes, name='Notes'),
    path('execute/', views.execute_code, name='execute_code'),  # Add your execute code view
    path('run_java/', views.run_java_code, name='run_java_code'),
    path('success/', views.profile, name='success'),

]



