from django.contrib.auth.mixins import AccessMixin

class VendorRequiredMixin(AccessMixin):
    #Requiere que el usuario esté autenticado y NO tenga perfil_cliente (o sea VENDEDOR)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or hasattr(request.user, 'perfil_cliente'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class ClientRequiredMixin(AccessMixin):
    #Requiere que el usuario esté autenticado y TENGA perfil_cliente (o sea CLIENTE).
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not hasattr(request.user, 'perfil_cliente'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)