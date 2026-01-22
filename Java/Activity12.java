

package com.example;


@FunctionalInterface
interface FuncInterfaceExample {
    String display(String str);
}

public class Activity12 {
    public static void main(String[] args) {

        
        FuncInterfaceExample obj = (String str) -> {
            return "Got this: " + str;
        };

       
        System.out.println(obj.display("Hello"));
    }
}
