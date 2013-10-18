package EMRA;

import java.util.regex.Matcher;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.ArrayList;

public class Parser {

	/**
	 * @param args
	 */

	private static Pattern namePattern = Pattern
			.compile("^name\\s+([A-Za-z\\s]+)$");
	private static Pattern birthdayPattern = Pattern
			.compile("^birthday\\s+(\\d{1,2}-\\d{1,2}-\\d{4})$");
	private static Pattern phonePattern = Pattern.compile("^phone\\s+(\\d+)$");
	private static Pattern addressPattern = Pattern
			.compile("^address\\s+([A-Za-z0-9\\s,]+)$");
	private static Pattern addressPatternAdditional = Pattern
			.compile("^\\s+([A-Za-z0-9\\s,]+)$");
	private static Pattern emailPattern = Pattern
			.compile("^email\\s+([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+)$");
	private static String previousLine = "";

	static boolean updateMedicalRecordbyInputLine(MedicalRecord medicalRecord,
			String line, Scanner scanner) {
		Matcher nameMatcher = namePattern.matcher(line);
		Matcher birthdayMatcher = birthdayPattern.matcher(line);
		Matcher phoneMatcher = phonePattern.matcher(line);
		Matcher addressMatcher = addressPattern.matcher(line);
		Matcher emailMatcher = emailPattern.matcher(line);
		if (nameMatcher.matches()) {
			medicalRecord.setName(nameMatcher.group(1));
		} else if (birthdayMatcher.matches()) {
			medicalRecord.setBirthday(birthdayMatcher.group(1));
		} else if (phoneMatcher.matches()) {
			medicalRecord.setPhone(Integer.parseInt(phoneMatcher.group(1)));
		} else if (addressMatcher.matches()) {
			medicalRecord.setAddress(addressMatcher.group(1));
			if (scanner.hasNextLine()) {
				line = scanner.nextLine();
				previousLine = line;
			}
			else {
				return true;
			}
			Matcher addressMatcherAdditional = addressPatternAdditional
					.matcher(line);
			while (addressMatcherAdditional.matches()) {
				medicalRecord.setAddress(medicalRecord.getAddress()
						+ addressMatcherAdditional.group(1));
				if (!scanner.hasNextLine())
					break;
				line = scanner.nextLine();
				previousLine = line;
				addressMatcherAdditional = addressPatternAdditional
						.matcher(line);
				
			}

			return false;

		} else if (emailMatcher.matches()) {
			medicalRecord.setEmail(emailMatcher.group(1));
		}
		return true;
	}

	public static void main(String[] args) {

		ArrayList<MedicalRecord> medicalRecordList = new ArrayList<MedicalRecord>();
		Scanner scanner = new Scanner(System.in);
		String line = "";

		while (scanner.hasNextLine()) {

			while (line.equals("")) {
				if (!scanner.hasNextLine())
					break;
				line = scanner.nextLine();
			}
			MedicalRecord medicalRecord = new MedicalRecord();
			while (!line.equals("")) {
				if (updateMedicalRecordbyInputLine(medicalRecord, line, scanner)) {
					if (!scanner.hasNextLine())
						break;
					line = scanner.nextLine();
				}
				else {
					line = previousLine;
					previousLine = "";
				}
				
			}
			System.out.println(medicalRecord);
			medicalRecordList.add(medicalRecord);

		}

		scanner.close();
		System.out.println(medicalRecordList);
	}

}
