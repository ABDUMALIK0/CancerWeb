from django.urls import path
from . import views
#from django.contrib.auth.views import LoginView
#from .forms import LoginForm

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_photo, name='add_photo'),
    path('signup/', views.signup, name='sign_up'),
    path('login/',views.login_page, name='log_in'),
    path('logout/',views.logout_page, name='log_out')
    #path('login/', LoginView.as_view(template_name ='blog/login.html', authentication_form = LoginForm), name='log_in'),
]