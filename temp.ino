/*

  WiFi UDP Send and Receive String

 This sketch wait an UDP packet on localPort using a WiFi shield.

 When a packet is received an Acknowledge packet is sent to the client on port remotePort

 Circuit:

 * WiFi shield attached

 created 30 December 2012

 by dlf (Metodo2 srl)

 */

#include <SPI.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include "SparkFun_Qwiic_Twist_Arduino_Library.h"

int status = WL_IDLE_STATUS;
char ssid[] = "GuHome"; //  your network SSID (name)
char pass[] = "1095952792";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)
char serverAddress[] = ("192.168.5.167"); // Replace with the IP of the Flask server
unsigned int serverPort = 5000;      // Replace with the desired Flask server port number

unsigned int localPort = 5000;      // local port to listen on

char packetBuffer[255]; //buffer to hold incoming packet
char  ReplyBuffer[] = "132";       // a string to send back

WiFiUDP Udp;
WiFiClient client;
TWIST twist;

void setup() {

  //Initialize serial and wait for port to open:

  Serial.begin(1200);


  // attempt to connect to Wifi network:

  while (status != WL_CONNECTED) {
Serial.println("Failed to connect to network!");
    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:

    delay(10000);

  }

  Serial.println("Connected to wifi");

  printWifiStatus();

  Serial.println("\nStarting connection to server...");

  // if you get a connection, report back via serial:

  // Udp.begin(localPort);
}

void loop() {

    if (!client.connected())
  {
    if (client.connect(serverAddress, serverPort))
    {

      //int ching = twist.getCount();
      int ching = 42;
      String chong = String(ching);






      // Construct the HTTP POST request
      String jsonData = "{\"integer\":\"13232112342\"}";  // JSON data to be sent in the POST request

      String request = "POST / HTTP/1.1\r\n";
      request += "Host: " + String(serverAddress) + "\r\n";
      request += "Content-Type: application/json\r\n";
      request += "Content-Length: " + String(jsonData.length()) + "\r\n";
      request += "\r\n";
      request += jsonData;

      // Send the HTTP request
      client.println(request);

      // Wait for response
      while (client.connected() && !client.available()) {}

      // Read and print the response
      while (client.available())
      {
        char c = client.read();
        Serial.print(c);
      }

      client.stop();

      Serial.println("\nRequest completed");
    }
    else
    {
      Serial.println("Connection failed");
    }
  }

  delay(1000);

  }



void printWifiStatus() {


  // print the SSID of the network you're attached to:


  Serial.print("SSID: ");


  Serial.println(WiFi.SSID());


  // print your WiFi shield's IP address:


  IPAddress ip = WiFi.localIP();


  Serial.print("IP Address: ");


  Serial.println(ip);


  // print the received signal strength:


  long rssi = WiFi.RSSI();


  Serial.print("signal strength (RSSI):");


  Serial.print(rssi);


  Serial.println(" dBm");

}