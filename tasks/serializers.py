from rest_framework import serializers
from django_celery_beat.models import ClockedSchedule


class ClockedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockedSchedule
        fields = ('clocked_time', 'enabled')
