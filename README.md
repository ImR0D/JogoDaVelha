# Jogo Da Velha
Jogo da Velha (Console Mode) criado com Python. O jogo foi desenvolvido apenas com o intuito de praticar programação com a linguagem Python.

Boas práticas de estruturação, não foram aplicadas neste jogo <strong>até o presente momento</strong>. Algumas linhas de código deverão ser melhoradas ao decorrer das implementações. Assim como a refatoração do código em momentos oportunos.

Cabe-se ressaltar que o jogo só rodará adequadamente no console do 'Windows', pois será possível realizar a limpeza da tela corretamente e o redimensionamento do console.
Outros terminais também podem ser utilizados, tais como, o próprio IDLE do Python (porém sem a limpeza da tela ou recursos providos do 'cmd' do Windows) ou o Terminal do Linux.
Não houve testes em plataformas adjacentes, apenas, no Sistema Operacional Windows (versão Windows 10 Home Single Language 22H2 x64), portanto, não foi possível determinar o funcionamento correto em outros S.O

## Para executar no console
- É necessário que baixe o arquivo 'Jogo Da Velha.py' e coloque em alguma pasta de sua preferência
- Após isso abra o 'Prompt de Comando' do Windows ou pressione 'Windows + R' e digite 'CMD'
- É necessário a versão do Python 3x (de preferencia) instalada adequadamente no computador e com o PATH do Python alocado no System32 para que o comando seja reconhecido adequadamente, no entanto, pode ser que na versão 2.x funcione, também, porém não foi testado em versões anteriores.
- A versão utilizada para testes e execução do jogo foi na versão 3.11.0 do Python
- Com isso basta apenas passar o comando [<strong><i>python "Jogo da Velha.py"</i></strong>] ou simplemente <strong><i>"Jogo da Velha.py"</i></strong> no CMD

[:exclamation:] : ERROS E BUGS NO CÓDIGO SERÃO TRATADOS E ATUALIZADOS ASSIM QUE POSSÍVEL, TAL QUAL, TODA REFATORAÇÃO DO CÓDIGO ASSIM QUE CONVENIENTE

## Menu principal (default)
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/f55047c9-cdb5-45ce-bc6e-d4e2e874925c)

## Menu principal (opção de saída)
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/3368f972-b53f-4c6d-a451-5cc08f55532b)

## Menu principal (modos de jogo)
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/80992668-f561-42c1-abc3-d69930b9d4c5)

Obs.: Em posteriores atualizações, será adicionado os modos de jogos: 
1. Jogador vs Máquina (Easy)............... Implementado? [:heavy_check_mark:]
2. Jogador vs Máquina (Medium)....... Implementado? [:heavy_check_mark:]
3. Jogador vs Máquina (Hard).............. Implementado? [:heavy_check_mark:]
4. Jogador vs Máquina (Insane)........... Implementado? [:x:]

## In-game
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/f105c42e-2a24-43f8-86c8-0698abac5603)

O jogo é composto de uma informação no topo da tela, indicando os comandos disponíveis.<br/>
Em seguida é exibido a sessão atual (jogadores ativos) e o modo de jogo.<br/>
E abaixo é exibido o jogador atual que está realizando a jogada

### Ao realizar a passagem de um comando a tela é atualizada:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/eeee8a3b-0771-4734-a787-75b79c42e348)

Após o envio do comando, o jogador é atualizado e a posição indicada pelo comando é atualizada no tabuleiro do jogo
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/0f40b2be-c1a2-4322-b479-ec9c0852538e)

Caso o jogo fique empatado (não tenha uma sequência de três X ou O no tabuleiro de um jogador específico) é exibido a tela:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/6d7c0443-a9c6-44d5-accb-bc5da83ecd04)

Com isso é possível pressionar qualquer tecla do teclado para jogar novamente, ou simplesmente 'Q' para sair do jogo
A partir daqui você é redirecionado para o menu principal, caso tenha optado pela opção de continuar jogando.

### Caso haja um vencedor na partida será exibida a tela:

Tela 1:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/36b80231-e814-4dee-8b76-4e3ed2866dc7)

Tela 2:
![image](https://github.com/ImR0D/JogoDaVelha/assets/97006482/a08e4ec6-8d6b-4299-bcd6-9a5e1abaf07c)

Obs.: Conforme visto na imagem 2, assim como caso o jogo fique empatado, haverá opção para retornar ao menu principal ou simplesmente sair do jogo
