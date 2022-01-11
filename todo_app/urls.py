
from django.contrib import admin
from django.urls import path, include
from main_app.views import TaskView, UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TaskView.as_view({
        'get':'list',
        'post':'create'
    })),
    path('user/', UserView.as_view({
        'get':'list',
        
    }))
]
