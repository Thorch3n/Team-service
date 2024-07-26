from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['members'] = instance.members.split(',')
        return ret

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        ret['members'] = ','.join(data['members'])
        return ret