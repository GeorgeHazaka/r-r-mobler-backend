from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to create, update, or delete a product.
    """

    def has_permission(self, request, view):
        # Allow read-only access to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow write access to admin users
        return request.user and request.user.is_staff
