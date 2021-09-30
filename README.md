<h1 align="center">Django Testes</h1>
<p align="center">
    Aprendendo os Conceitos de Testes e aplicando
    No meu Projeto
</p>

<p>
    #### O que são Testes Unitários?
        - Um metodo de teste de software que valida se uma funcionalidade está ou não pronta para uso
    #### Bibliotecas Importantes
        - coverage==5.5 (Esse cara fala o que tem que ser testado)
        - model-mommy==2.0.0 (Esse cara vai automatizar criação de objetos nos models)
</p>
    ### Alguns comandos
        coverage run manage.py test
        coverage report
        coverage html
        cd htmlcov/
        python -m http.server

Adiciona no gitignora /htmlcov/* pra não enviar os arquivos gerados


### Features

- [ x ] Configurando os testes
- [ ] Testando Models
- [ ] Testando Formulários
- [ ] Testando Views

MIT License

Copyright (c) <2021> <Pedro Demeu>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.