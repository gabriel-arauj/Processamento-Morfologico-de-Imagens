
# Relatório Processamento Morfológico de Imagens

## 	<center>Introdução</center>
A morfologia trata de um modo geral do estudo da estrutura e formação, nesse caso, o contexto usado neste trabalho é o da morfologia matemática como uma ferramenta para extrair componentes das imagens que são úteis na representação e na descrição da forma de uma região, como fronteiras, esqueletos e o fecho convexo [1]. 

O processo da morfologia morfológica se baseia na geometria, em um contexto bem específico. A ideia básica é percorrer uma imagem com um elemento estruturante e quantificar a maneira com que este se encaixa ou não na imagem. No caso afirmativo, marca-se o local ou nível de cinza onde o elemento estruturante coube  na imagem. Dessa forma, pode-se extrair informações relevantes sobre o tamanho e forma de estruturas na imagem [2].

O objetivo deste relatório é descrever as respostas das questões apresentadas na atividade 02 da disciplina de Processamento Digital de Imagens.

 ## <center>Desenvolvimento</center>
 <p>
Todas as questões que se seguem são desenvolvidas a partir da imagem morfologia.png, uma imagem 200x200 que apresenta figuras de cores e formas diferentes e alguns pontos pretos, com um fundo branco. Vide Figura 1.
</p>

<center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/morfologia.png?raw=true"></center>
<center> Figura 1. Imagem original</center>

Todos os métodos utilizados neste trabalho foram implementados por mim na linguagem Python 3, usando como referência o livro [1]. O arquivo `.ipynb` contém os scrpts.

### Questão 01
A questão 01 pede para que todos os pontos pretos sejam eliminados da imagem, uma das formas de fazer tal procedimento é aplicar o filtro da mediana. Para obter o resultado mostrado na Figura 2 primeiro foi aplicado o filtro com uma janela de tamanho 5x5, em seguida um total de 5 aplicações sucessivas do mesmo filtro porém com a janela 3x3. Optou-se por esse método a fim de diminuir o efeito de suavização nas bordas dos objetos.
 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_01/questao_01.png?raw=true"></center>
<center> Figura 2. Filtro de mediana</center>

###  Questão 02
A Questão 02 pede para que os buracos das figuras verde, vermelho e magenta sejam retirados. Para realizar essa operação foi necessário encontrar pelo menos um ponto que pertença a cada um dos buracos, depois aplicar a função preenche_buraco para cada um desses pontos. Esse procedimento foi realizado em cada uma das figuras coloridas de maneira separada, Figura 3, pois a função requer uma imagem binária, e em seguida as imagens foram coloridas e  unidas novamente, Figura 4. O elemento estruturante usado é 3x3, com a âncora no meio, Figura 5.

 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_02/magenta.png?raw=true"><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_02/vermelho.png?raw=true"><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_02/verde.png?raw=true"></center>
<center> Figura 3. Imagens separadas</center>


 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_02/questao_02.png?raw=true"></center>
<center> Figura 4. Imagens sem buracos</center>

###  Questão 03
A Questão 03 requer que o fecho convexo dos objetos magenta, vermelho e verde sejam encontrados. O elemento estruturante usado é apresentado na Figura 6. Os mesmo procedimentos de transformar cada componente de cor em uma imagem binária foi utilizado, e em seguida as imagens foram unidos com a imagem original. 
 <center><img src="https://lh6.googleusercontent.com/FD3GtsIo7cAFvK2ZXNO3Irtn_FNWPvq2juLPLLGLtr6sT7ygvmehjKIKd2MsMCfx_t78y3zUGXtnb_FP9prKqWXSio9l63lU--7_VT4yzJg7Ng23vlbouNS3VHlOjzg1ZhyYHOcG"></center>
<center> Figura 6. Elemento estruturante</center>

 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_03/juntas.png?raw=true"></center>
<center>Figura 7. Imagens com fecho convexo  </center>


A Figura 7 mostra o resultado da função fecho convexo aplicado a cada um dos elementos e em seguida unidos com a imagem original.
### Questão 04
Na Questão 04 é necessário utilizar a transformada hit-or-miss para localizar cada um dos elementos da cor azul. Primeiro foi necessário obter as dimensões de cada um dos retângulos para em seguida criar elementos estruturantes de cada um. A função deve ser aplicada de maneira separada em cada um dos objetos para que o centro de cada um seja encontrado. 
 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_04/juntas.png?raw=true"></center>
<center>Figura 8. Ponto central no elemento azul   </center>

Como podemos observar na Figura 8, um ponto preto foi inserido no centro de cada um dos elementos de cor azul. 


### Questão 05
A Questão 05 pede para que o esqueleto do elemento de cor vermelha seja destacado. 
Para tal procedimento foi utilizado o elemento estruturante mostrado na Figura 9.
 <center><img width="100"  height="100" src="https://lh4.googleusercontent.com/hfj5NI4FKTx9IxxnqDSKjQuiSbfbc9SofUit3syU1kTFEuBpZCDOvwDSW3721aNz3WlPET_GmzAKdHb5nBvZ0GDRBvzkl67jOCO1eJnFLb-HVhKJeBQALRV92KMDrAHW5wmQw3Ea"></center>
<center>Figura 9.  Elemento estruturante </center>

 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_05/esqueleto.png?raw=true">
 <img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_05/juntas.png?raw=true"></center>
<center>Figura 10. Esqueletos </center>

A Figura 10.a mostra o apenas o esqueleto obtido a partir da função, enquanto que a 10.b mostra o esqueleto dentro da imagem original.

### Questão 06
A Questão pede para que a partir do fecho convexo da imagem de cor vermelha seja obtido o esqueleto. Então primeiro foi aplicado a função de fecho convexo, vide Figura 8, porém apenas na imagem vermelha. Em seguida, a partir da imagem obtida aplicou-se a função que obtém o esqueleto. O resultado pode ser observado na Figura 11.
 <center><img src="https://github.com/gabriel-arauj/Processamento-Morfologico-de-Imagens/blob/main/quest%C3%A3o_06/juntas.png?raw=true"></center>
<center>Figura 11. Esqueleto do Fecho Convexo</center>

 ## <center>Conclusão</center>
Este trabalho apresentou a resolução das questões apresentadas na atividade 02 da disciplina de  Processamento digital de imagens.
	É possível notar que o processamento morfológico das imagens é capaz de extrair informações relevantes sobre o tamanho e forma de estruturas na imagem.
 ## <center>Referências</center>	
[1] GONZALEZ, Rafael C.; WOODS, Richard C. Processamento digital de imagens . Pearson Educación, 2009.
[2] VALENTE. Raul A.; MESQUITA, Marcos E. Introdução à Morfologia Matemática Binária e em Tons de Cinza. Universidade Estadual de Londrina, 2010.

