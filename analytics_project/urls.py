from django.contrib import admin
from django.urls import path, include
from analytics.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),  # root URL
    path('api/', include('analytics.urls')),  # Optional: if you want `/api/...` too
]