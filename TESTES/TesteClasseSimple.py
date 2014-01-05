class ParamPacotes(object):
	def __init__(self,numero_chamado,nome_script,diretorio):
		self._numero_chamado = numero_chamado
		self._nome_script = nome_script
		self._diretorio = diretorio

class CorpoPacote(ParamPacotes):
	def __init__(self,numero_chamado,nome_script,diretorio):
		self._numero_chamado = numero_chamado
		self._nome_script = nome_script
		self._diretorio = diretorio

	sScripts = '''PROMPT --**************************** [ APLICANDO ''' + _numero_chamado + '''] *********************--; '''	

pp = ParamPacotes('1234323','script','c:\\sati')
#cp = CorpoPacote('1234323','script','c:\\sati')

print pp._numero_chamado