# Modelo de Avaliação do Projeto de IoT

12/12/23

## Informações do Aluno/Equipa:
- **Equipa:** 
João
Dinis
Miguel
  

## Visão Geral do Projeto:
- **Título do Projeto:** 
Desenvolvimento de um sistema inteligente de detecção e alerta de fumo baseado em sensores de fumo e monóxido de carbono(mQ).
 

- **Breve Descrição do Projeto:**
O objetivo do seu projeto é desenvolver um sistema de detecção de fumo utilizando dois microcontroladores ESP32 WROOM D32, um dos quais está equipado com um sensor de gás MQ-135. O MQ-135 é um sensor de gás que pode detectar uma ampla gama de gases, incluindo monóxido de carbono (CO), amônia (NH3) e dióxido de enxofre (SO2).

No projeto, o MQ-135 será usado para detectar a presença de fumo. Quando o fumo é detetado, o sensor envia um sinal para um dos ESP32. Este ESP32, em seguida, comunica a informação para o nosso projeto Firebase. Todos os três sensores de cada sala enviam os dados separadamente, bem como uma mensagem quando o sensor passa os 400 a avisar o perigo de incendio.

- **Objetivo do Projeto:**
O objetivo do seu projeto é desenvolver um sistema de deteção de fumo utilizando o sensor de gás MQ-135 e um ESP32.
  
- **Contextualização da Aplicação IoT:**
Este sistema de deteção de fumo é uma aplicação IoT que pode ser usada para monitorizar a qualidade do ar em ambientes interiores, como casas e escritórios. Pode alertar os utilizadores quando os níveis de fumo excedem um certo limite, permitindo-lhes tomar medidas para melhorar a ventilação ou extinguir possíveis fontes de fogo.
## Componentes do Projeto:

### 1. Sensores e Dispositivos:
- **Lista de Sensores Utilizados:**
O sensor principal utilizado neste projeto é o sensor de gás MQ-135, leds e buzzers.

- **Descrição dos Dispositivos IoT Implementados:**
Os dispositivos IoT implementados neste projeto são três microcontroladores ESP32 WROOM D32. Os três estão equipados com o sensor de gás MQ-135 para detetar a presença de fumo.
### 2. Conetividade:
- **Tipo de Conetividade Utilizada (Wi-Fi, Bluetooth, LoRa, etc.):**
Neste projeto, a conectividade é fornecida através de Wifi integrado nos ESP32.

- **Justificação da Escolha da Conetividade:**
A escolha do Wifi deve-se à sua robustez e viabilidade para este projeto.

### 3. Plataforma e Protocolos:
- **Plataforma de Desenvolvimento Utilizada:**
A plataforma de desenvolvimento utilizada neste projeto é o Arduino IDE, juntamente com o Firebase.

### 4. Arquitetura do Sistema:
- **Arquitetura Geral do Sistema IoT:**
O sistema é composto por três microcontroladores ESP32 WROOM D32, estão equipados com um sensor de gás MQ-135.Ligados por Wifi ao nosso projeto Firebase

- **Integração entre Componentes:**
É realizada através da comunicação entre os microcontroladores ESP32 e o sensor de gás MQ-135. Quando o sensor MQ-135 deteta a presença de fumo, ele envia um sinal para o ESP32. O ESP32, por sua vez, processa este sinal e comunica a informação para o projeto Firebase através de uma conexão Wi-Fi.
## Desenvolvimento de Software:

### 1. Programação e Linguagens:
- **Linguagens de Programação Utilizadas:**
 A linguagem de programação utilizada para programar o ESP32 e o sensor MQ-135 é C++, através do Arduino IDE.
 A linguagem de programação utilizada no Jupyter notebook é python



- **Justificação da Escolha das Linguagens:**
C++ é uma linguagem de programação comum para programação de microcontroladores devido à sua eficiência e flexibilidade. Além disso, o Arduino IDE, que é usado para programar o ESP32, suporta C++.
Python é uma linguagem de programação de alto nível amplamente utilizada para análise de dados e visualização, tornando-a adequada para uso no Jupyter notebook.
 


### 2. Interface do Utilizador (UI):
- **Descrição da Interface do Utilizador:**
A interface do utilizador é o Jupyter notebook bem como o realtime database do firebase
 
  
### 3. Segurança:
- **Medidas de Segurança Implementadas:**
Não necessario medidas de segurança por ser um circuito fechado


## Testes e Validação:

### 1. Testes Funcionais:
Depois de passarmos por varios tipos de tecnologia, mesmo que estas nao tivessem o resultado esperado,acabamos por absorver bastante conteudo pelas tentativas.

### 2. Desafios e Soluções Encontrados:
- **Principais Desafios no Desenvolvimento do Projeto:**
Os desafios podem incluir garantir uma comunicação confiável e em tempo real entre os componentes, bem como a implementação de medidas de segurança.

- **Soluções Adotadas para Superar Desafios:**
As soluções podem incluir a utilização de protocolos de comunicação robustos e a implementação de medidas de segurança adequadas.
## Considerações Finais:

### 1. Lições Aprendidas:
- **Principais Lições Aprendidas Durante o Desenvolvimento:**
As lições aprendidas podem incluir a importância de uma comunicação robusta e segura em sistemas IoT, bem como a importância de testes rigorosos.

- **Recomendações para Futuros Projetos IoT:**
As recomendações podem incluir a utilização de componentes e protocolos de comunicação confiáveis, a implementação de medidas de segurança adequadas, e a realização de testes rigorosos.

### 2. Próximos Passos:
- **Planos para o Desenvolvimento Futuro do Projeto:**
Os planos futuros podem incluir a adição de mais sensores para monitorizar outros gases, ou a utilização de um módulo GSM para enviar alertas via SMS.

- **Possíveis Melhorias e Expansões:**
As possíveis melhorias podem incluir a melhoria da eficiência energética do sistema, a expansão da gama de gases que podem ser detetados, ou a melhoria da interface do utilizador.

## Avaliação Geral:

### 1. Originalidade e Criatividade:
- **Pontuação (de 0 a 20):**

### 2. Implementação Técnica:
- **Pontuação (de 0 a 20):**

### 3. Documentação e Apresentação:
- **Pontuação (de 0 a 20):**

### 4. Colaboração na Equipa (se aplicável):
- **Pontuação (de 0 a 20):**

### 5. Comentários Adicionais:
 
