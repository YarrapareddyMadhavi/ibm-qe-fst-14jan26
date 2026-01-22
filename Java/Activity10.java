package com.example;

import java.util.HashSet;

public class Activity10 {
    public static void main(String[] args){
        HashSet<String> hs=new HashSet<String>();
        hs.add("app");
        hs.add("pop");
        hs.add("sos");
        hs.add("map");
        hs.add("rome");
        hs.add("pap");
        System.out.println(hs);
        System.out.println(hs.size());
        System.out.println(hs.remove("pop"));
         if(hs.remove("pop")) {
        	System.out.println("pop removed from the Set");
        } else {
        	System.out.println("pop is not present in the Set");
        }
        

        System.out.println("Checking if rome is present: " + hs.contains("rome"));
       
        System.out.println("Updated HashSet: " + hs);




    }
    
}
