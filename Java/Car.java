package com.example;

public class Car {
    String color;
    String transmission;
    int make;
    int tyres;
    int doors;
    public Car(){
        tyres=4;
        doors=4;

    }
    public void displayCharacteristics(){
        System.out.println(make);
        System.out.println(tyres);
        System.out.println(color);
        System.out.println(doors);
        System.out.println(transmission);

    }
    public void accelarate(){
        System.out.println("Car is moving");

    }
    public void brake(){
        System.out.println("Car has stopped");
    }


    
}
