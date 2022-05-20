from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import CategoryListView, PostView

router = DefaultRouter()
router.register('posts', PostView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api/categories', CategoryListView.as_view()),
    path('v1/api/', include(router.urls)),
]
