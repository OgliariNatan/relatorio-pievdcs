####################
# Para gerir os grupos de usuarios permitidos
########################

from django.contrib.auth.models import Group
from django.http import HttpResponse
from usuarios.models import CustomUser

def grupos_permitidos(grupos):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Verificação 1: Usuário autenticado
            if not request.user.is_authenticated:
                return HttpResponse("""<!-- code HTML -->""", status=401)
            
            # Verificação 2: Usuário está ativo no banco de dados
            try:
                usuario = CustomUser.objects.only('id', 'is_active').get(
                    id=request.user.id
                )                
                if not usuario.is_active:
                    return HttpResponse("""<!-- code HTML -->""", status=403)                    
            except CustomUser.DoesNotExist:
                return HttpResponse("""<!-- code HTML -->""", status=403)
            
            # Verificação 3: Pertence aos grupos permitidos
            if request.user.groups.filter(name__in=grupos).exists():
                return view_func(request, *args, **kwargs)            
            # Usuário ativo mas sem permissão de grupo
            return HttpResponse("""<!-- code HTML -->""", status=403) 
            
        _wrapped_view.__name__ = view_func.__name__
        return _wrapped_view
    return decorator
