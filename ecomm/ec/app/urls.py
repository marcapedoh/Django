from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import base_view,home_view,CategoryView,about_view,ProductDetail,CustomerRegistrationView, ProfileView,address,UpdateAddress
from django.contrib.auth import views as auth_view
from app.forms import LoginForm




urlpatterns = [
    path("base/",base_view),
    path("home/",home_view,name='home'),
    path("category/<slug:val>",CategoryView.as_view(),name='category'),
    path("about/",about_view, name='about'),
    path("product_detail/<int:pk>",ProductDetail.as_view(),name='proddetail'),
    path("registration/",CustomerRegistrationView.as_view(),name='registration'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('address/',address, name='adresse'),
    path('update/',UpdateAddress.as_view(), name='update'),
    path("login/",auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)