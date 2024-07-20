#  https://www.hackerrank.com/challenges/java-anagrams/

import java.util.Scanner;
import java.io.*;
import java.util.*;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
        Scanner sc=new Scanner(System.in);
        String a=sc.nextLine();
        String b=sc.nextLine();
        if (isAnagram(a,b)) {
            System.out.println("Anagrams");
        } else {
            System.out.println("Not Anagrams");
        }
        sc.close();
    }
    private static boolean isAnagram(String a,String b) {
        a=a.toLowerCase();
        b=b.toLowerCase();
        if(a.length()!= b.length()){
            return false;
        }
        char[] arrayA = a.toCharArray();
        char[] arrayB = b.toCharArray();
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);
        return Arrays.equals(arrayA,arrayB);
    }
}
