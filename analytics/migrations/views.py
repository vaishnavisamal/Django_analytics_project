from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from .models import EventLog
from .serializers import EventLogSerializer
from django.views.generic import TemplateView

# POST /api/events/ → log an event
class EventLogCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EventLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# GET /api/analytics/summary/ → total logins, clicks, events
class AnalyticsSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_events = EventLog.objects.count()
        total_logins = EventLog.objects.filter(event_type='login').count()
        total_button_clicks = EventLog.objects.filter(event_type='button_click').count()
        return Response({
            'total_events': total_events,
            'total_logins': total_logins,
            'total_button_clicks': total_button_clicks,
        })

# GET /api/analytics/buttons/ → clicks per button
class AnalyticsButtonsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = EventLog.objects.filter(event_type='button_click') \
            .values('button_name') \
            .annotate(count=Count('id'))
        return Response(data)

class DashboardView(TemplateView):
    template_name = "dashboard.html"