/**
 * Write a program to count the number of integers and characters 
 * in a given string. Input: "nAJh4837sj"
 */

public class Program1 {
    public static void main(String[] args) {
        String input = "nAJh4837sj";
        int integerCount = 0;
        int characterCount = 0;

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (Character.isDigit(c)) {
                integerCount++;
            } else if (Character.isLetter(c)) {
                characterCount++;
            }
        }

        System.out.println("Number of integers: " + integerCount);
        System.out.println("Number of characters: " + characterCount);
    }
}