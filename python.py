import paho.mqtt.client as mqtt
import urllib.request
import gpiozero

connected = False
url = ""
led1=gpiozero.LED(18)
led2=gpiozero.LED(23)
led3=gpiozero.LED(24)
led4=gpiozero.LED(25)
led5=gpiozero.LED(12)


def on_connect(client, userdata, flags, rc):
    global connected
    global url
    if rc == 0:
        print("Connected with result code " + str(rc))
        url = "[Text file link/path that contains clomosy Project GUID]"
        try:
            with urllib.request.urlopen(url) as f:
                contents= f.read().decode('utf-8')
            if contents != "":
               client.subscribe(contents + "/clomosy/#")
               connected = True
            else:
                print("[002] GUID ERROR FOR P3")
        except Exception as e:
            print("[001] GUID Error For P3")
            print(f"An exception occurred: {str(e)}")
            client.disconnect()
    else:
        print("Connection failed with result code " + str(rc))


def on_message(client,userdata,message):
	strMsg=message.payload.decode("utf-8").split('!')
	print("message received from ",str(strMsg[0]))
	print("message: ",str(strMsg[1]))
	words=message.payload.decode("utf-8").split('!') 
	if  words[1] == 'ON1':
		led1.on()
	elif words[1] =='OFF1':
		led1.off()	
	if  words[1] == 'ON2':
		led2.on()
	elif words[1] =='OFF2':
		led2.off()	
	if  words[1] == 'ON3':
		led3.on()
	elif words[1] =='OFF3':
		led3.off()	
	if  words[1] == 'ON4':
		led4.on()
	elif words[1] =='OFF4':
		led4.off()	
	if  words[1] == 'ON5':
		led5.on()
	elif words[1] =='OFF5':
		led5.off()					


def main():		
    client = mqtt.Client("P3")
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("1","1")

    global connected
    if not connected:
        client.connect("1.1.1.1", 1111)

	
    client.loop_forever(1, None, True)


if __name__ == "__main__":
    main()
