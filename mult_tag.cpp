#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>
#include <iostream>
#include <string>

#define RST_PIN         22  
#define SS_1_PIN        21  
#define SS_2_PIN        4  
#define BOTAO           5
#define NR_OF_READERS   2

int ESTADO_BOTAO = 1;
unsigned long lastDebounceTime = 0;  
unsigned long debounceDelay = 100;  

byte ssPins[] = {SS_1_PIN,SS_2_PIN};
String tagIDs[] = {
  "be41cd1d", // A
  "ce24251d", // E
  "53cef2f6", // B
  "ddb93e2d", // D
  "ceb9211d", // F
  "53e51df5", // C
  "83df46f5", // I
  "b3c424f5", // O
  "2301e8f6", // R
  "736347fa", // A
  "f37aebf6", // E
  "c3a526f5", // U
  "53400ef5", // M
  "73540ff5", // R
  "63d939f5", // L
  "731409f5", // Z
  "04e56a1a", // S
  "13701bf5"  // N
};
char tagLetters[] = {'A', 'E', 'B', 'D', 'F', 'C', 'I', 'O', 'R', 'A', 'E', 'U', 'M', 'R', 'L', 'Z', 'S', 'N'};

String dump_byte_array(byte *buffer, byte bufferSize) {
  String tag = "";
  for (byte i = 0; i < bufferSize; i++) {
    if (buffer[i] < 0x10) {
      tag += "0";
    }
    tag += String(buffer[i], HEX);
  }
  return tag;
}

char Dicionario(String tagID, String tagIDs[], int numTags) {
  for (int i = 0; i < numTags; i++) {
    if (tagID == tagIDs[i]) {
      return tagLetters[i];
    }
  }
  return '0';
}

MFRC522 mfrc522[NR_OF_READERS]; 

void setup() {
  Serial.begin(9600); 
  while (!Serial);    

  SPI.begin(); 

  for (uint8_t leitor = 0; leitor < NR_OF_READERS; leitor++) {
    
    mfrc522[leitor].PCD_Init(ssPins[leitor], RST_PIN); 
    mfrc522[leitor].PCD_DumpVersionToSerial();
  }

  pinMode(BOTAO, INPUT_PULLDOWN);  

}

void loop() {
  unsigned long currentTime = millis();
  ESTADO_BOTAO = digitalRead(BOTAO);


  if (currentTime - lastDebounceTime > debounceDelay) {
    ESTADO_BOTAO = digitalRead(BOTAO);
    if (ESTADO_BOTAO == LOW) {
      Serial.println("W");
    }
    lastDebounceTime = currentTime;
  }
  for (uint8_t leitor = 0; leitor < NR_OF_READERS; leitor++) {

    if (mfrc522[leitor].PICC_IsNewCardPresent() && mfrc522[leitor].PICC_ReadCardSerial()) {
      String tag = dump_byte_array(mfrc522[leitor].uid.uidByte, mfrc522[leitor].uid.size);
      char letra = Dicionario(tag, tagIDs, sizeof(tagIDs) / sizeof(tagIDs[0]));
      std::string numero_str = std::to_string(leitor);
      std::string resultado = numero_str + letra;
      std::cout << resultado << std::endl;
      mfrc522[leitor].PICC_HaltA();
      mfrc522[leitor].PCD_StopCrypto1();
    }
  }
  delay(50);
}
