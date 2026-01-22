package com.example;

interface BicycleParts {
    int tyres = 2;      
    int maxSpeed = 25;  
}


interface BicycleOperations {
    void applyBrake(int decrement); 
    void speedUp(int increment);    
}


class Bicycle implements BicycleParts, BicycleOperations {

    int gears;
    int currentSpeed;

  
    public Bicycle(int gears, int currentSpeed) {
        this.gears = gears;
        this.currentSpeed = currentSpeed;
    }

   
    @Override
    public void applyBrake(int decrement) {
        currentSpeed -= decrement;
        System.out.println("Current Speed after brake: " + currentSpeed);
    }

   
    @Override
    public void speedUp(int increment) {
        currentSpeed += increment;
        System.out.println("Current Speed after speeding up: " + currentSpeed);
    }

    public String bicycleDesc() {
        return "No of gears are " + gears + "\nSpeed of bicycle is " + maxSpeed;
    }
}


class MountainBike extends Bicycle {

    int seatHeight;

  
    public MountainBike(int gears, int currentSpeed, int seatHeight) {
        super(gears, currentSpeed);
        this.seatHeight = seatHeight;
    }

    public void setHeight(int newValue) {
        seatHeight = newValue;
    }

   
    @Override
    public String bicycleDesc() {
        return super.bicycleDesc() + "\nSeat height is " + seatHeight;
    }
}


public class Activity7 {

    public static void main(String[] args) {

        MountainBike mb = new MountainBike(3, 0, 25);

        System.out.println(mb.bicycleDesc());

        mb.speedUp(20);
        mb.applyBrake(5);
    }
}

    

