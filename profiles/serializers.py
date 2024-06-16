from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'owner', 'created_at', 'updated_at', 'first_name',
            'last_name', 'phone_number', 'email',
            'date_of_birth', 'image', 'is_owner'
        ]
