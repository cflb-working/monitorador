import requests

class Monitorador:
    """
        Verificar como vou coletar os dados
        - github.com/ <usario> / <repo> 
    """
    GITHUB_URL = 'https://github.com/'

    def __init__(self, usuario, repo):
        self.usuario = usuario
        self.repo = repo

    def consulta_ao_repositorio(self):
        release = requests.get(self.GITHUB_URL + self.usuario + '/' + self.repo + '/' + 'releases/latest').url.split('/')[-1]
        return release
