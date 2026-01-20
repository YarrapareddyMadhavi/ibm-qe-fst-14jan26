package com.example;

public class Activity {
   
    public static void main (String[] args){
        Car myCar= new Car();
        myCar.color="red";
        myCar.transmission="automatic";
        myCar.make=2022;
        myCar.displayCharacteristics();
        myCar.accelarate();
        myCar.brake();
    }



}
