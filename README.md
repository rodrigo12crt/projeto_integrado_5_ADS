
# 🐾 KlugPet – Projeto Integrado 5 (ADS)

Este é um sistema web desenvolvido com Django como parte do Projeto Integrado V do curso de Análise e Desenvolvimento de Sistemas. O sistema é voltado para o gerenciamento de um daycare para pets — com cadastro de tutores, pets, serviços, agendamentos e geração de relatórios.

---

## 📌 Funcionalidades

- Cadastro e login de usuários com autenticação personalizada
- Cadastro de tutores e seus pets
- Gerenciamento de serviços e agendamentos
- Listagem e edição de registros
- Relatórios e geração de notas de atendimento com exportação em PDF
- Layout responsivo utilizando Bootstrap

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Django 5.2.1
- SQLite3
- HTML + CSS (Bootstrap)
- JavaScript
- Biblioteca `xhtml2pdf` para geração de PDFs

---

## 🚀 Como executar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/rodrigo12crt/projeto_integrado_5_ADS.git
cd projeto_integrado_5_ADS/projeto_integrado
```

2. **Crie e ative o ambiente virtual:**

```bash
python3 -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

3. **Instale as dependências:**

> Caso não tenha um arquivo `requirements.txt`, instale manualmente:
```bash
pip install django xhtml2pdf
```

4. **Aplique as migrações:**

```bash
python manage.py migrate
```

5. **Inicie o servidor:**

```bash
python manage.py runserver 0.0.0.0:8000
```

6. **Acesse o sistema:**

Abra no navegador: [http://localhost:8000](http://localhost:8000)  
Ou use o IP público da sua máquina virtual (ex: `http://<seu_ip>:8000`)

---

## 👤 Acesso ao sistema

Você pode criar um superusuário com o comando:

```bash
python manage.py createsuperuser
```

---

## 📂 Estrutura do Projeto

```
projeto_integrado_5_ADS/
├── projeto_integrado/
│   ├── settings.py
│   └── ...
├── klugpet/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos na faculdade.  
Uso livre para estudos e apresentações.

---

Desenvolvido com 💻 por Rodrigo e equipe – 2025.
