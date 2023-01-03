from typing import Any
from rest_framework import permissions
from rest_framework.views import APIView

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Any, view: APIView) -> bool:
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_staff
        )
