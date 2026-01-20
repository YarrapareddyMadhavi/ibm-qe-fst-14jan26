package com.example;

public class Activity2 {
    public static void main (String[] args){
        int[] num={10,77,10,54,-11,10};
        int count=0;
        for (int i: num){
            if (i==10){
                count=count+i;
               
            }
            

        }
        System.out.println(count);
    if (count==30){
        System.out.println("true");
        }
    else{
        System.out.println("false");
        }





    }
    
}
