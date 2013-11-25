import java.util.Observable;
import java.util.Observer;

class MessageBoard extends Observable {
 
  public void changeMessage(String message) {
    setChanged();
    notifyObservers(message);
  }

  public static void main(String[] args) {
    MessageBoard board = new MessageBoard();
    Student bob = new Student();
    Student joe = new Student();
    Teacher liu = new Teacher();
    board.addObserver(bob);
    board.addObserver(joe);
    board.addObserver(liu);
    board.changeMessage("More Homework!");
  }
}

class Student implements Observer {
  public void update(Observable o, Object arg) {
    System.out.println("Message board changed: " + arg);
  }
}
class Teacher implements Observer{
	public void update(Observable o, Object arg){
		System.out.println("The students get notified!");
	}
}
