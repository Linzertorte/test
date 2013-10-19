package EMRA;
import java.util.ArrayList;
public class MedicalRecord {
	private String name;
	

	private String birthday;
	private int phone;
	private String address;
	private String email;
	private ArrayList<MedicalHistoryEntry> medicalHistory;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getBirthday() {
		return birthday;
	}

	public void setBirthday(String birthday) {
		this.birthday = birthday;
	}

	public int getPhone() {
		return phone;
	}

	public void setPhone(int phone) {
		this.phone = phone;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public ArrayList<MedicalHistoryEntry> getMedicalHistory() {
		return medicalHistory;
	}

	public void setMedicalHistory(ArrayList<MedicalHistoryEntry>  medicalHistory) {
		this.medicalHistory = medicalHistory;
	}
	@Override
	public String toString(){
		String medicalHistoryString="";
		if(medicalHistory==null) medicalHistoryString="\t\tNone";
		else {
			for(MedicalHistoryEntry medicalHistoryEntry:medicalHistory){
				medicalHistoryString += "\t\t\t\t" + medicalHistoryEntry.toString();
			}
		}
		return "name\t\t\t\t" + name + "\nbirthday\t\t\t" + birthday
				+ "\nphone\t\t\t\t" + phone + "\naddress\t\t\t\t" + address + "\nemail\t\t\t\t"
				+ email + "\nmedicalHistory" + medicalHistoryString + "\n";
	}
	/*public String toString() {
		return "MedicalRecord [name=" + name + ", birthday=" + birthday
				+ ", phone=" + phone + ", address=" + address + ", email="
				+ email + ", medicalHistory=" + medicalHistory + "]";
	}*/
	
}
