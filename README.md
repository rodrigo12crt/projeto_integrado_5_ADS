# Projeto Integrado 5 Semestre ADS - KlugPet

Este é um sistema desenvolvido para a disciplina de Projeto Integrado do curso de Análise e Desenvolvimento de Sistemas. O sistema gerencia usuários, serviços, agendamentos e pets.

## Funcionalidades

- Cadastro de usuários personalizados
- Gerenciamento de pets e seus donos
- Controle de agendamentos e serviços
- Interface amigável com Bootstrap

## Tecnologias

- Python 3.10+
- Django 5.2.1
- SQLite3
- HTML, CSS (Bootstrap)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/rodrigo12crt/projeto_integrado_5_ADS.git
cd projeto_integrado_5_ADS/projeto_integrado

## Crie e ative o ambiente virtual:

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

## Instale as dependências:
pip install -r requirements.txt

## Rode as migrações:
python manage.py migrate

## Inicie o servidor:
python manage.py runserver 0.0.0.0/8000

## Usuário padrão (para testes)
Usuário: admin
Senha: adm123456
