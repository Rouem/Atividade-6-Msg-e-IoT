# Atividade-6-Msg-e-IoT
Penúltimo trabalho da disciplina de Sistemas Distribuídos

Descrição:

• Ideia Geral: Implementar um sistema distribuído usando o protocolo MQTT como broker de mensagens. O sistema deverá ter um publisher (smartphone) e um subscriber (um arduíno ou raspberry). O broker de mensagem pode ser o CloudMQTT.

• Operação: O publisher irá mandar uma mensagem ao subscriber com algum comando (acender um led, fazer um beep ou qualquer outra ação deste tipo). Pense em alguma ideia que seja útil e contextualizada, não sendo apenas acender o led em si. Se possível use sensores para incrementar.

• Linguagem: À sua escolha

• Apresentação das Informações: O smartphone deverá ter um botão de acionar o comando.

Sobre o trabalho:

Foram usados dois brokers MQTT: O Mosquitto, implementado com a linguagem C; e o PAHO MQTT, implementado usando a linguagem python. Um dispositivo móvel com um aplicativo para enviar mensagens ao broker e um Raspberry Pi 3 com broker mosquito, no papel de servidor.

![alt text](https://github.com/Rouem/Atividade-6-Msg-e-IoT/blob/master/diagSD.jpg)
 
O computador possui os dois brokers (PAHO e Mosquitto) e usando simultaneamente como subscribers (ouvintes ou observadores). Seu papel principal é agir como um monitor para visualização do tráfego de mensagens entre o dispositivo móvel e o broker servidor. O PAHO foi utilizado na implementação do monitor para que fosse possível visualizar quais tópicos estavam sendo acessados pelo aplicativo.
O Raspberry possui o papel de servidor, tendo o broker Mosquitto implentado para a comunicação de mensagens.
No dispositivo móvel foi utilizado o aplicativo Mqtt Dash, disponível gratuitamente para android.

