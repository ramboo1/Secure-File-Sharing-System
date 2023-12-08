from rest_framework import permissions

class IsOpsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.is_ops_user if hasattr(request.user, 'profile') else False

class IsFileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user