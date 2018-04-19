import serial
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    delay = 1

    while 1:
        
        ask_arduino(ser, '2;', delay) # hello
        ask_arduino(ser, '3, Foobar;', delay) # echo
        ask_arduino(ser, '4;', delay) # get temp
        ask_arduino(ser, '5;', delay) # get status
        time.sleep(1)
               
def ask_arduino(ser, command, delay):
    
    delay = delay/1000.
    
    ser.write(command)
    time.sleep(delay)
    message = ser.readline()
    message = message.strip()
    print "asked {} >> {}".format(command, message)
    
    
if __name__ == "__main__":

    main()
    
    
