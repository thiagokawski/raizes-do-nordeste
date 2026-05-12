# Raizes do Nordeste
Curso: CST ANÁLISE E DESENVOLVIMENTO DE SISTEMAS.

Trabalho: Raízes do Nordeste


## 1. Instalação

### Criar .venv

Mac/Linux:
```bash
python3 -m venv .venv
```

Windows:
```bash
python -m venv .venv
```

### Ativar .venv
Mac/Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\Activate.ps1
```

### Instalar depêndencias
```bash
pip install -r requirements.txt
```

## 2. Executar

Crie um arquivo .env, com as variáveis necessárias, exemplo:
```text
DATABASE_URL=conection_string_aqui

JWT_SECRET_KEY=sua_chave_secreta_aqui
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

Em seguida, execute o comando:
```bash
python3 run.py
```

Para acessar a documentação detalhada, acesse: 
<a link="localhost:4201/docs">localhost:4201/docs</a>