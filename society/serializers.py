from rest_framework import serializers

from .models import Profile, Society, SocietyMembers, SocietyComments


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = '__all__'


class SocietyMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyMembers
        fields = '__all__'


class SocietyCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyComments
        fields = '__all__'
