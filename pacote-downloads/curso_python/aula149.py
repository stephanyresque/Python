# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Outra nota')
    raise exception_

try:
    levantar()
except (MeuError, ZeroDivisionError) as erro:
    print(erro.__class__.__name__)
    print(erro)
    exception_ = OutroError('vou lançar dnv')
    exception_.add_note('olha eu aqui dnv')
    exception_.__notes__ += erro.__notes__.copy()
    raise exception_ from erro



