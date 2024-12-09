

#### 1. **Criar Usuário**
- **Endpoint:** `/users`  
- **Método:** `POST`
- **Descrição:** Cria um novo usuário no sistema.
- **Requisição (JSON):**
  ```json
  {
    "name": "Nome do Usuário",
    "role": "Função do Usuário"
  }
  ```
- **Resposta (JSON):**
  ```json
  {
    "message": "Usuário criado com sucesso!"
  }
  ```
- **Código de Status:** 201 (Created)

---

#### 2. **Obter Lista de Usuários**
- **Endpoint:** `/users`  
- **Método:** `GET`
- **Descrição:** Retorna a lista de todos os usuários registrados no sistema.
- **Resposta (JSON):**
  ```json
  [
    {
      "id": 1,
      "name": "Nome do Usuário",
      "role": "Função do Usuário"
    },
    ...
  ]
  ```
- **Código de Status:** 200 (OK)

---

#### 3. **Atualizar Usuário**
- **Endpoint:** `/users/<int:id>`  
- **Método:** `PUT`
- **Descrição:** Atualiza as informações de um usuário existente.
- **Requisição (JSON):**
  ```json
  {
    "name": "Novo Nome",
    "role": "Nova Função"
  }
  ```
- **Resposta (JSON):**
  ```json
  {
    "message": "Usuário atualizado com sucesso!"
  }
  ```
- **Código de Status:** 200 (OK)

---

#### 4. **Deletar Usuário**
- **Endpoint:** `/users/<int:id>`  
- **Método:** `DELETE`
- **Descrição:** Deleta um usuário do sistema.
- **Resposta (JSON):**
  ```json
  {
    "message": "Usuário deletado com sucesso!"
  }
  ```
- **Código de Status:** 200 (OK)

---

#### 5. **Cadastrar Material**
- **Endpoint:** `/materials`  
- **Método:** `POST`
- **Descrição:** Cadastra um novo material.
- **Requisição (JSON):**
  ```json
  {
    "name": "Nome do Material",
    "material_type": "Tipo do Material",
    "validity_date": "YYYY-MM-DD"
  }
  ```
- **Resposta (JSON):**
  ```json
  {
    "message": "Material cadastrado com sucesso!",
    "serial": "CODIGO-UNICO"
  }
  ```
- **Código de Status:** 201 (Created)

---

#### 6. **Obter Lista de Materiais**
- **Endpoint:** `/materials`  
- **Método:** `GET`
- **Descrição:** Retorna a lista de todos os materiais cadastrados no sistema.
- **Resposta (JSON):**
  ```json
  [
    {
      "id": 1,
      "name": "Nome do Material",
      "material_type": "Tipo do Material",
      "validity_date": "YYYY-MM-DD",
      "serial": "CODIGO-UNICO"
    },
    ...
  ]
  ```
- **Código de Status:** 200 (OK)

---

#### 7. **Atualizar Material**
- **Endpoint:** `/materials/<int:id>`  
- **Método:** `PUT`
- **Descrição:** Atualiza as informações de um material existente.
- **Requisição (JSON):**
  ```json
  {
    "name": "Novo Nome",
    "material_type": "Novo Tipo",
    "validity_date": "YYYY-MM-DD"
  }
  ```
- **Resposta (JSON):**
  ```json
  {
    "message": "Material atualizado com sucesso!"
  }
  ```
- **Código de Status:** 200 (OK)

---

#### 8. **Deletar Material**
- **Endpoint:** `/materials/<int:id>`  
- **Método:** `DELETE`
- **Descrição:** Deleta um material do sistema.
- **Resposta (JSON):**
  ```json
  {
    "message": "Material deletado com sucesso!"
  }
  ```
- **Código de Status:** 200 (OK)

---

#### 9. **Rastrear Material por Serial**
- **Endpoint:** `/track/<serial>`  
- **Método:** `GET`
- **Descrição:** Retorna as etapas de processo associadas ao material com o serial especificado.
- **Resposta (JSON):**
  ```json
  [
    {
      "step_name": "Nome da Etapa",
      "failure": false
    },
    ...
  ]
  ```
- **Código de Status:** 200 (OK) ou 404 (Not Found) se o material não for encontrado.

---

#### 10. **Registrar Etapa de Processo**
- **Endpoint:** `/process_step`  
- **Método:** `POST`
- **Descrição:** Registra uma nova etapa no processo de rastreamento de um material.
- **Requisição (JSON):**
  ```json
  {
    "material_id": 1,
    "step_name": "Nome da Etapa",
    "failure": false
  }
  ```
- **Resposta (JSON):**
  ```json
  {
    "message": "Etapa do processo registrada com sucesso!"
  }
  ```
- **Código de Status:** 201 (Created)

---

#### 11. **Gerar Relatório em PDF**
- **Endpoint:** `/report/pdf`  
- **Método:** `GET`
- **Descrição:** Gera um relatório de materiais esterilizados em formato PDF.
- **Resposta:** Arquivo PDF gerado contendo as informações dos materiais.
- **Código de Status:** 200 (OK)

---

#### 12. **Gerar Relatório em Excel**
- **Endpoint:** `/report/xlsx`  
- **Método:** `GET`
- **Descrição:** Gera um relatório de materiais esterilizados em formato Excel (XLSX).
- **Resposta:** Arquivo Excel gerado contendo as informações dos materiais.
- **Código de Status:** 200 (OK)

---

### Dependências
- **Flask:** Framework web para Python.
- **Flask-SQLAlchemy:** ORM para interação com o banco de dados.
- **Flask-Migrate:** Extensão para migração de banco de dados.
- **Pandas:** Biblioteca para manipulação de dados em formato de tabela.
- **ReportLab:** Biblioteca para geração de PDFs.

### Exemplos de Uso

1. **Criar Usuário:**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "João", "role": "Admin"}' http://localhost:5000/users
   ```

2. **Obter Lista de Materiais:**
   ```bash
   curl http://localhost:5000/materials
   ```
