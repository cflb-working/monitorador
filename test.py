"""
Vamos tentar fazer um TDD.
Vamos criar testes antes de criar os objetos, a ideia é de fato
criar testes que falhem, para assim poder corrigi-los.

vamos tentar usar 'baby steps' ao maximo.
"""
import unittest
from utils.monitoradores import Monitorador
from utils.dados import ArquivoDeDados

class TestMonitorador(unittest.TestCase):
    """
      Se o Monitorador existe ou pode ser criado
      Se o monitor funciona para um repositorio com release
      Se o monitor funcionar para um repositorio sem release
    """

    def test_se_o_monitorador_exist(self):
        m = Monitorador('pixies', 'devinf')
        self.assertIsInstance(m, Monitorador)


    def test_se_monitorador_funciona_em_repositorios_com_release(self):
        m = Monitorador('pixies', 'devinf')
        release = m.consulta_ao_repositorio() # db-base-v1.1
        # como exemplo, vou usar o repositorio 'pixies/devinf'
        self.assertEqual(release, 'db-base-v1.1')

    def test_se_monitorador_funciona_em_repositorios_sem_release(self):
        m = Monitorador('pixies', 'bee')
        release = m.consulta_ao_repositorio()
        self.assertEqual(release, 'releases')

# -------------------------------------------------------------------------

class TestArquivoDeDado(unittest.TestCase):
    """
      Se o arquvio existe - criar
      Vai escrever no arquivo - e salvar
    """

    def test_se_o_diretorio_exist(self):
        """
           Verificar se este arquivo existe
           /tmp/monitorador/usuario/repositio.db
        """
        ar_dados = ArquivoDeDados('pixies', 'devinf')
        arquivo = ar_dados.diretorio_existe()
        if self.assertTrue(arquivo):
            return True
        
    def test_se_arquivo_existe(self):
        ar_dados = ArquivoDeDados('pixies', 'devinf')
        self.assertTrue(ar_dados.arquivo_existe())



if __name__ == '__main__':
    unittest.main()


