from django.shortcuts import redirect
from django.contrib import messages


class StaffUsuarioMixins(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,'No tienes los permisos para realizar esta accion.')
            return redirect('listaralumnos')
    