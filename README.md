# High-n-Safe

# Condições mínimas para utilização:
- Linguagem de programação Python 3;
- Ambiente de desenvolvimento. (Recomendamos o PyCharm);
- Ferramenta de design para banco de dados para rodar o script SQL. (Recomendamos MySQL Workbench);
- Instalação de navegador atualizado (Recomendamos o uso do Google Chrome);

Observação 1: Todas as instruções mencionadas neste documento são para usuários do sistema operacional Windows.

Observação 2: Ao baixar o Python 3 em sua máquina, na tela inicial do instalador, marcar a opção “Add Python 3.7 to PATH” para criar a variável de ambiente.

# Passo a passo para executar a aplicação:

1. Descompacte a pasta “High-n-Safe-master” que está disponível no link do projeto no GitHub;
2. No PyCharm, abra o projeto na opção “Open”;
3. No terminal do PyCharm, localizado na parte inferior do programa, digite o caminho “cd venv\Scripts”;
4. Execute a máquina virtual com o comando “activate”;
5. Execute o pip3 digitando o comando “python get-pip.py”;
  a. Instale as bibliotecas com “pip3 install -r requisitos.txt”;
6. No MySQL Workbench, crie uma nova conexão:
  b. No campo “Hostname” insira “www.db4free.net”;
  6.2. No campo “Port” insira “3306”;
  6.3. No campo “Username” insira “alunoufrpe”;
  6.4. Clique no botão “Store in Vault …”;
  6.5. Insira “ufrpe2018.2” no campo Password e confirma;
  6.6. No campo “Default Schema” insira “mydb_ufrpe” e confirma;
7. Voltando ao terminal do PyCharm, execute o comando “python run.py runserver”;
8. No navegador digite o endereço “127.0.0.1:5000/” e cofirme para abrir a aplicação;

# Equipe:

- Caroline Gomes;
- Eliana França;
- José Vidal;
- Marcone Carlos;
- Wenderson Leonardo.
