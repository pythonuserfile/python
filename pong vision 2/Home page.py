import Tpg
import Opg
while True:
    
    f = input("Please enter the game type (T: double game, O: single game, case supported)")
    f.upper()
    if f != "":
  
        if f == "T":
            Tpg.sryx()
        elif f == "O":
            Opg.dryx()
        else:
            print("The input is not recognized. Please do not enter anything other than 't' and 'O'")


