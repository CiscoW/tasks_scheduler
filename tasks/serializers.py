from rest_framework import serializers
from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import SolarSchedule
from django_celery_beat.models import PeriodicTask
from rest_framework.validators import UniqueTogetherValidator


class ClockedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockedSchedule
        fields = ('id', 'clocked_time', 'enabled')

        validators = [
            UniqueTogetherValidator(
                queryset=ClockedSchedule.objects.all(),
                fields=('clocked_time',),
                message="已存在，无需重复新增"
            )
        ]


class CrontabScheduleSerializer(serializers.ModelSerializer):
    # 该字段无法直接转换，需要单独声明
    timezone = serializers.CharField(max_length=63)

    class Meta:
        model = CrontabSchedule
        fields = ('id', 'minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year', 'timezone')

        validators = [
            UniqueTogetherValidator(
                queryset=CrontabSchedule.objects.all(),
                fields=('minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year', 'timezone'),
                message="已存在，无需重复新增"
            )
        ]


class IntervalScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = ('id', 'every', 'period')

        validators = [
            UniqueTogetherValidator(
                queryset=IntervalSchedule.objects.all(),
                fields=('every', 'period',),
                message="已存在，无需重复新增"
            )
        ]


class SolarScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarSchedule
        fields = ('id', 'event', 'latitude', 'longitude')

        validators = [
            UniqueTogetherValidator(
                queryset=SolarSchedule.objects.all(),
                fields=('event', 'latitude', 'longitude'),
                message="已存在，无需重复新增"
            )
        ]


class PeriodicTaskSerializer(serializers.ModelSerializer):
    interval = IntervalScheduleSerializer(allow_null=True)
    crontab = CrontabScheduleSerializer(allow_null=True)
    solar = SolarScheduleSerializer(allow_null=True)
    clocked = ClockedScheduleSerializer(allow_null=True)

    class Meta:
        model = PeriodicTask
        fields = ('id', 'name', 'task', 'interval', 'crontab', 'solar', 'clocked', 'args', 'kwargs', 'queue',
                  'exchange', 'routing_key', 'headers', 'priority', 'expires', 'one_off', 'start_time', 'enabled',
                  'last_run_at', 'total_run_count', 'date_changed', 'description')

    def create(self, validated_data):
        validated_data, relation_data = self.pop_data(validated_data)

        periodic_task = PeriodicTask.objects.create(**validated_data, **relation_data)
        return periodic_task

    def update(self, instance, validated_data):
        validated_data, relation_data = self.pop_data(validated_data)
        for attr, value in dict(validated_data, **relation_data).items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    @staticmethod
    def pop_data(validated_data):
        interval_data = validated_data.pop('interval')
        crontab_data = validated_data.pop('crontab')
        solar_data = validated_data.pop('solar')
        clocked_data = validated_data.pop('clocked')
        if interval_data:
            interval_schedule = IntervalSchedule.objects.get(**interval_data)
        else:
            interval_schedule = None

        if crontab_data:
            crontab_schedule = CrontabSchedule.objects.get(**crontab_data)
        else:
            crontab_schedule = None

        if solar_data:
            solar_schedule = SolarSchedule.objects.get(**solar_data)
        else:
            solar_schedule = None

        if clocked_data:
            clocked_schedule = ClockedSchedule.objects.get(**clocked_data)
        else:
            clocked_schedule = None

        return validated_data, {"interval": interval_schedule, "crontab": crontab_schedule, "solar": solar_schedule,
                                "clocked": clocked_schedule}
