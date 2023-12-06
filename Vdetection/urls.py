from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('log_in', views.log_in, name='log_in'),
    path("sign_up", views.sign_up, name='sign_up'),
    path('log_out', views.log_out, name='log_out'),
    path('dashboard', views.dashboard, name='dashboard'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)