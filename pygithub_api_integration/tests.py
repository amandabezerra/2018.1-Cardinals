from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class RepoInfoTests(TestCase):

    def test_get_repo_name(self):

        organization = 'fga-gpp-mds'
        repo_name = '2018.1-Cardinals'
        repo_path = organization + '/' + repo_name

        url = reverse('getRepoInfo')
        content = {'repository': repo_path}

        #A váriavel response retorna a reposta da requisição que o client faz a url('getRepoInfo'), a variável repository
        #é um objeto do tipo repositório, a váriavel repo_path é uma basicamente a url do repositório que você quer pesquisar.
        #e a váriavel context é um dicionario do tipo repositório que vai ser preenchido por váriaveis repo_path que são do tipo path.
        
        response =  self.client.post(url, content)

        #esta variável vai pegar a variável response(que é a resposta do tipo https que damos ao usuário), pegar o seu contexto que é um dicionário 
        #de variáveis do tipo repo (repositório = repo) e depois chamar o método name para ver o nome da váriavel/objeto repo.
        
        response_repo_name = response.context['repo'].name
        
        #esse método usa o self para falar que o método é desta classe, e chama oo assertEquals que verifica que as váriaveis passadas
        #na assinatura são iguais (repo_name = response_repo_name)
        
        self.assertEquals(repo_name, response_repo_name)

    def test_get_contributors(self):

        contributor = 'Amanda Bezerra'
        login = 'amandabezerra'
        contributor_name = contributor + ':' + login

        url = reverse('getContributors')
        content = {'contributors': contributor_name}

        response = self.client.post(url, content)

        #response_contributor_name = response.context['contributors'].name.login

        contributors =  response.context['contributors']
        print(contributors)

        self.assertEquals(True, False)

