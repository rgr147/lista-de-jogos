# 💻 Lista de jogos com Flask e Python.

![License](https://img.shields.io/badge/license-GPL-blue.svg)

# Indcice
- [Descrição do projeto](#descrição-do-projeto) 
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Contribuindo](#contribuindo)

## Descrição do projeto

 Aplicação desenvolvida com Flask e Python para cadastro de titulos de jogos que possuo nas bibliotecas da Steam, GOG, Ubsoft e Epic Games. A finalidade é pesquisar de modo rápido e identificar se, ao aproveitar aquela promoção de 80% de desconto, não estou comprando um jogo repetido que já posuo em outra plataforma.

Esse projeto foi desenvolvido para colocar em prática os conhecimentos adquiridos no curso de Framework Flask para Python

## Tecnologias Utilizadas
| Tecnologia | Documentação |
| - | - | 
| [Python](https://www.python.org/downloads/) | [Documentação Python](https://www.python.org/doc/) |
| [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/) | [Documentação Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/) |
| [Mysql](https://dev.mysql.com/downloads/mysql/) | [Documentação Mysql](https://dev.mysql.com/doc/) |
| [Bootstrap](https://getbootstrap.com/) | [Documentação Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) |
| [Git](https://git-scm.com/downloads) | [Documentação Git](https://git-scm.com/) |
| [GitHub](https://github.com/) | [GitHub](https://docs.github.com/pt) |

## Funcionalidades

- Página de login com validação de usuário e senha
- Cadastro de títulos, plataforma, genero e imagens das capas dos jogos
- Alteração dos títulos, plataforma, genero e imagens das capas dos jogos
- Exclusão dos títulos cadastrados
- Consulta de títulos por palavras

## Instalação
### Instale esse projeto localmente

1. Clone o repositório e acesse o diretório 
```
git clone https://github.com/rgr147/lista-de-jogos.git

cd lista-de-jogos/
```
2. Crie um ambiente virtual e ative-o para instalar as dependências do projeto
```
#Criando o ambiente virtual
python -m venv venv

#Iniciando o ambiente virtual no Windows
venv\Script\activate.bat

#Iniciando o ambiente virtual no Linux
source venv/bin/activate
```

3. Instalando as dependências
```
pip install -r requirements.txt
```

4. Antes de iniciar a aplicação, instale e inicie o banco de dados MySQL, versão 8.4.1 de preferência.

5. Configure as variáveis de ambiente do banco no arquivo `config.py`. No mesmo arquivo inclua uma palavra(string) na variável `SECRET_KEY`

6. Execute o arquivo `prepara_banco.py` para criar o banco de dados, cadastrar alguns usuários e títulos de exemplo. Consulte o arquivo para verificar os usuários e senhas de acesso.

7. Inicie a aplicação 
```
Flask run
```

8. Utilize o navegador para acessar a aplicação em `http://localhost:5000`

## Contribuindo

Contribuições são sempre bem-vindas!

Veja `contribuindo.md` para saber como começar.

## Aprendizados com esse projeto

Desenvolver esse projeto durante a formação em [Flask como framework web com Python](https://cursos.alura.com.br/formacao-flask) me permitiu aplicar os conhecimentos adquiridos no curso e entender os conceitos de ORM, utilizando o [SQLALchemy](https://www.sqlalchemy.org/) para interação com o banco de dados. Além disso implementei o [Flask WTF](https://flask-wtf.readthedocs.io/en/1.2.x/) nos formulários criados com FlaskForm para proteção contra ataques [CSFR](https://www.treinaweb.com.br/blog/cross-site-request-forgery-csrf-e-abordagens-para-mitiga-lo/) nas requisições HTTP.

## Sobre mim

* Meu nome é Roger, trabalho como Analista de Tecnologia e sou pós graduado em Analise e Desenvolvimento de Sistemas. Recentemente tenho focado nos estudos de programação com Python e Inteligência Artificial Generativa.

[![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rgr147?tab=overview&from=2024-07-01&to=2024-07-31) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roger-alves-rodrigues-melo-24443294/) [![project](https://img.shields.io/badge/Projeto_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rgr147/lista-de-jogos)

