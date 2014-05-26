import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class stringReverse {
	public static void main(String[] args) {
		String input = "";
		String cont = "";
		boolean run = true;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(run){
			System.out.print("What word or phrase would you like to reverse?\n");
			try {
				input = br.readLine();
			} catch(IOException e) {
				e.printStackTrace();
			}
			
			System.out.print("Reversing '" + input + "' : \n");
			String reverse = Reverse(input);
			System.out.print(reverse);
			
			// continue?
			System.out.print("\nWould you like to continue?\n");
			try {
				cont = br.readLine();
				char str = cont.charAt(0);
				run = EndProgram(str);
			} catch(IOException e) {
				e.printStackTrace();
			}
			
		}
		
	}
	
	public static String Reverse(String s) {
		String[] aString = s.split("");
		String reverseString = "";
		for(int i = s.length(); i > 0; i--) {
			reverseString += aString[i];
		}
		return reverseString;
	}
	
	// Setter for flag to end continues the program.
	public static boolean EndProgram(char input) {
		boolean end = false;
		switch(input) {
			case 'y':
				end = true;
				break;
			case 'n':
				end = false;
				break;
		}
		return end;
		
	}
}
