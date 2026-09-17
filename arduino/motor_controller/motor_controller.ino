
const int LEFT_IN1 = 5;
const int LEFT_IN2 = 6;

const int RIGHT_IN1 = 9;
const int RIGHT_IN2 = 10;


void setup() {

  Serial.begin(115200);

  pinMode(LEFT_IN1, OUTPUT);
  pinMode(LEFT_IN2, OUTPUT);

  pinMode(RIGHT_IN1, OUTPUT);
  pinMode(RIGHT_IN2, OUTPUT);

  stopMotors();

  Serial.println("Motor controller ready.");
}


void loop() {

  if (Serial.available() > 0) {

    String command = Serial.readStringUntil('\n');

    command.trim();
    command.toUpperCase();

    if (command == "FORWARD") {

      moveForward();

    }
    else if (command == "BACKWARD") {

      moveBackward();

    }
    else if (command == "LEFT") {

      turnLeft();

    }
    else if (command == "RIGHT") {

      turnRight();

    }
    else if (command == "STOP") {

      stopMotors();

    }
  }
}


void moveForward() {

  digitalWrite(LEFT_IN1, HIGH);
  digitalWrite(LEFT_IN2, LOW);

  digitalWrite(RIGHT_IN1, HIGH);
  digitalWrite(RIGHT_IN2, LOW);
}


void moveBackward() {

  digitalWrite(LEFT_IN1, LOW);
  digitalWrite(LEFT_IN2, HIGH);

  digitalWrite(RIGHT_IN1, LOW);
  digitalWrite(RIGHT_IN2, HIGH);
}


void turnLeft() {

  digitalWrite(LEFT_IN1, LOW);
  digitalWrite(LEFT_IN2, HIGH);

  digitalWrite(RIGHT_IN1, HIGH);
  digitalWrite(RIGHT_IN2, LOW);
}


void turnRight() {

  digitalWrite(LEFT_IN1, HIGH);
  digitalWrite(LEFT_IN2, LOW);

  digitalWrite(RIGHT_IN1, LOW);
  digitalWrite(RIGHT_IN2, HIGH);
}


void stopMotors() {

  digitalWrite(LEFT_IN1, LOW);
  digitalWrite(LEFT_IN2, LOW);

  digitalWrite(RIGHT_IN1, LOW);
  digitalWrite(RIGHT_IN2, LOW);
}
