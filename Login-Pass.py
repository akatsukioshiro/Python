def mail():
  #function for Login Portal
	print("LOGIN PORTAL");
	id1=raw_input("Email ID : ");
	pass1=raw_input("Password : ");
	login(id1,pass1);

def login(id1,pass1):
    #ID PASSWORD checking function
    import time;
    f=open(id1+".txt","r");
    c=f.readlines()
    if(id1=='exit' or pass1=='exit'):
        print("\n\nExiting . . .");
        time.sleep(3);
        cls();
        print(">>> ================================ RESTART ================================");
        
    elif(id1==c[0].strip('\n') and pass1==c[1].strip('\n')):
        print("Login Successful");print("\n\nLoading . . .");
        time.sleep(3);
        access(id1);
    else :
        print("\nLogin Failed");
        time.sleep(13);
        cls();
        mains();

def cls():
  #Function to clear screen
	print(100*"\n");

def access(id1):
  #Welcome page
	print("Welcome to the PORTAL - "+id1+" !!!");
	lgt=raw_input("Logout ?(y) :");
	logout(lgt);

def logout(lgt):
  #Function to enable Logout
	if(lgt=="y" or lgt=="Y"):
		cls();
		mains();

def mains():
    #Main function that needs to be called for anything to start working
    print("Welcome to The PORTAL\n1. Create Account\n2. Login Portal");
    choice=raw_input("Option : ");
    if(choice=='1'):
        cls();
        create_acc();
    else :
        cls();
        mail();
        
def create_acc():
    #Account creation function
    import time;
    print("ACCOUNT REGISTRATION FORUM")    
    acc_id=raw_input("Email id : ");
    acc_pass=raw_input("Password : ");
    f=open(acc_id+".txt","w+");
    f.write(acc_id+"\n");
    f.write(acc_pass+"\n");
    f.close();
    time.sleep(3);
    mains();
