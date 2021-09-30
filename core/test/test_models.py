import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path

class GetFilePathTestCase(TestCase):
    def setUp(self) -> None:
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        """
            Testa o nome da imagem criada
        """
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):
    def setUp(self) -> None:
        self.servico = mommy.make('Servico') #Mãe faz um serviço
    
    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    def setUp(self) -> None:
        self.cargo = mommy.make('Cargo') #Mãe faz um serviço
    
    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self) -> None:
        self.funcionario = mommy.make('Funcionario') #Mãe faz um serviço
    
    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)