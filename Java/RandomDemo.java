package com.example;

import java.util.Random;   

public class RandomDemo {
    public static void main(String args[]) {
        // create Random object
        Random randomno = new Random();

        // get next random integer
        System.out.println("Next int value: " + randomno.nextInt());
    }
}
