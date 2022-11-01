# Heath Hilton
# 10/31/2022

# Program: Dean's List Checker
# Project M02 Case Study

# The program is to take in a list of students and their grades and determines whether they
# are on the Dean's List or Honor Roll.

# Declaring Global Variables to Use Throughout
fName = ""
lName = ""
sGPA = 0.0

# Basically the starter program that is looped through at every iteration.
def main():
  #Take in the student's last name and then determine if it is ZZZ.
  lName = str(input("Enter the student's last name or ZZZ to end: "))
  # Put all of the characters to uppercase and then test if it is ZZZ and end the program if it is.
  while lName.upper() != "ZZZ":
      # Program continues if the last name is real.
      continueProg(lName)
  else:
      quit()

# Take in the rest of the student info.
def continueProg(lName):
  fName = str(input("Enter the student's first name: "))
  sGPA = float(input("Enter the student's GPA: "))
  finalOutput(lName, fName, sGPA)

# Determine the grade rankings and display the results
def finalOutput(lName, fName, sGPA):
  if sGPA >= 3.5:
    print(lName + ",", fName + ": Dean's List with a", sGPA)
  elif sGPA >= 3.25 and sGPA < 3.5:
    print(lName + ",", fName + ": Honor Roll with a", sGPA)
  else:
    print(lName + ",", fName + ": ", sGPA)
  # Loop back to the main method to repeat.
  main()

# It starts
if __name__ == "__main__":
  main()