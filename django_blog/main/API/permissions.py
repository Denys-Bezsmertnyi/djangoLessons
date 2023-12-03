from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.author == request.user

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user == view.get_object().author

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsProfileOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.pk
