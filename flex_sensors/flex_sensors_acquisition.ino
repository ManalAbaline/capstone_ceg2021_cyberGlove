const int FLEX_PIN0 = A0; // Pin connected to voltage divider output
const int FLEX_PIN1 = A1; // Pin connected to voltage divider output
const int FLEX_PIN2 = A2; // Pin connected to voltage divider output
const int FLEX_PIN3 = A3; // Pin connected to voltage divider output
const int FLEX_PIN4 = A6; // Pin connected to voltage divider output

// Measure the voltage at 5V and the actual resistance of your
// 47k resistor, and enter them below:
const float VCC = 5; // Measured voltage of Ardunio 5V line
const float R_DIV = 33000.0; // Measured resistance of 3.3k resistor

// Upload the code, then try to adjust these values to more
// accurately calculate bend degree.
const float STRAIGHT_RESISTANCE0 = 13000.0; // resistance when straight
const float BEND_RESISTANCE0 = 30000.0; // resistance at 90 deg

const float STRAIGHT_RESISTANCE1 = 13000.0; // resistance when straight
const float BEND_RESISTANCE1 = 30000.0; // resistance at 90 deg

const float STRAIGHT_RESISTANCE2 = 13000.0; // resistance when straight
const float BEND_RESISTANCE2 = 30000.0; // resistance at 90 deg

const float STRAIGHT_RESISTANCE3 = 13000.0; // resistance when straight
const float BEND_RESISTANCE3 = 30000.0; // resistance at 90 deg

const float STRAIGHT_RESISTANCE4 = 13000.0; // resistance when straight
const float BEND_RESISTANCE4 = 30000.0; // resistance at 90 deg

void setup() 
{
  Serial.begin(9600);
  pinMode(FLEX_PIN0, INPUT);
  pinMode(FLEX_PIN1, INPUT);
  pinMode(FLEX_PIN2, INPUT);
  pinMode(FLEX_PIN3, INPUT);
  pinMode(FLEX_PIN4, INPUT);
}

void loop() 
{
  // Read the ADC, and calculate voltage and resistance from it
  int flexADC0 = analogRead(FLEX_PIN0);
  int flexADC1 = analogRead(FLEX_PIN1);
  int flexADC2 = analogRead(FLEX_PIN2);
  int flexADC3 = analogRead(FLEX_PIN3);
  int flexADC4 = analogRead(FLEX_PIN4);
  
  float flexV0 = flexADC0 * VCC / 1023.0;
  float flexR0 = (R_DIV * (VCC / flexV0 - 1.0));
  float flexV1 = flexADC1 * VCC / 1023.0;
  float flexR1 = (R_DIV * (VCC / flexV1 - 1.0));
  float flexV2 = flexADC0 * VCC / 1023.0;
  float flexR2 = (R_DIV * (VCC / flexV0 - 1.0));
  float flexV3 = flexADC1 * VCC / 1023.0;
  float flexR3 = (R_DIV * (VCC / flexV1 - 1.0));
  float flexV4 = flexADC0 * VCC / 1023.0;
  float flexR4 = (R_DIV * (VCC / flexV0 - 1.0));


  // Use the calculated resistance to estimate the sensor's
  // bend angle:
  float angle0 = map(flexR0, STRAIGHT_RESISTANCE0, BEND_RESISTANCE0, 0, 90.0);
  float angle1 = map(flexR1, STRAIGHT_RESISTANCE1, BEND_RESISTANCE1, 0, 90.0);
  float angle2 = map(flexR2, STRAIGHT_RESISTANCE2, BEND_RESISTANCE2, 0, 90.0);
  float angle3 = map(flexR3, STRAIGHT_RESISTANCE3, BEND_RESISTANCE3, 0, 90.0);
  float angle4 = map(flexR4, STRAIGHT_RESISTANCE4, BEND_RESISTANCE4, 0, 90.0);

  Serial.println(String(angle0) + "x" + String(angle1) + "x" + String(angle2) + "x" + String(angle3) + "x" + String(angle4));

  delay(500);
}
