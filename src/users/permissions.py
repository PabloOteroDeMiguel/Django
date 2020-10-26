from rest_framework.permissions import BasePermission




class UsersPermission(BasePermission):

    # Listado de usuarios: solo administrados (por tanto autenticado)
    # Creacion de usuario: libre
    # Detalle de usuario: admin y  el propio usuario
    # Actualizacion de usuario: admin y el propio usuario
    # Borrado de usuario: admin y el propio usuario

    def has_permission(self, request, view):
        """
        Define si el usuario puede ejecutar una accion (GET, POST, PUT, o DELETE) sobre la vista "view"
        """
        from users.api import UserDetailApi

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, UserDetailApi):
            return True

        return request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE")

    def has_object_permission(self, request, view, obj):
        """
        El usuario autenticado solo puede trabajar con el usuario solicitado si es él mismo o el admin"
        """
        return request.user == obj or request.user.is_superuser
