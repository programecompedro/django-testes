from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.dados = {
            'nome':'Pedrão Demeu',
            'email':'pdemeu@outlook.com',
            'assunto':'Django Tests',
            'mensagem':'Muito legal usar Tests no Django'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome':'Pedrão Demeu',
            'assunto':'teste de assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)