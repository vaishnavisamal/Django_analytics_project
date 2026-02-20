from django.urls import path
from .views import DashboardView,EventLogCreateAPIView, AnalyticsSummaryAPIView, AnalyticsButtonsAPIView

urlpatterns = [
     path('', DashboardView.as_view(), name='dashboard'),
    path('api/events/', EventLogCreateAPIView.as_view(), name='log-event'),
    path('api/analytics/summary/', AnalyticsSummaryAPIView.as_view(), name='analytics-summary'),
    path('api/analytics/buttons/', AnalyticsButtonsAPIView.as_view(), name='analytics-buttons'),
]