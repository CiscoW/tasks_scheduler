from rest_framework import serializers
from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import SolarSchedule
from django_celery_beat.models import PeriodicTask


class ClockedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockedSchedule
        fields = ('id', 'clocked_time', 'enabled')


class CrontabScheduleSerializer(serializers.ModelSerializer):
    # 该字段无法直接转换，需要单独声明
    timezone = serializers.CharField(max_length=63)

    class Meta:
        model = CrontabSchedule
        fields = ('id', 'minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year', 'timezone')


class IntervalScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = ('id', 'every', 'period')


class SolarScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarSchedule
        fields = ('id', 'event', 'latitude', 'longitude')


class PeriodicTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ('id', 'name', 'task', 'interval', 'crontab', 'solar', 'clocked', 'args', 'kwargs', 'queue',
                  'exchange', 'routing_key', 'headers', 'priority', 'expires', 'one_off', 'start_time', 'enabled',
                  'last_run_at', 'total_run_count', 'date_changed', 'description')
