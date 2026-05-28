# 🚀 Urban Reports (SDU - Sistema de Denúncias Urbanas)

## 📌 Sobre o Projeto

O **SDU (Sistema de Denúncias Urbanas)** é uma aplicação web desenvolvida para facilitar o registro, visualização e acompanhamento de problemas urbanos.

A plataforma permite que usuários registrem denúncias contendo:

- Título
- Descrição
- Localização (latitude e longitude)

Essas informações são armazenadas em banco de dados e exibidas de forma organizada, incluindo visualização em mapa interativo.

---

## 🎯 Objetivo

- Promover a participação cidadã
- Melhorar a comunicação com a gestão pública
- Contribuir para cidades mais organizadas

---

## 🧠 Modelagem de Dados

### Entidades principais:

- **Usuário**
- **Denúncia**
- **Comentário**
- **Categoria**

### Relacionamentos:

- Um usuário pode criar várias denúncias (1:N)
- Um usuário pode fazer vários comentários (1:N)
- Uma denúncia pode ter vários comentários (1:N)
- Uma denúncia pode pertencer a várias categorias (N:N)

---

## 🗄️ Estrutura do Banco de Dados

### Exemplo de tabela:

```sql
CREATE TABLE usuario (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  senha VARCHAR(255) NOT NULL,
  tipo VARCHAR(20) DEFAULT 'comum',
  data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Relacionamento com integridade:

```sql
CREATE TABLE denuncia (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(150) NOT NULL,
  descricao TEXT NOT NULL,
  latitude DECIMAL(10,8),
  longitude DECIMAL(11,8),
  status VARCHAR(30) DEFAULT 'aberta',
  data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
  usuario_id INT NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuario(id)
  ON DELETE CASCADE
);
```

---

## 🛠️ Tecnologias Utilizadas

- HTML, CSS e JavaScript
- SQL (MySQL)
- Git & GitHub
- Leaflet (mapas interativos)

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/viitusx/urban-reports.git
```

2. Abra o projeto:

```bash
cd urban-reports
```

3. Execute o banco de dados:

```bash
python init_db.py
```

4. Execute o backend:

```bash
python run.py
```

5. Execute o frontend:

- Abra o arquivo `index.html` no navegador

---

## 🚧 Melhorias futuras

- Sistema de autenticação
- Painel administrativo
- API REST completa
- Notificações em tempo real

---

## 👨‍💻 Autor

Projeto desenvolvido por **Victor Silva, Klecius Thiago, Ruan Nicolas, Willian Gabriel**
