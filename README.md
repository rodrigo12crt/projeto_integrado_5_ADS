
# Paw Pals – Projeto Integrado 5º (ADS)

Este é um sistema web desenvolvido com Django como parte do Projeto Integrado do curso de Análise e Desenvolvimento de Sistemas. O sistema é voltado para o gerenciamento de um daycare para pets — com cadastro de tutores, pets, serviços, agendamentos e geração de relatórios.

---

## Funcionalidades

- Cadastro e login de usuários com autenticação personalizada
- Cadastro de tutores e seus pets
- Gerenciamento de serviços e agendamentos
- Listagem e edição de registros
- Relatórios e geração de notas de atendimento com exportação em PDF
- Layout responsivo utilizando Bootstrap

---

## Tecnologias Utilizadas

- Python 3.10+
- Django 5.2.1
- SQLite3
- HTML + CSS (Bootstrap)
- JavaScript

---

## Como executar o projeto

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

```bash
pip install -r requirements.txt
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

User: admin
Senha: adm123456
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

Este projeto foi desenvolvido para fins acadêmicos.  
Uso livre para estudos.

---
