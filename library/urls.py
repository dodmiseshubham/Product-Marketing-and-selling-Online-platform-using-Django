from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^imarts/', include('imarts.urls')),
    url(r'^imartl/', include('imartl.urls')),
    url(r'^$', include('imarts.urls')),
=======
    url(r'^student/', include('student.urls')),
    url(r'^librarian/', include('librarian.urls')),
    url(r'^$', include('student.urls')),
>>>>>>> 7bf91ad4dd01dd7c7de88bf7ce9eda85ce038dd6
]
