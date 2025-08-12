from rest_framework import permissions


class GlobalAllowAny(permissions.BasePermission):

    def has_permission(self, request, view):
        model_allow = self.__get_model_allow(
            method=request.method,
            view=view,
        )

        if not model_allow:
            return False
        return request.user.has_perm(model_allow)

    def __get_model_allow(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_action = {
            'GET': 'view',
            'HEAD': 'view',
            'OPTIONS': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete'
        }
        return method_action.get(method, '')
    

