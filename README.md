# Sistema de Gerenciamento de Ordens de Serviço 📋⚙️

## Descrição 📝

Este projeto é um **Sistema de Gerenciamento de Ordens de Serviço** simples, desenvolvido em **Python** utilizando a biblioteca **Tkinter** para a interface gráfica e o banco de dados **SQLite** para o armazenamento das informações. O sistema permite ao usuário adicionar, visualizar, editar e excluir ordens de serviço de maneira prática e eficiente. 

Este sistema pode ser utilizado em diversos cenários, como oficinas, prestadores de serviço ou qualquer outra área onde seja necessário o controle de ordens de serviço. 🚗🔧

## Funcionalidades ✨

- **Cadastro de Ordens de Serviço**: Permite adicionar novas ordens de serviço informando o nome do cliente, a descrição do serviço e a data da ordem. 📝
- **Visualização das Ordens de Serviço**: Exibe todas as ordens cadastradas de forma organizada. 📑
- **Edição de Ordens de Serviço**: Permite ao usuário editar os detalhes de uma ordem de serviço já cadastrada. ✏️
- **Exclusão de Ordens de Serviço**: O usuário pode excluir ordens de serviço que não são mais necessárias. ❌

## Tecnologias Utilizadas 🛠️

- **Tkinter**: Biblioteca gráfica do Python para criar interfaces de usuário. 🖥️
- **SQLite**: Banco de dados relacional simples embutido no Python. 💾

## Estrutura do Projeto 🗂️

### 1. **Classe `OrdemServicoApp`**

A classe principal que define o aplicativo e sua interface gráfica.

#### Métodos principais:

- **`__init__(self, root)`**: Inicializa a interface gráfica e a conexão com o banco de dados. 🌐
- **`create_table(self)`**: Cria a tabela `ordens_servico` no banco de dados, se não existir. 🏗️
- **`create_widgets(self)`**: Cria os widgets (rótulos, campos de entrada, botões) para a interface. 🖱️
- **`add_ordem(self)`**: Adiciona uma nova ordem de serviço ao banco de dados. ➕
- **`view_ordens(self)`**: Exibe uma lista de todas as ordens de serviço cadastradas. 👀
- **`edit_ordem(self, listbox)`**: Permite editar os detalhes de uma ordem de serviço. ✍️
- **`save_edit(self, ordem_id, nome_cliente, descricao, data, edit_window)`**: Salva as alterações feitas em uma ordem de serviço. 💾
- **`delete_ordem(self, listbox)`**: Exclui uma ordem de serviço do banco de dados. 🗑️
- **`clear_entries(self)`**: Limpa os campos de entrada após adicionar uma nova ordem de serviço. 🚮

### 2. **Banco de Dados**

- O banco de dados SQLite utilizado chama-se `ordens_servico.db`. 💻
- A tabela `ordens_servico` possui os seguintes campos:
  - **id**: Identificador único da ordem de serviço (chave primária). 🔢
  - **nome_cliente**: Nome do cliente. 👤
  - **descricao**: Descrição do serviço solicitado. 🛠️
  - **data**: Data da ordem de serviço. 📅

## Como Rodar o Projeto 🚀

### Pré-requisitos

- Python 3.x 🐍
- Biblioteca Tkinter (geralmente vem instalada com o Python) 🖥️
- Biblioteca SQLite (também embutida no Python) 💾

### Passos para execução:

1. Clone ou baixe este repositório. 📂
2. Abra o terminal ou prompt de comando. 💻
3. Navegue até o diretório onde o arquivo Python está salvo. 📁
4. Execute o script com o comando:

```bash
python ordem.py
