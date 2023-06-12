# Jogo Da Velha
Jogo da Velha (Console Mode) criado com Python
O jogo foi desenvolvido apenas com o intuito de praticar programação com a linguagem Python.

Boas práticas como criação de classes ou responsabilidade única de funçõoes ou afins, não foram aplicadas neste jogo
Algumas linhas de código deverão ser melhoradas ao decorrer das implementações.

Cabe-se ressaltar que o jogo só rodará adequadamente no console do 'Windows', pois será possível realizar a limpeza da tela corretamente.
Outros terminais também podem ser utilizados, tais como, o próprio IDLE do Python (porém sem a limpeza da tela) ou o Terminal do Linux.
Não houve testes em plataformas adjacentes, apenas, no Sistema Operacional Windows (versão Windows 10 Home Single Language 22H2 x64)

## Para executar no console
- É necessário que baixe o arquivo 'Jogo Da Velha.py' e coloque em alguma pasta de sua preferência
- Após isso abra o 'Prompt de Comando' do Windows ou pressione 'Windows + R' e digite 'CMD'
- É necessário a versão do Python 3x (preferencia) instalada adequadamente no computador e com o PATH do Python alocado no System32 para que o comando seja reconhecido adequadamente, no entanto, pode ser que na versão 2.x funcione, também, porém não foi testado.
- A versão utilizada para testes e execução do jogo foi na versão 3.11.0 do Python
- Com isso basta apenas passar o comando 'python "Jogo da Velha.py"' ou simplemente "Jogo da Velha.py" no CMD

:Edit: ERROS E BUGS NO CÓDIGO SERÃO TRATADOS E ATUALIZADOS ASSIM QUE POSSÍVEL, TAL QUAL, TODA REFATORAÇÃO DO CÓDIGO ASSIM QUE CONVENIENTE

## Menu principal (default)
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/f55047c9-cdb5-45ce-bc6e-d4e2e874925c)

## Menu principal (opção de saída)
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/3368f972-b53f-4c6d-a451-5cc08f55532b)

## Menu principal (modos de jogo)
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/85b60e68-3d61-4062-9677-ea727896dab2)

Obs.: Em posteriores atualizações, será adicionado os modos de jogos: 
1. Jogador vs Máquina (Easy)............... Implementado? [:heavy_check_mark:]
2. Jogador vs Máquina (Medium)....... Implementado? [:heavy_check_mark:]
3. Jogador vs Máquina (Hard).............. Implementado? [:x:]

## Jogo da Velha
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/96b9aeba-0b3b-4534-98f9-aa79dc1aee75)

O jogo é composto de uma informação no topo da tela, indicando os comandos disponíveis
Em seguida é exibido a sessão atual (jogadores ativos) e o modo de jogo
E abaixo é exibido o jogador atual que está realizando a jogada

### Ao realizar a passagem de um comando a tela é atualizada:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/d5da58a1-25b7-475d-8cf1-9ac2d46a894a)

Após o envio do comando, o jogador é atualizado e a posição indicada pelo comando é atualizada no tabuleiro do jogo
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/6c99f84c-60cf-43d6-bfe6-53a2a06cfd4c)

Caso o jogo fique empatado (não tenha uma sequência de três X ou O no tabuleiro de um jogador específico) é exibido a tela:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/6d7c0443-a9c6-44d5-accb-bc5da83ecd04)

Com isso é possível pressionar qualquer tecla do teclado para jogar novamente, ou simplesmente 'Q' para sair do jogo
A partir daqui você é redirecionado para o menu principal, caso tenha optado pela opção de continuar jogando.

### Caso haja um vencedor na partida será exibida a tela:

Tela 1:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/e2d0ed37-4689-42c4-bdbe-84327f5085df)

Tela 2:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/a08e4ec6-8d6b-4299-bcd6-9a5e1abaf07c)

Obs.: Conforme visto na imagem 2, assim como caso o jogo fique empatado, haverá opção para retornar ao menu principal ou simplesmente sair do jogo
