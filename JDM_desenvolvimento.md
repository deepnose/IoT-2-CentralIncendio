# Modelo de Avaliação do Projeto de IoT

12/12/23

## Informações do Aluno/Equipa:
- **Equipa:** 
João
Dinis
Miguel
  

## Visão Geral do Projeto:
- **Título do Projeto:** 
Desenvolvimento de um sistema inteligente de detecção e alerta de fumaça baseado em sensores de fumo e monóxido de carbono(mQ).
 

- **Breve Descrição do Projeto:**
O objetivo do seu projeto é desenvolver um sistema de detecção de fumo utilizando dois microcontroladores ESP32 WROOM D32, um dos quais está equipado com um sensor de gás MQ-135. O MQ-135 é um sensor de gás que pode detectar uma ampla gama de gases, incluindo monóxido de carbono (CO), amônia (NH3) e dióxido de enxofre (SO2).

No projeto, o MQ-135 será usado para detectar a presença de fumo. Quando o fumo é detetado, o sensor envia um sinal para um dos ESP32. Este ESP32, em seguida, comunica a informação para o outro ESP32 via BLE. O segundo ESP32 é responsável por compilar as informações e enviá-las para um servidor MQTT usando Node-RED.

- **Objetivo do Projeto:**
O objetivo do seu projeto é desenvolver um sistema de deteção de fumo utilizando o sensor de gás MQ-135, um módulo Bluetooth Low Energy (BLE) e um ESP32.
  
- **Contextualização da Aplicação IoT:**
Este sistema de deteção de fumo é uma aplicação IoT que pode ser usada para monitorizar a qualidade do ar em ambientes interiores, como casas e escritórios. Pode alertar os utilizadores quando os níveis de fumo excedem um certo limite, permitindo-lhes tomar medidas para melhorar a ventilação ou extinguir possíveis fontes de fogo.
## Componentes do Projeto:

### 1. Sensores e Dispositivos:
- **Lista de Sensores Utilizados:**
O sensor principal utilizado neste projeto é o sensor de gás MQ-135.

- **Descrição dos Dispositivos IoT Implementados:**
Os dispositivos IoT implementados neste projeto são dois microcontroladores ESP32 WROOM D32. Um deles está equipado com o sensor de gás MQ-135 para detetar a presença de fumo. O outro ESP32 é responsável por receber as informações do primeiro ESP32 via BLE e enviá-las para um servidor MQTT.
### 2. Conetividade:
- **Tipo de Conetividade Utilizada (Wi-Fi, Bluetooth, LoRa, etc.):**
Neste projeto, a conectividade é fornecida através do Bluetooth Low Energy (BLE) integrado nos ESP32.

- **Justificação da Escolha da Conetividade:**
A escolha do BLE é ideal para este tipo de aplicação, pois permite uma comunicação sem fios eficiente e de baixo consumo de energia entre os dois ESP32.

### 3. Plataforma e Protocolos:
- **Plataforma de Desenvolvimento Utilizada:**
A plataforma de desenvolvimento utilizada neste projeto é o Arduino IDE, juntamente com o Node-RED para a compilação e envio de informações para um servidor MQTT.


- **Protocolos de Comunicação Empregados:**
Os protocolos de comunicação empregados neste projeto incluem o protocolo MQTT para a comunicação entre o ESP32 e o servidor MQTT, e o protocolo BLE para a comunicação entre os dois ESP32.

### 4. Arquitetura do Sistema:
- **Arquitetura Geral do Sistema IoT:**
O sistema é composto por dois microcontroladores ESP32 WROOM D32, um dos quais está equipado com um sensor de gás MQ-135. Os dois ESP32 comunicam entre si através de BLE. O segundo ESP32 é responsável por compilar as informações e enviá-las para um servidor MQTT usando Node-RED.

- **Integração entre Componentes:**
Os componentes são integrados através de comunicação sem fios. O sensor MQ-135 envia dados para o ESP32, que por sua vez comunica com o outro ESP32 através de BLE. O segundo ESP32 compila os dados e envia-os para um servidor MQTT.

## Desenvolvimento de Software:

### 1. Programação e Linguagens:
- **Linguagens de Programação Utilizadas:**
 A linguagem de programação utilizada para programar o ESP32 e o sensor MQ-135 é C++, através do Arduino IDE.



- **Justificação da Escolha das Linguagens:**
C++ é uma linguagem de programação comum para programação de microcontroladores devido à sua eficiência e flexibilidade. Além disso, o Arduino IDE, que é usado para programar o ESP32, suporta C++.
 


### 2. Interface do Utilizador (UI):
- **Descrição da Interface do Utilizador:**
A interface do utilizador é composta por notificações push, e-mails ou alarmes sonoros enviados para um dispositivo conectado via BLE quando o fumo é detetado.
 


- **Facilidades e Desafios na Implementação da UI:**
A implementação da UI pode ser desafiadora devido à necessidade de garantir que as notificações sejam enviadas de forma confiável e em tempo real. No entanto, a utilização de BLE facilita a comunicação sem fios com outros dispositivos.
 
  
### 3. Segurança:
- **Medidas de Segurança Implementadas:**
As medidas de segurança podem incluir a encriptação dos dados transmitidos via BLE e MQTT para proteger contra a interceção de dados.



- **Desafios Relacionados à Segurança:**
Os desafios relacionados à segurança podem incluir garantir que a encriptação seja implementada corretamente e que o sistema seja resistente a ataques.

## Testes e Validação:

### 1. Testes Funcionais:
- **Descrição dos Testes Realizados:**
Os testes funcionais podem incluir testar a detecção de fumo pelo sensor MQ-135, a comunicação entre os dois ESP32 via BLE, e o envio de dados para o servidor MQTT.


- **Resultados dos Testes:**
Os resultados dos testes dependerão da implementação específica do sistema.

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
 