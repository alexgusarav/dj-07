from rest_framework.permissions import BasePermission
from rest_framework import serializers


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.method == "DELETE" and obj.creator != request.user:
            raise serializers.ValidationError('Можно удалять только свои объявления')
        return request.user == obj.user