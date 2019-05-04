import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    print("Mensagem recebida: " ,str(message.payload.decode("utf-8")))
    print("Topico da mensagem: ",message.topic)

endereco_broker="endereco/ip do broker"
topico = "topico/teste"

cliente = mqtt.Client("Monitor")
cliente.on_message=on_message
cliente.connect(endereco_broker)
cliente.loop_start()
cliente.subscribe(topico)#subscribe mantem o cliente ouvindo todas as publicacoes

'''
use 'cliente.publisher(seuTopico,SuaMensagem)' para que publicar mensagens aos
outros clientes conectados ao broker

#time.sleep(15) # mantem o cliente conectado por 15s
#helbs.loop_stop() #encerra o loop
'''
