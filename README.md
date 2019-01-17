# High-n-Safe

# Condições mínimas para utilização:
Linguagem de programação Python 3;
Ambiente de desenvolvimento. (Recomendamos o PyCharm Community);
 Ferramenta de design para banco de dados para rodar o script SQL. (Recomendamos MySQL Workbench);
 Instalação de navegador atualizado (Recomendamos o uso do Google Chrome);

Observação 1: Todas as instruções mencionadas neste documento são para usuários do sistema operacional Windows.

Observação 2: Ao baixar o Python 3 em sua máquina, na tela inicial do instalador, marcar a opção “Add Python 3.7 to PATH” para criar a variável de ambiente.

# Passo a passo para executar a aplicação:

1. Descompacte a pasta “High-n-Safe-master” que está disponível no link do projeto no GitHub;
2. No PyCharm, abra o projeto na opção “Open”;

Observação 3: Caso esteja utilizando outro ambiente, os comandos executados no terminal do PyCharmy Community podem ser utilizados no prompt de Comando do Windows para executar a aplicação, selecionando a pasta do projeto “High-n-Safe” para executar os comandos:

3. No terminal do PyCharm Community, localizado na parte inferior do programa, digite o caminho “venv\Scripts\activate”;
4. Instale as bibliotecas com “pip3 install -r requisitos.txt”;

Observação 4: Se no terminal mostrar que precisa atualizar o pip, você deverá executar o comando “pip install --upgrade pip”.

5. Voltando ao terminal do PyCharm Community, execute o comando “python run.py runserver”;
6. No navegador digite o endereço “127.0.0.1:5000/” e cofirme para abrir a aplicação;

#Conexão com o banco de dados:

No MySQL Workbench, crie uma nova conexão:
- No campo “Hostname” insira “www.db4free.net”;
- No campo “Port” insira “3306”;
- No campo “Username” insira “alunoufrpe”;
- Clique no botão “Store in Vault …”;
- Insira “ufrpe2018.2” no campo Password e confirma;
- No campo “Default Schema” insira “mydb_ufrpe” e confirma;

On line:
- Acesse o “https://www.db4free.net/phpMyAdmin”;
- No campo “login”, insira “alunoufrpe”;
- No campo “senha”, insira “ufrpe2018.2”;
- Confirme.

No VSCode:
- Baixe a extensão vscode_ database;
- aperte CTRL + Shift + P;
- digite Sql connect , escolher mysql;
- No campo “hostname” insira “www.db4free.net”;
- No campo “root/user” insira “alunoufrpe”;
- No campo “password” insira “ufrpe2018.2”.

# Equipe:

- Caroline Gomes;
- Eliana França;;
- José Vidal;
- Marcone Carlos;
- Wenderson Leonardo.
