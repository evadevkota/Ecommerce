from django.urls import path
from .views import open_men_collection,open_women_collection
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 
  
    path("women_collection",open_women_collection,name="open_women_collection"),
    path("men_collection",open_men_collection,name="open_men_collection"),
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)