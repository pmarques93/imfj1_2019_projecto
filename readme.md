# Introdução à Matemática e Física Para Videojogos I - Final Project - Parte 1

![pirâmide](https://temptempo.yolasite.com/resources/form%20-tf%20matematica.png)

---

## Trabalho Realizado

Para esta primeira parte do projecto, foram implementadas teclas para rotação e translação do objecto e foram criadas uma pirâmide e um *child object*, sendo este uma pirâmide menor na parte inferior da pirâmide principal.

### Contribuições
### Pedro Marques - (por ordem de trabalho realizado)

#### *sample.py*
Para realizar este trabalho comecei por parar a rotação do objecto de modo a poder controlá-lo. Após isto, implementei as teclas com o objetivo de realizar a translação e rotação da forma. Para isto, foram criadas variáveis para cada tecla com o valor inicial de *False*.    

As teclas ao serem premidas vão ter o valor alterado para *True* e ao largar a tecla o valor volta para *False*.
Ao serem premidas, no caso das setas e *pageup*/*pagedown*, vão incrementar o valor de *axis* de modo a rodar o objecto em torno de si próprio. Para qualquer uma destas teclas, ao terem o valor de *True* vão normalizar o *axis*.

No caso das teclas de translação, são semelhantes às de rotação, incrementado o valor da *position* do objecto.

#### *mesh.py*
Para desenhar uma pirâmide, comecei por criar 3 vértices no método *create_triangle*, de modo a criar um triângulo. Criei também 4 vértices no método *create_square* para a parte inferior da forma, aproveitando o código inicialmente criado.

Com estes métodos definidos de modo a criar triângulos e quadrados, o método *create_Pyramid* vai desenhar essas mesmas formas nas posições designadas, criando assim a forma em 3D.

#### *sample.py*
Após a realização das tarefas mencionadas anteriormente, apenas modifiquei valores do *child objecto* de modo a ficar desenhado para baixo. Modifiquei também a posição do objecto principal para ficar centrado no ecrã.

---

## Dificuldades

Durante esta primeira parte do projecto existiram poucas dificuldades. 
A implementação das teclas para executar a translação e rotação do objecto foram relativamente fáceis. 

O tópico onde surgiram algumas dúvidas foi durante a criação da forma diferente do cubo. Primeiro foi tentar perceber que parte do código tinha que alterar, após isto, foi perceber o que modificar nessa parte, de modo a criar faces triangulares com o vértice do topo inclinado para o centro da forma.

Quanto à criação do *child object* não existiram grandes dificuldades, sendo que já estava praticamente feito após a criação da forma maior.

---

## Grupo

Pedro Miguel Marques, 21900253  |  Github Account - pmarques93

Miguel Feliciano, 21904115  |  Github Account - Mike-Feliz

Luís Gomes, 21901362  |  Github Account - LuisTheGomes
