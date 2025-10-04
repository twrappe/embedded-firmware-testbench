#define LED_PIN 13
#define SENSOR_PIN A0

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == '1') {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED_ON");
    } else if (cmd == '0') {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED_OFF");
    } else if (cmd == 'S') {
      int sensorValue = analogRead(SENSOR_PIN);
      Serial.print("SENSOR:");
      Serial.println(sensorValue);
    } else {
      Serial.println("ERR_CMD");
    }
  }
}
