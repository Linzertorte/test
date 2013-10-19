package EMRA;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class EMR {

	/**
	 * @param args
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args) throws FileNotFoundException {
		File medicalRecordsFile = new File(args[0]);
		ArrayList<MedicalRecord> medicalRecordList= MedicalRecordsParser.parse(medicalRecordsFile);
		//System.out.println(medicalRecordList);
		PrintWriter writer = new PrintWriter("report.txt");
		for(MedicalRecord medicalRecord: medicalRecordList){
			System.out.println(medicalRecord);
			writer.println(medicalRecord);
		}
		writer.close();
	}

}
