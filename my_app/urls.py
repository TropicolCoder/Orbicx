from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'my_app'
urlpatterns = [
    # home views
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:category>/<slug:project>/', views.project_detail, name='project_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
