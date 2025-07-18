  ♦ hangman_art.py
  
    Contém logo e estágios representando o número de vidas do usuário no formato de "ASCII Art"
    Esse arquivo serve apenas para armazenar essas informações
   
   --------------------
   
   ♦ hangman_words.py
   
    Contém uma lista aleatória de palavras 

   --------------------

   ♦ main.py:

    Arquivo principal do projeto
   
   --------------------

   <img width="701" height="258" alt="image" src="https://github.com/user-attachments/assets/ab4183b5-ddf8-4b02-b885-5b200502227a" />

   ♦ Importei o módulo "Random" para posteriormente, adicionar a função "random.choice()".
   
   ♦ Também importei elementos dos outros 2 arquivos como a arte ASCII e a logo e os armazenei em variáveis
   
   --------------------
   
<img width="670" height="398" alt="image" src="https://github.com/user-attachments/assets/1810386a-5b90-469c-9331-21fecd4e70ad" />


   ♦ Imprimi a logo do jogo

   ♦ Criei uma variável (chosen_word) para armazenar uma palavra escolhida aleatoriamente usando "random.choice()" na lista de palavras

   ♦ Criei uma variável (word_length) para armazenar o tamanho dessa palavra escolhida usando a função Len()

   ♦ Depois fiz uma variável (placeholder) vazia inicialmente e logo em seguida fiz um Loop For começando de 0 até o tamanho da variável word_length.
     Nisso, cada iteração adicionei um "_" ao placeholder e o imprimi depois para o usuário saber o tamanho da palavra

   --------------------

<img width="956" height="598" alt="image" src="https://github.com/user-attachments/assets/0728dea2-03bb-449b-b9b6-5fafe35b6846" />

   ♦ Criei um loop while. Comecei com a variável game_over como False para a inverter com not game_over e o loop começar com valor verdadeiro

   ♦ Fiz uma lista (right_letters) para conter as letras que o usuário acertar. Essa lista será mais importante mais pra frente

   ♦ Fiz a variável "lives" para já começar com o valor 6 e em seguida imprimi para o usuário ver quantas vidas restam

   ♦ Em seguida fiz a variável "guess" para armazenar um input do usuário, o perguntando qual letra ele acha que a palavra tem

   ♦ Gerei uma variável vazia "display" para armazenar as letras a partir do input do usuário e em seguida fiz uma limpeza de tela, usando a função print() para pular 100 linhas

--------------------

<img width="916" height="707" alt="image" src="https://github.com/user-attachments/assets/bcf7f3b6-0d8f-4e26-93e9-fb8fcf78d0c7" />

   ♦ Fiz uma condição para verificar se o usuário já adivinhou tal letra a partir dos dados armazenados dentro da lista right_letters[]
     Se sim, então não tiro nenhuma vida do usuário. Apenas imprimo que ele já adivinhou tal letra 

   ♦ Gerei um loop for para verificar cada caractere da palavra escolhida aleatoriamente (chosen_word)

     Se o input do usuário (guess) estiver certo, então adiciono esse input à variável "display" e também preencho a lista right_letters[] com esse mesmo input
     
     Logo depois em um "Elif", verifico se esse input do usuário já está na lista right_letters[].
     
     Se esse for o caso, adiciono a mensagem do item anterior e adiciono o input do usuário da mesma forma na variável "display"

     Se não, adiciono "_" na variável "display"

     Depois dessas condições, imprimo a variável "display" para o usuário ver se acertou ou não a letra

   ♦ Então verifico se o input do usuário está na palavra escolhida. Se não, perde uma vida e imprimo uma mensagem

   --------------------

   <img width="882" height="390" alt="image" src="https://github.com/user-attachments/assets/86681e5d-5e7f-4d82-b4b3-86dcd33e1ee8" />

   ♦ Imprimo a arte ASCII em determinada posição, dependendo da quantidade de vidas do usuário 

   ♦ Verifico se o usuário ganhou ou perdeu:
   
    Se não tiver mais o caractere "_" em "display", então o usuário ganhou

    Se o número de vidas do usuário for = 0, então o usuário perdeu

    Em ambos os casos, defino a variável "game_over" para Verdadeiro. Dessa forma o While termina e o jogo também
