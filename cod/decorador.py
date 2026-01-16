# Outras importações
""" Configuração de decoradores para debug """
import os

var_debug = os.getenv('DEBUG', False) #Carrega apenas a variável de debug

if var_debug == 'True':
    from MAIN.decoradores.calcula_tempo import calcula_tempo, calcula_tempo_fun
    checked_debug_decorador = calcula_tempo
    checked_debug_decorador_fun = calcula_tempo_fun
else:
    checked_debug_decorador = lambda x: x
    checked_debug_decorador_fun = lambda x: x

""" Fim da configuração de decoradores para debug """


# No inicio de cada visualização
@checked_debug_decorador
@login_required(login_url=reverse_lazy('login'))
@grupos_permitidos(['instituicao_autorizadas' , 'outras_instituicoes_autorizadas'])
def funcao(request):
    pass

# No inicio de cada função
@checked_debug_decorador_fun
@login_required(login_url=reverse_lazy('login'))
@grupos_permitidos(['instituicao_autorizadas', 'outras_instituicoes_autorizadas'])
def funcao_qualquer(parametros):
    # code
    # Para exibir impressões no terminal
    if var_debug == 'True':
        print("Impressão de depuração")
    # code
