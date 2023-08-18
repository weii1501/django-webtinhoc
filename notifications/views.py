from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_noti(request):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.filter(recipient=user).order_by('-created_at')
        return Response({
            'ok': True,
            'data': NotificationSerializer(notifications, many=True).data
        }, status=200)
    else:
        return Response({'error': 'User is not authenticated!'}, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def put_read(request, id):
    user=request.user
    if user.is_authenticated:
        notification = Notification.objects.filter(id=id).first()
        notification.is_read = True
        notification.save()
        return Response({
            'ok': True
        }, status=200)
    else:
        return Response({'error': 'User is not authenticated!'}, status=400)