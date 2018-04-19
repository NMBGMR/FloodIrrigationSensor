#include <CmdMessenger.h>


// global shit
// Attach a new CmdMessenger object to the default Serial port
CmdMessenger cmdMessenger = CmdMessenger(Serial);


enum {kERR, kACK, 
     kHELLO,          //2
     kECHO,           //3
     kGETTEMP,        //4
     kGETWATERSTATUS  //5
     };
// Commands we send from the PC and want to recieve on the Arduino.
// We must define a callback function in our Arduino program for each entry in the list below vv.

void attachCommandCallbacks()
{
  // Attach callback methods
  cmdMessenger.attach(invalid_command);
  cmdMessenger.attach(kECHO, echo);
  cmdMessenger.attach(kHELLO, hello);
  cmdMessenger.attach(kGETTEMP, get_temp);
  cmdMessenger.attach(kGETWATERSTATUS, get_water_status);
}


// Its also possible (above ^^) to implement some symetric commands, when both the Arduino and
// PC / host are using each other's same command numbers. However we recommend only to do this if you
// really have the exact same messages going in both directions. Then specify the integers (with '=')
void invalid_command(){
  cmdMessenger.sendCmd(kERR, "Invalid Command");
}

void hello() {
  cmdMessenger.sendCmd(kACK, "Hello World");
}
void echo() {

  char* r=cmdMessenger.readStringArg();
  cmdMessenger.sendCmd(kACK, r);
}

void get_temp() {

  //read temperature from board and send it back
  float temp = 28;
  cmdMessenger.sendCmd(kACK, temp);
}

void get_water_status(){
  // read the water status and return
  // 0= no water
  // 1= water
  int status =0;
  cmdMessenger.sendCmd(kACK, status);
}

void setup() {
  // put your setup code here, to run once:

  // set the baod rate (pulses)
  Serial.begin(115200);
  cmdMessenger.printLfCr();
  // Attach my application's user-defined callback methods
  attachCommandCallbacks();

}


void loop() {
  // put your main code here, to run repeatedly:

   cmdMessenger.feedinSerialData();
  

}
