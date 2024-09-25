# file "accdata.dat"
import pickle
x=[{"accno":"1000","name":"soman","amt":12345,"pin":"1001"},{"accno":"2000","name":"sasi","amt":100,"pin":"2002"},{"accno":"3000","name":"gabru","amt":5600001,"pin":"3003"}]
f=open("accdata.dat","wb")
for i in range(3):
  pickle.dump(x[i],f)
f.close()

# to view file
k=open("accdata.dat","rb")
try:
  while True:
    print(pickle.load(k))
except EOFError:
  pass
k.close()

#data extractor
def data():
  data=[]
  with open("accdata.dat","rb") as f:
    while True:
      try:
        data.append(pickle.load(f))
      except EOFError:
        break
  return data
#print(data())

#menu
while True:
  print("\n**************************************")
  print("**Welcome to Banking Management tool**")
  print(" 1: Create account \n 2: Deposit money \n 3: Withdraw money \n 4: Update pin \n 5: View account \n 6: Search acount \n 7: Delete account \n 8: Exit")
  c=input("Enter the choice: ")
  print()
  if c=="1":
    create()
  elif c=="2":
    deposit()
  elif c=='3':
    withdraw()
  elif c=='4':
    updatepin()
  elif c=='5':
    view()
  elif c=='6':
    search()
  elif c=='7':
    delete()
  elif c=='8':
    print("Thank you, See you again soon..")
    print("=======================================")
    break
  else:
    print("Invalid response, Please try again")

#create
import pickle
def create():
  rec=data()
  print("***********Create Account***********")
  while True:
    query="n"
    accno=input("Enter account no: ")
    for i in rec:
      if i["accno"]==accno:
        print("Account already exists, Please try again")
        query="y"
        break
    if query!="y":
      name=input("Enter the customer name: ")
      pin=input("Enter the pin: ")
      amt=float(input("Enter the amount: "))
      rec.append({"accno":accno,"name":name,"amt":amt,"pin":pin})
      print("***********Account Created**********")
      print("""
If you need to add another account enter y for yes
and n for no!""")
      query=input("Enter here: ")
      if query[0].lower()=="n":
        break
  with open("accdata.dat","wb") as nf:
    for i in rec:
      pickle.dump(i,nf)
  print('''
******Thanks for creating acount(s)******''')
create()

#deposit
import pickle
def deposit():
  print("***********Deposit Money***********")
  accno=input("Enter the account no: ")
  pin=input("Enter the pin: ")
  rec=data()
  for i in rec:
    if i["accno"]==accno:
      if i["pin"]==pin:
        amt=abs(float(input("Enter amount: ")))
        i["amt"]+=amt
        print("\n Transaction Successful,\n Amount deposited:",amt,"/-")
      else:
        print("\nIncorrect pin, Please try again")
      break
  else:
    print("\nAccount not found, Please try again")
  with open("accdata.dat","wb") as nf:
    for i in rec:
      pickle.dump(i,nf)
  print("====================================")
deposit()

#withdraw
import pickle
def withdraw():
  print("***********Withdraw Money***********")
  accno=(input("Enter the account no: "))
  pin=input("Enter the pin: ")
  rec=data()
  for i in rec:
    if i["accno"]==accno:
      if i["pin"]==pin:
        amt=abs(float(input("Enter amount: ")))
        if i["amt"]-amt>=0:
          i["amt"]-=amt
          print("\n Transaction Successful,\n Amount withdrawed:",amt,"/-")
        else:
          print("\n Transaction Unsuccessful,\n Not enough balance")
      else:
        print("\nIncorrect pin, Please try again")
      break
  else:
    print("\nAccount not found, Please try again")
  with open("accdata.dat","wb") as nf:
    for i in rec:
      pickle.dump(i,nf)
  print("====================================")
withdraw()

# View
import pickle
def view():
  print("***********View Account***********")
  rec=data()
  accno=input('Enter the account no: ')
  pin=input('Enter the pin: ')
  for i in rec:
    if i["accno"]==accno:
      if i["pin"]==pin:
        print("\n***********Account Info***********")
        print(" Account No.:\t",i['accno'],"\n Name:\t\t",i["name"],"\n Balance:\t",i["amt"])
      else:
        print("\nIncorrect pin, Please try again")
      break
  else:
    print("\nAccount not found, Please try again")
  print("==================================")
view()

#update pin
import pickle,re
def updatepin():
  print("************Update Pin*************")
  accno=input("Enter the account no: ")
  pin=input("Enter the pin: ")
  rec=data()
  for i in rec:
    if i["accno"]==accno:
      if i["pin"]==pin:
        print("\nPin should contain 4 digits")
        npin=input("Enter new pin: ")
        conpin=input("Confirm new pin: ")
        if npin==conpin and re.match("^[0-9]{4}$",npin):
          i["pin"]=npin
          print("\n Successfully Updated pin")
        else:
          print("\nPins didn't match Or Invalid characters used,\nPlease try again")
      else:
        print("\nIncorrect pin, Please try again")
      break
  else:
    print("\nAccount not found, Please try again")
  with open("accdata.dat","wb") as nf:
    for i in rec:
      pickle.dump(i,nf)
  print("===================================")
updatepin()

#Search
def search():
  rec=data()
  print("***********Search Account***********\n 1:Account no \n 2:Account name")
  hm=input("Enter your choice: ")
  if hm=="1":
    accno=input("\nEnter account no: ")
    for i in rec:
      if i["accno"]==accno:
        print("\n***********Search Result************")
        print(" Account No.:\t",i['accno'],"\n Name:\t\t",i["name"])
        break
    else:
      print("\n***********Search Result************")
      print("Account not found")
  elif hm=="2":
    name=input("\nEnter account name: ")
    for i in rec:
      if i["name"].lower()==name.lower():
        print("\n***********Search Result************")
        print(" Account No.:\t",i['accno'],"\n Name:\t\t",i["name"])
        break
    else:
      print("\n***********Search Result************")
      print("Account not found")
  else:
    print("\n Invalid choice, Please try again")
  print("====================================")
search()

#delete
import pickle
def delete():
  print("***********Delete Account************")
  rec=data()
  accno=input('Enter the account no: ')
  pin=input('Enter the pin: ')
  for i in rec:
    if i["accno"]==accno:
      if i["pin"]==pin:
        rec.remove(i)
        print("\nAcount Deleted, Sorry to see you go..")
      else:
        print("\nIncorrect pin, Please try again")
      break
  else:
    print("\nAccount not found, Please try again")
  with open("accdata.dat","wb") as nf:
    for i in rec:
      pickle.dump(i,nf)
  print("=====================================")
delete()
