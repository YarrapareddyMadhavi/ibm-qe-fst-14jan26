package com.example;

// Interface 1
interface BicycleParts {
    int tyres = 2;      // number of tyres
    int maxSpeed = 25;  // max speed
}

// Interface 2
interface BicycleOperations {
    void applyBrake(int decrement); // slow down
    void speedUp(int increment);    // speed up
}

// Base class implementing both interfaces
class Bicycle implements BicycleParts, BicycleOperations {

    int gears;
    int currentSpeed;

    // Constructor
    public Bicycle(int gears, int currentSpeed) {
        this.gears = gears;
        this.currentSpeed = currentSpeed;
    }

    // Implement applyBrake
    @Override
    public void applyBrake(int decrement) {
        currentSpeed -= decrement;
        System.out.println("Current Speed after brake: " + currentSpeed);
    }

    // Implement speedUp
    @Override
    public void speedUp(int increment) {
        currentSpeed += increment;
        System.out.println("Current Speed after speeding up: " + currentSpeed);
    }

    // Description method
    public String bicycleDesc() {
        return "No of gears are " + gears + "\nSpeed of bicycle is " + maxSpeed;
    }
}

// Derived class extending Bicycle
class MountainBike extends Bicycle {

    int seatHeight;

    // Constructor
    public MountainBike(int gears, int currentSpeed, int seatHeight) {
        super(gears, currentSpeed);
        this.seatHeight = seatHeight;
    }

    // Set seat height
    public void setHeight(int newValue) {
        seatHeight = newValue;
    }

    // Override bicycleDesc
    @Override
    public String bicycleDesc() {
        return super.bicycleDesc() + "\nSeat height is " + seatHeight;
    }
}

// Driver class with main
public class Activity7 {

    public static void main(String[] args) {

        MountainBike mb = new MountainBike(3, 0, 25);

        System.out.println(mb.bicycleDesc());

        mb.speedUp(20);
        mb.applyBrake(5);
    }
}

    

