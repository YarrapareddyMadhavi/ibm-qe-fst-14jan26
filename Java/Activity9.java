package com.example;
import java.util.ArrayList;

public class Activity9 {
    public static void main(String[] args) {
       
        ArrayList<String> myList = new ArrayList<String>();
       
        myList.add("Madhavi");
        myList.add("Anvitha");
        myList.add("Abhinandhan");
       
        myList.add(3, "Imran");
        myList.add(1, "hussain");
        
        System.out.println("Print All the Objects:");
        for(String s:myList){
            System.out.println(s);
        }
        
        System.out.println("3rd element in the list is: " + myList.get(2));
        System.out.println("Is harika is in list: " + myList.contains("Harika"));
        System.out.println("Size of ArrayList: " + myList.size());
        
        myList.remove("Imran");
        
        System.out.println("New Size of ArrayList: " + myList.size());
    }
}


