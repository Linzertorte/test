package EMRA;
import java.util.regex.Matcher;
import java.util.Scanner;
import java.util.regex.Pattern;
public class Parser {

	/**
	 * @param args
	 */
	
	
	private static Pattern namePattern = Pattern.compile("^name\\s+([A-Za-z\\s]+)$");
	private static Pattern birthdayPattern = Pattern.compile("^birthday\\s+(\\d{1,2}-\\d{1,2}-\\d{4})$");
	private static Pattern phonePattern = Pattern.compile("^phone\\s+(\\d+)$");
	static void updateMedicalRecordbyInputLine(MedicalRecord medicalRecord,String line){
		Matcher nameMatcher = namePattern.matcher(line);
		Matcher birthdayMatcher = birthdayPattern.matcher(line);
		Matcher phoneMatcher = phonePattern.matcher(line);
		
		if(nameMatcher.matches()){
			medicalRecord.setName(nameMatcher.group(1));
		}
		else if(birthdayMatcher.matches()){
			medicalRecord.setBirthday(birthdayMatcher.group(1));
		}
		else if(phoneMatcher.matches()){
			medicalRecord.setPhone(Integer.parseInt(phoneMatcher.group(1)));
		}
		return;
		
		
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
        MedicalRecord medicalRecord = new MedicalRecord();
        System.out.println(medicalRecord);
        
        
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNextLine()){
        	String line=scanner.nextLine();
        	updateMedicalRecordbyInputLine(medicalRecord,line);
        }
        System.out.println(medicalRecord);
	}

}
