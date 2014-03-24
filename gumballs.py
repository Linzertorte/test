class HasQuarterState:
    def __init__(self, gumballMachine):
        self.gumballMachine=gumballMachine
    def insertQuarter(self):
        print "You cannot insert another quarter"
    def ejectQuarter(self):
        print "Quarter returned"
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    def turnCrank(self):
        print "You turned..."
        self.gumballMachine.setState(self.gumballMachine.getSoldState())
    def dispense(self):
        print "No gumball dispensed"
    def __repr__(self):
        return "waiting for turn of crank"

class SoldState:
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print "Please wait, we're already giving you a gumball"
    def ejectQuarter(self):
        print "Sorry, you already turned the crank"
    def turnCrank(self):
        print "Turning twice doesn't get you another gumball"
    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount()>0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print "OOps, out of gumballs"
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
    def __repr__(self):
        return "dispensing a gumball"

class SoldOutState:
    def __init__(self,gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print "You can't insert a quarter, the machine is sold out"
    def ejectQuarter(self):
        print "You cannot eject, you have not inserted a quarter yet"
    def turnCrank(self):
        print "You turned, but there are no gumballs"
    def dispense(self):
        print "No gumball dispensed"
    def __repr__(self):
        return "sold out"


class NoQuarterState:
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    def insertQuarter(self):
        print "You inserted a quarter"
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
    def ejectQuarter(self):
        print "You haven't inserted a quarter'"
    def turnCrank(self):
        print "You turned, but there is no quarter"
    def dispense(self):
        print "You need to pay first"
    def __rep__(self):
        return "waiting for quarter"

class GumballMachine:
    def __init__(self,numberGumballs):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState= NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.count = numberGumballs
        self.state = self.soldOutState
        if numberGumballs > 0:
            self.state=self.noQuarterState
    def insertQuarter(self):
        self.state.insertQuarter()
    def ejectQuarter(self):
        self.state.ejectQuarter()
    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()
    def releaseBall(self):
        print 'A gumball comes rolling out the slot...'
        if self.count !=0:
            self.count -=1
    def getCount(self):
        return self.count
    def refill(self,count):
        self.count = count
        self.state = self.noQuarterState
    def setState(self,state):
        self.state = state
    def getState(self):
        return self.state
    def getSoldOutState(self):
        return self.soldOutState
    def getNoQuarterState(self):
        return self.noQuarterState
    def getHasQuarterState(self):
        return self.hasQuarterState
    def getSoldState(self):
        return self.soldState
    def __repr__(self):
        s=""
        s+="\nMighty Gumball, Inc."
        s+="\nJava-enabled Stating Gumball Model #2004"
        s+="\nInventory: "+str(self.count) +" gumball"
        if self.count!=1:
            s+="s"
        s+="\n"
        s+="Machine is "+str(self.state)+"\n"
        return s
    


gumballMachine=GumballMachine(5)
print gumballMachine
gumballMachine.insertQuarter();
gumballMachine.turnCrank();
print gumballMachine
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.insertQuarter()
gumballMachine.turnCrank()
print gumballMachine
