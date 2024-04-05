#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Adafruit_NeoPixel.h>

#define PIN 2
#define NUMPIXELS 10
#define LED_ON_TIME 10000  // LED on time in milliseconds

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

const char* ssid = "MayTheForceBeWithWiFi";
const char* password = "6xY6NeERnCxJKnyk";

ESP8266WebServer server(80);

unsigned long ledTimers[NUMPIXELS];  // Array to store the timer for each LED

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print('.');
  }
  Serial.println("\nConnected to WiFi");

  strip.begin();
  for(int i = 0; i < NUMPIXELS; i++) {
    strip.setPixelColor(i, strip.Color(0, 0, 0));
    ledTimers[i] = 0;  // Initialize all LED timers to 0
  }
  strip.show();

  server.on("/", handleRoot);
  server.on("/led", handleLED);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();

  // Check each LED to see if it's time to turn it off
  for (int i = 0; i < NUMPIXELS; i++) {
    if (ledTimers[i] > 0 && millis() - ledTimers[i] > LED_ON_TIME) {
      strip.setPixelColor(i, strip.Color(0, 0, 0));
      strip.show();
      ledTimers[i] = 0;  // Reset the timer
    }
  }
}

void handleRoot() {
  server.send(200, "text/plain", "Hello from ESP8266 and NeoPixel!");
}

void handleLED() {
  String message = "LED Control";
  if (server.hasArg("num") && server.hasArg("red") && server.hasArg("green") && server.hasArg("blue")) {
    // Subtract 1 from num to align slot numbers with LED indices (slots start at 1, indices start at 0)
    int num = server.arg("num").toInt() - 1;
    int red = server.arg("red").toInt();
    int green = server.arg("green").toInt();
    int blue = server.arg("blue").toInt();

    // Check if the num is within the range of LEDs
    if (num >= 0 && num < NUMPIXELS) {
      strip.setPixelColor(num, strip.Color(red, green, blue));
      strip.show();
      ledTimers[num] = millis();  // Start the timer for this LED

      message = "LED " + String(num + 1) + " set to RGB(" + String(red) + "," + String(green) + "," + String(blue) + ")";
    } else {
      message = "LED number out of range";
    }
  } else {
    message = "Missing arguments";
  }
  server.send(200, "text/plain", message);
}
