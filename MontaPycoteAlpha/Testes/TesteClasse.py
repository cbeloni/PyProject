class Person(object):
    def set_name(self, name):
        if len(name) >= 2:
            self.name = name

woman = Person()
woman.set_name('Juliana')
print woman.name

class ParamPacotes(object):
	"""docstring for ClassName"""
	def set_numero_chamado(self, NumeroChamado):
		self.NumeroChamado  = NumeroChamado		

	def set_nome_script(self, NomeScript):
		self.NomeScript = NomeScript
			
	def set_diretorio(self, Diretorio):
		self.Diretorio = Diretorio


# self.sDiretorio = 'c:\\sati'
param = ParamPacotes()		
param.set_numero_chamado('12345')
param.set_nome_script('TESTE1.sql')
param.set_diretorio('c:\\SATI')
print param.Diretorio