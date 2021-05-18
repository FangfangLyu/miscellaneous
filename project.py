import csv
 
fields = ['LastName','FirstName', 'Grade','PassOrFail']

rows = []
filename = "gradebookhere.csv"

#use to determine PassOrFail
passOrfail=input("What is a passing grade in your course\n:")

inputType=input("Is the inputted score numerical value? Y/N\n:")
if (inputType.upper() == "Y" or inputType.upper()=="YES"):
    inputType = "number"
else:
    inputType = "none"

def askForRowP(judge,types): # judge is used to judge the pass or fail
    pof=""
    #first ask for all the input data, while used to determine if user entered empty stuff
    while True:             # Loop continuously
        lname=input("\tLast Name: ")   # Get the input
        if lname != "":       # If it is not a blank line...
            break           # ...break the loop
    while True:             # Loop continuously
        fname=input("\tFirst Name: ")   # Get the input
        if fname != "":       # If it is not a blank line...
            break           # ...break the loop
   
    if ( types =="number"):
        while True:             # Loop continuously
            try:
                grade=int(input("\tGrade:"))   # Get the input
                if grade != "" :       # If it is not a blank line...
                  break           # ...break the loop
            except ValueError:
                print("Enter a number: ")
        if grade>= int(judge):
            pof="Pass"
        else:
            pof="Fail"
    else:
            while True:             # Loop continuously
                grade=input("\tGrade:") # Get the input
                if grade != "" :       # If it is not a blank line...
                    break           # ...break the loop
    
    print("Name: " + fname+" "+lname+ ", Grade: " + str(grade)+ ", "+pof)
       
    return [lname,fname,grade,pof]
    
i=1
while(True):
    inputrow=[]
    print("Student "+str(i)+":")
    rows.append(askForRowP(passOrfail,inputType))

    if(input("Press Enter to Continue. Type anything to stop\n: ")!=""):
        break
    print()
    i+=1
    
    
with open(filename,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(fields)
    
    csvwriter.writerows(rows)
   
print()
for i in range(len(fields)):
    print(fields[i],end="\t")
print()
for i in range(len(rows)):
    for e in range(len(rows[i])):
        print(rows[i][e],end="\t")
    print()
    
	