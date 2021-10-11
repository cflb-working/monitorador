import os

class ArquivoDeDados:
    
    TMP_DIR_PREFIX = '/tmp/monitorador/'
    


    def __init__(self, usuario, repo):
        self.usuario = usuario
        self.repo = repo


    def criar_diretorio_do_arquivo_de_dados(self):
        os.makedirs(self.TMP_DIR_PREFIX + self.usuario + '/')


    def criar_o_arquivo_de_dados(self):
        self.arq_dados = open(self.TMP_DIR_PREFIX + self.usuario + '/' + self.repo + '.db', 'w')
        self.arq_dados.close()

    def diretorio_existe(self):
        """
          Como posso verificar que um diretorio existe?
          /tmp/monitorador/usuario/repositorio.db
        """
        try:
            self.criar_diretorio_do_arquivo_de_dados()
            return True
        except FileExistsError as e:
            return e
     

    def arquivo_existe(self):
       try:
           self.criar_o_arquivo_de_dados()
           return True
       except IOError as e:
           return False, e 
