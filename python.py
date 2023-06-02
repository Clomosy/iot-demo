import paho.mqtt.client as mqtt
import urllib.request
import gpiozero

connected = False
url = ""
led1=gpiozero.LED(18)

def on_connect(client, userdata, flags, rc):
    global connected
    global url
    if rc == 0:
        print("Connected with result code " + str(rc))
        url = "https://clomosy.com/iot/p2.txt"
        try:
            with urllib.request.urlopen(url) as f:
                contents = f.read().decode('utf-8')
            if contents != "":
                client.subscribe(contents + "/LEDONOFF/#")
                connected = True
            else:
                print("[002] GUID Error For P2")
        except:
            print("[001] GUID Error For P2")
            client.disconnect()
    else:
        print("Connection failed with result code " + str(rc))
 def on_message(client,userdata,message):
    strMsg=message.payload.decode("utf-8").split('!')
    print("message received from ",str(strMsg[0]))
    print("message: ",str(strMsg[1]))
    words=message.payload.decode("utf-8").split('!') 
    if words[1] == 'ONRED':
        led1.on()
    elif words[1] == 'OFFRED':
        led1.off()

def main ():
    client = mqtt.Client('P2')
    client.on_connect = on_connect
    client.on_message = on_message

    global connected
    if not connected:
        client.connect("1.1.1.1",1111)

    client.loop_forever(1,None, True) 
if __name__ ==  "__main__":
    main()
