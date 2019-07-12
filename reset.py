from gpiozero import Button

button=Button(2)
#def help():
#    for i in range(15):
#        print("i am here ", i)

def say():
    print('not pressed')
button.when_pressed =say