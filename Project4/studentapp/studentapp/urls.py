from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("to_do_list.urls")),              # homepage = to-do list
    path("blog/", include("blog.urls")),               # blog section
    path("notes/", include("upload_notes.urls")),      # upload notes section
]

# serve uploaded images in dev
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
