from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    # SAFE_METHODS = ['POST','PUT','DELETE']
    def has_permission(self, request, view):
        # if (request.method in self.SAFE_METHODS):
        return request.user.user_type == 'Admin'


class AdminStudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'Admin' or request.user.user_type == 'Student'
