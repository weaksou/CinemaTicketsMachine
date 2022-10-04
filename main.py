import numpy as np
import pandas as pd
import datetime
import re
import functions as mf
data = np.array([0, 0, 0, 0, 0, 0])
data = data.reshape(3, 2)

newDate = datetime.datetime.now()
date = newDate.strftime("%x")

#buyTicket = int(input())
boughtTickets = 0
#bought Tickets Data Frame
obj = {
  "date":[],
  "name": [],
  "tickets":[],
  "refunded":[],
}
btDataFrame = pd.DataFrame(obj)
#btDataFrame.loc[len(btDataFrame.index)] = [date, 'amy pamy', 2, False]
#index = btDataFrame[btDataFrame["name"] == "Amy Pamy".lower()].index
#print(index)
#x = btDataFrame.loc[index, "refunded"] = True
#print(btDataFrame.iloc[0]["tickets"])


def buyTicket(name):
  global boughtTickets
  if len(data[data == 1]) == 6:
    print("Sorry, All seats are taken.")
    boughtTickets = 0
  elif len(data[data == 1]) + boughtTickets > data.size:
    b = len(data[data == 0])
    print("Sorry, Only {0} seat{1}".format(b, ("s are available." if b > 1 else " left.")))
    boughtTickets = 0
  else:
    btDataFrame.loc[len(btDataFrame.index)] = [date, name, boughtTickets, False] 
    a = "s" if boughtTickets > 1 else ""
    for x in range(len(data)):
      for i in range(len(data[x])):
        if boughtTickets > 0:
          if data[x][i] == 0: 
            data[x][i] = 1
            boughtTickets -= 1
    print("Thank you for your purchase, Please claim your ticket" + a)
    
def refund(num, name):
  tempNum = num
  if len(data[data == 1]) > 0 and len(data[data == 1]) >= tempNum:
    try:
        index = btDataFrame[btDataFrame["name"] == name.lower()].index
        btDataFrame.loc[index[0], "refunded"] = True
        if btDataFrame.iloc[index[0]]["refunded"]:
          if btDataFrame.iloc[index]["tickets"] >= num:
            for x in range(len(data)):
             for i in range(len(data[x])):
                if tempNum > 0:
                 if data[-x][-i] == 1: 
                    data[-x][-i] = 0
                    tempNum -= 1
            print(str(num) + " {0} has been refunded.".format("Ticket" if num == 1 else "Tickets"))
          else:
            print("Number of tickets to be refunded is incorrect ({0})".format(num))
    except IndexError:
       print("There was an error, Please check the Name. make sure its the name you bought tickets with, or enter: \"info\" to check the data for name")
  else:
    print("There isn't anything to refund!")
    
pattern = r"^.efund.\d+.\w+"

#wwhen the program starts
print("Type 'help' for available commands.")
while True:
  buyInput = input("Number of tickets: ")
  try:
    if buyInput == "reset":
     data[data == 1] = 0
     print("Empty seats has been reseted")
    elif buyInput == "info":
        #print(data)
        print(btDataFrame)

    elif buyInput == "shutdown":
        print("Goodbye.")
        break
    elif buyInput == "help":
        print("List of available commands: \n-default: number of tickets you want to buy (1, 2, 3... etc) \n-info: will return informations related to stored data (tickets, names, dates...) \n-refund: Syntax 'refund number name' (refund 1 alex) will refund a ticket that been purchased by alex, please make sure you enter the name correctly \n-reset: will reset seat count (use to mark seats as available again) \n-shutdown: stops the program")
    else:
      if re.match(pattern, buyInput):
        number = re.findall(r"\d+", buyInput)
        name = re.findall(r"\d+.+\w+", buyInput)
        print("Are you sure you want to refund {0} ticket{1} for \"{2}\", Yes or No?".format(int(number[0]), "" if int(number[0]) == 1 else "s", mf.refundName(name[0])))
        while True:
          answer = input().lower()
          if answer == "yes":
            refund(int(number[0]), mf.refundName(name[0]))
            break
          elif answer == "no":
            print("Sure.")
            break
          else:
            print("Sorry, Yes or No?")
      else:
        num = int(buyInput)
        name = input("Enter name: ")
        print("Are you sure you want to buy {0} ticket{1} for \"{2}\", Yes or No?".format(num, "" if num == 1 else "s", mf.upperName(name)))
        while True:
          answer = input().lower()
          if answer == "yes":
            boughtTickets += num
            buyTicket(name.lower().strip())
            break
          elif answer == "no":
            print("Sure.")
            break
          else:
            print("Sorry, Yes or No?")
        
  except ValueError:
    print("Please enter a valid number!")
  











