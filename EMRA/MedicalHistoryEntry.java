package EMRA;

public class MedicalHistoryEntry {
	private String diagnosisInformation;
	private String dateOfDiagnosis;
	
	public String getDiagnosisInformation() {
		return diagnosisInformation;
	}
	public void setDiagnosisInformation(String diagnosisInformation) {
		this.diagnosisInformation = diagnosisInformation;
	}
	public String getDateOfDiagnosis() {
		return dateOfDiagnosis;
	}
	public void setDateOfDiagnosis(String dateOfDiagnosis) {
		this.dateOfDiagnosis = dateOfDiagnosis;
	}
	
	@Override
	public String toString() {
		return "MedicalHistoryEntry [diagnosisInformation="
				+ diagnosisInformation + ", dateOfDiagnosis=" + dateOfDiagnosis
				+ "]";
	}
	
	
}
