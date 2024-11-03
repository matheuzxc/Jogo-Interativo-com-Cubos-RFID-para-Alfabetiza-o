# Jogo-Interativo-com-Cubos-RFID-para-Alfabetização
Este projeto apresenta um jogo educativo interativo para alfabetização, utilizando cubos físicos com RFID para a separação silábica. O jogo combina uma interface digital com manipulação tátil, promovendo a consciência fonológica. O objetivo é facilitar a alfabetização de crianças, oferecendo feedback imediato e uma experiência lúdica.

### 1. Introdução
Os jogos educativos têm um papel importante no processo de aprendizagem, especialmente no desenvolvimento das habilidades de leitura e escrita. Dentre esses jogos, destaca-se para este trabalho os jogos de separação silábica, que ajudam os alunos a compreender a estrutura das palavras através da identificação e manipulação das sílabas. Segundo Santos (2014), esse tipo de atividade é fundamental para o desenvolvimento da consciência fonológica, que é a habilidade de reconhecer e manipular os sons da fala.

Diversos jogos educativos visam a alfabetização, mas muitos se limitam a interfaces digitais, como aplicativos para tablets e computadores. Alguns estudos, como Healy (1999), mostram que a interação física pode potencializar a aprendizagem, mas poucos jogos exploram essa combinação. Comparado a soluções existentes, este trabalho apresenta um jogo que utiliza aspectos do digital e do físico, com o objetivo de potencializar o engajamento e ampliar a eficácia no aprendizado.

Este estudo explora o desenvolvimento e a aplicação de um jogo educativo interativo para alfabetização infantil, que combina elementos digitais e físicos. Utilizando cubos com tags RFID, o jogo propicia uma experiência de aprendizado tátil, integrando a leitura de palavras com a manipulação física dos cubos. A proposta visa estimular o desenvolvimento cognitivo e motor das crianças, oferecendo uma abordagem diferenciada para a alfabetização que transcende as limitações dos jogos exclusivamente digitais. 

## Estrutura de Pastas
- `sons`: Contém todos os arquivos de áudio utilizados no jogo.
- `imagens`: Inclui as imagens e gráficos utilizados no jogo.
- `fontes`: Armazena fontes customizadas para o layout e design textual do jogo.

As contribuições específicas do trabalho são:
1. A descrição do jogo, suas mecânicas e regras.
2. A apresentação das decisões para um protótipo funcional físico.
3. Experimentos do funcionamento do jogo, tanto digital quanto físico, para auxiliar nos próximos passos do projeto.

Este artigo está organizado da seguinte forma:
- A Seção 2 discute a fundamentação teórica da atividade de separação silábica, o contexto de jogos educativos, e o desenvolvimento cognitivo orientado com sistemas tangíveis.
- A Seção 3 descreve o jogo, mecânicas, e desenvolvimento do protótipo.
- A Seção 4 apresenta uma análise experimental em relação à viabilidade técnica da proposta e do protótipo.
- A Seção 5 discute as conclusões e próximas etapas do projeto.

## 2. Fundamentação Teórica

O processo de alfabetização nos três primeiros anos do Ensino Fundamental apresenta muitos desafios para a apropriação do sistema de escrita alfabética, permitindo que os alunos avancem para a junção das sílabas, formação de palavras e frases, até alcançarem autonomia nas práticas de leitura e escrita de pequenos textos [Marinho et al. 2023]. 

Segundo [Alves et al. 2022], professores enfrentam dificuldades em propor metodologias e estratégias que captem a atenção dos alunos e promovam a aprendizagem. A introdução de jogos pode ser uma forma de melhorar a participação dos alunos e obter um maior índice de aprendizagem em diversos conteúdos.

O jogo de separação silábica facilita a aprendizagem da leitura e escrita e estimula o pensamento crítico e a capacidade de resolver problemas, já que os alunos precisam analisar e segmentar palavras em unidades sonoras menores. Esse processo é essencial para a alfabetização, permitindo que os alunos compreendam que as palavras são formadas por diferentes sons que podem ser combinados para criar novas palavras [Santos 2014].

### 2.1. Desenvolvimento Cognitivo e Sistemas Tangíveis

O desenvolvimento cognitivo infantil avança à medida que as crianças exploram os aspectos físicos e espaciais do ambiente. Piaget, Gibson, Vygotsky, Dewey e Newell enfatizam as crianças como aprendizes ativos em um ambiente físico e social [Bransford et al. 2000]. Esse desenvolvimento envolve a aquisição de estruturas de conhecimento organizadas, chamadas esquemas, além da aquisição gradual de estratégias para lembrar, compreender e resolver problemas [Bransford et al. 2000].

Em [DeLoache et al. 1998], os autores demonstram que até mesmo crianças pequenas desenvolvem estratégias metacognitivas, ou seja, aprendem sobre o próprio processo de aprendizagem, incluindo a habilidade de autorregular a aprendizagem e refletir sobre a adequação das estratégias utilizadas.

Os sistemas tangíveis têm o potencial de envolver crianças em idade escolar em brincadeiras ativas que promovem o desenvolvimento cognitivo. [Healy 1999] defende formas tangíveis e físicas de interação computacional infantil, destacando que os movimentos do corpo, a capacidade de tocar, sentir, manipular e construir são essenciais para a compreensão das relações no mundo e o desenvolvimento cognitivo das crianças.

## 3. Apresentação do Jogo e Protótipo

O jogo desenvolvido é uma aplicação interativa que utiliza imagens e sons para criar uma experiência de aprendizado. Na tela do jogo, o jogador vê uma palavra com algumas letras faltantes, representadas por traços sublinhados, e uma imagem ilustrativa. O objetivo é preencher as letras faltantes usando cubos com tags RFID, que permitem a entrada de letras específicas. A Figura 1 apresenta a interface do jogo, onde é mostrada a imagem de uma banana e solicitada a última sílaba do nome dessa fruta.

Cada vez que uma letra é inserida, o sistema verifica a correção e fornece feedback. Se a sílaba estiver correta, um som de acerto é reproduzido e uma voz digital pronuncia a palavra completada. Se a sílaba estiver incorreta, um som de erro é tocado e a tentativa é marcada como falha. O jogo monitora o tempo e a pontuação, que é baseada na rapidez e precisão ao completar as palavras.

![image](https://github.com/user-attachments/assets/e866b508-0d6f-45ba-b260-27445779a74d)


### 3.1. Modelagem do Sistema

Para o desenvolvimento do projeto, foi utilizada a metodologia Arcadia (Architecting for Critical Systems) com a ferramenta Capella. A metodologia passa por camadas de especificação da arquitetura do sistema: **Operational Analysis**, **System Analysis**, **Logical Architecture** e **Physical Architecture**. As duas primeiras etapas abordam o entendimento da missão, enquanto as duas últimas tratam de como a missão será conduzida e quais recursos serão utilizados [Voirin 2017].

#### 3.1.1. Análise Operacional e Lógica

A Figura 3 apresenta a análise operacional do sistema, onde são definidas as operações e funções que o jogo deve executar, identificando as necessidades operacionais e requisitos funcionais. Foram identificados os seguintes requisitos:

![image](https://github.com/user-attachments/assets/668c90f4-6a38-4478-8acf-4554280384e2)


1. **Identificar Letras**: O sistema deve identificar corretamente as palavras associadas aos cubos com tags RFID.
2. **Identificação do Posicionamento**: O sistema deve reconhecer o posicionamento dos cubos nos slots e registrar as interações.
3. **Visualizar Palavra**: A letra escolhida deve ser exibida na interface de forma clara.
4. **Geração de Feedback**: O sistema deve fornecer feedback imediato sobre a correção da letra inserida.
5. **Geração de Perfil das Jogadas**: O sistema deve registrar e gerar um perfil detalhado das jogadas, incluindo tempo de resposta, acertos e erros.

A estrutura lógica do sistema, apresentada na Figura 4, descreve como os componentes interagem para atender aos requisitos estabelecidos.

![image](https://github.com/user-attachments/assets/555781c1-11e9-4de5-b704-af06c7ad7bec)


### 3.2. Dispositivo Físico

Para a comunicação e processamento do hardware, foram considerados três microcontroladores: **Arduino Uno**, **ESP32 WROOM** e **Raspberry Pi**. O **ESP32** foi selecionado por sua capacidade de processamento e custo-benefício. Ele oferece uma frequência operacional entre 80 MHz e 240 MHz, ampla gama de opções de comunicação (Wi-Fi, Bluetooth, UART, SPI, SDIO, I2C), e é acessível em termos de custo e disponibilidade.

Os modelos **RC522** e **RDM6300** foram analisados para a implementação dos módulos RFID. O RC522 foi escolhido devido à sua frequência de operação de 13,56 MHz, que oferece uma leitura rápida e eficiente, além de ser econômico. O RC522 se comunica com o ESP32 via protocolo SPI. A configuração de múltiplos módulos foi planejada para garantir leituras simultâneas, utilizando pinos exclusivos para cada leitor, permitindo escalabilidade.

![image](https://github.com/user-attachments/assets/006455ac-117b-4e24-8842-7501f5a849a1)


A bancada do dispositivo foi projetada para acomodar todos os componentes e ser de fácil fabricação e escalabilidade. Optou-se por MDF e corte a laser, possibilitando uma estrutura encaixável, sem parafusos ou colas. Além disso, o jogo é executado em um computador, com a Figura 5 apresentando a implementação do sistema RFID com os módulos RC522 e ESP32.

Na manufatura, foram desenvolvidos cubos com letras e uma mesa para leitura. Os cubos são feitos de MDF, material escolhido pela disponibilidade e facilidade de corte a laser. Cada face do cubo possui uma letra e uma tag RFID, permitindo a identificação precisa das letras pelo jogo. Os cubos são ocos, facilitando a inserção e proteção das tags RFID.

A mesa, também feita de MDF, foi projetada para ser robusta e segura para uso infantil.

![image](https://github.com/user-attachments/assets/8583f2ca-505c-4721-8b02-7f570a4be91b)


