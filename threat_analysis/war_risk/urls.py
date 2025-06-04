from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('signup',views.signup),
    path('login',views.login_page),
    path('login1',views.login1),
    path('signuplogic',views.signuplogic),
    path('userlogin',views.userlogin),
    path('upload_files',views.upload_files),
    path('upload',views.upload),
    path('tracking_dashboard',views.tracking_dashboard),
    path('home',views.home),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)