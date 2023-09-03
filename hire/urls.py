from django.urls import path
from .views import open_my_details,delete_data_method,update_data_method,open_Hire_me,hire_me
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
 
    path("my_details",open_my_details,name="open_my_detail"),
    path("update-my-data/<int:id>",update_data_method,name="update_data"),
    path("delete-my-data/<int:id>",delete_data_method,name="delete_data"),
    path("open_Hire_me",open_Hire_me, name="open_Hire_me"),
    path("hire_me",hire_me,name="hire_me"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)