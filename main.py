 #Libraries
import mysql.connector as con

#Database Connection
mycon = con.connect(host="localhost",user="root",password="1234",database="supersales")

#Database Connectivity Check
if mycon.is_connected():
    print("Connection Successful")

#functions

#function to check stock availability
def CheckStock():

  code = int(input("Code: "))
  query = "select quantity from stock where code={}".format(code)
  cursor.execute(query)
  quantity = cursor.fetchall()

  query2 = "select name from stock where code={}".format(code)
  cursor.execute(query2)
  name = cursor.fetchall()
    
  print("\n You checked stock for product code no."+str(code))

  print("Product is: "+name[0][0])
  if quantity<=10:
    print("Stock Limited!")
  elif quantity==1:
    print("1 left. Hurry up!")
  elif quantity>10:
    print("Stock Available!")
  else:
    print("Out of Stock!")

#function to print product description
def productDesc():

  code = int(input("Code: "))
  query = "select quantity from stock where code={}".format(code)
  cursor.execute(query)
  quantity = cursor.fetchall()

  query = "select name from stock where code={}".format(code)
  cursor.execute(query)
  name = cursor.fetchall()

  query = "select price from stock where code={}".format(code)
  cursor.execute(query)
  price = cursor.fetchall()

  query = "select description from stock where code={}".format(code)
  cursor.execute(query)
  desc = cursor.fetchall()

  print("\nProduct Details:")
  print("Product Code: "+str(code))

  print("Product name: "+str(name[0][0]))
  print("Quantity Available: "+str(quantity[0][0]))
  print("Price: Rs."+str(price[0][0]))
  print("Description: "+str(desc[0][0])+"\n")
    

#function to register a bill in the database
def registerABill():
    
  billNo = int(input("Bill no: "))
  date = input("Date(yyyy-mm-dd): ")
  products = input("Product codes: ")
  customer = input("Customer's username: ")
  operator = user
    
  query = "insert into bills values ({},'{}','{}','{}','{}')".format(billNo,date,products,customer,operator)
    
  cursor.execute(query)
  mycon.commit()
    
  print("Bill Registered!")
  return 1

#function to display an existing bill in the database
def displayBill():
    
  billNo = int(input("Enter Bill no: "))
  print("Showing bill: "+str(billNo))
    
  dateQuery = "select date from bills where billNo={}".format(billNo)
  cursor.execute(dateQuery)

  date = cursor.fetchall()
  print("Date of bill: "+str(date[0][0]))
    
  productQuery = "select codes from bills where billNo={}".format(billNo)
  cursor.execute(productQuery)
  products = cursor.fetchall()
  print("Products bought: "+str(products[0][0]))

  custQuery = "select customer from bills where billNo={}".format(billNo)
  cursor.execute(custQuery)
  cust = cursor.fetchall()
  print("Customer's username: "+str(cust[0][0]))

  userQuery = "select user from bills where billNo={}".format(billNo)
  cursor.execute(userQuery)
  operator = cursor.fetchall()
  print("Desk Operator: "+str(operator[0][0]))
    
#function to insert stock in database
def insertStock():
    
  code = int(input("Code: "))
  name = input("Name: ")
  quantity = int(input("Quantity: "))
  price = int(input("Price: "))
  desc = int(input("Description: "))
    
  query = "insert into stock values ({},'{}',{},{},'{}')" .format (code,name ,                quantity,price,desc)
  cursor.execute(query)
  mycon.commit()
    
  print("Insert successful!")
  return 1

#function to update stock in database
def updateStock():
    
  code = int(input("Enter product code: "))
  changedquantity = int(input("Enter updated quantity: "))
  changedprice = int(input("Enter changed price: "))
    
  query = "update stock set quantity={} where code={}".format(changedquantity,code)
  cursor.execute(query)
    
  query2 = "update stock set price={} where code={}".format(changedprice,code)
  cursor.execute(query2)
  mycon.commit()
    
  print("Update successful!")

#function to add reviews
def addReview():
    
  code = int(input("Enter product code: "))
  review = input("Add Review: ")
  rating = float(input("Rating(out of 5 and upto 1st decimal place): "))
    
  query = "insert into reviews values({},'{}',{},'{}')".format(code,review,rating,cusername)

  cursor.execute(query)
  mycon.commit()

  print("Review successfully added!")
  print("Thankyou for giving your honest review!")

#function to show a review added by users
def showReview():
    
  code = int(input("Enter product code: "))
    
  review = "select * from reviews where code={}".format(code)
  cursor.execute(review)
  result = cursor.fetchone()
    
  print("\nReview: "+str(result[1]))
  print("Rating: "+str(result[2]))

#function to show multiple reviews added by users
def showReviews():

  code = int(input("Enter product code: "))
    
  reviews = "select * from reviews where code={}".format(code)
  cursor.execute(reviews)
  result = cursor.fetchmany(10)
    
  for i in result:
    print("\n"+str(i))

#function to file complains
def lodgeComplain():

  print("Please keep your complain short and meaningful.")
  print("Also, enter correct contact no.")
  code = int(input("Enter product code: "))
  complain = input("Type your complain: ")
  suggestion = input("What do you expect: ")
  contact = input("Please enter your contact number: ")
    
  query = "insert into complains values ({},'{}','{}',{},'{}')".format(code,complain,suggestion,contact,cusername)
  cursor.execute(query)
  mycon.commit()

  print("Complain successfully added!")
  print("Thankyou for letting us resolve your issue.!")
  print("Sorry for the inconvinience. We will contact you ASAP.")

#function to order online
def orderonline():

  print("\nYou are ordering online......")
  print("Please make different orders for diferent product codes")

  orderno = int(input("\nEnter order number given by the desk operator: "))
  code = int(input("Enter product code: "))
  qty = int(input("Enter quantity: "))
  contact = int(input("Enter contact number: "))
  address = input("Enter delivery address: ")

  checkquery = "select quantity from stock where code={}".format(code)
  cursor.execute(checkquery)

  quant = cursor.fetchall()

    #check if product is in stock
  if quant[0][0]>= qty:

    pricequery = "select price from stock where code={}".format(code)
    cursor.execute(pricequery)
    price = cursor.fetchall()

    total = int(price[0][0])*qty

    status = "Order placed"
    orderquery = "insert into onlineorders values ({},'{}',{},{},{},'{}','{}',{})".format(orderno,cusername,code,qty,contact,address,status,total)
    cursor.execute(orderquery)
    mycon.commit()

    print("Order successfully Placed!")
    print("Please pay Rs. "+str(total)+" at the cash counter to confirm your order.")
        
  else:
    print("Product out of stock! Try again when product is in stock")

#function to show order to the employee
def showorders():

  status = "Order confirmed"

  stquery = "select * from onlineorders where status={}".format(status)
  cursor.execute(stquery)

  searchresult = cursor.fetchall()

  print(searchresult)

#function to confirm orders
def confirmOrder():

  status = "Order confirmed"
  orderno = int(input("Enter Order no: "))

  upquery = "update onlineorders set status={} where orderno={}".format(status,orderno)
  cursor.execute(upquery)
  mycon.commit()

  print(status)
    
        
#initials and login
print("Welcome to Super Sales Supermarket! \n ")
loginCondition = 1 #loop condition

#loop runs until the condition becomes false
while loginCondition:
    
  #check if the user is a customer or an employee
  print("\nDo you want to login as a customer or an employee")
  check = input("Enter 'c' for customer and 'e' for employee: ")

  if check=="c" or check=="C":
    print("\nLogin as a customer.")

    login = int(input("1. Have an existing account.\n2. New customer? Sign up.\n"))
    if login==1:
      cusername = str(input("\nEnter username: "))
      cpassword = str(input("Enter password: "))       
      cursor = mycon.cursor()
      query = "select name from customers where username='{}' and password='{}'".format(cusername,cpassword)
      cursor.execute(query)
      cname = cursor.fetchall()

      if cname==[]:
        print("\nOops! Wrong Creditionals. Try again!")
        continue
      else:
        print("\nLogin success!")
        print("logged in as "+str(cname[0][0]))
        loopCondition = 1 #loop condition

        while loopCondition:
          print("************************************************************************")
          print("\nWhat would you like to do?")
          print("1. Check Stock \n2. Product Description \n3. Add a product Review \n4. Show a product review\n5. Show multiple reviews \n6. Lodge a Complain \n7. Order online \n8. Logout")
          choice = int(input("\nEnter Operation: "))
          if choice==1:
            CheckStock()
                     
          elif choice==2:
            productDesc()
                     
          elif choice==3:
            addReview()
                     
          elif choice==4:
            showReview()
                     
          elif choice==5:
            showReviews()
                     
          elif choice==6:
            lodgeComplain()

          elif choice==7:
            orderonline()
                         
          elif choice==8:
            loopCondition = 0
                         
    elif login==2:
      print("\nSign Up as a new customer.")
      cusername = input("Enter username: ")
      cpassword = input("Enter password: ")
      cname =input("Enter name: ")
      dob = input("Enter DOB (yyyy-mm-dd): ")
      contact= int(input("Enter contact number: "))
      address= input("Enter address: ")
      cursor = mycon.cursor()
      query1 = "insert into customers values('{}','{}','{}','{}',{},'{}')".format(cusername,cpassword,cname,dob,contact,address)
      cursor.execute(query1)
      mycon.commit()

      querycheck = "select name from customers where contact={}".format(contact)
      cursor.execute(querycheck)
      result = cursor.fetchall()
      if result==[]:
        print("\nSignup unsuccessful!")
      else:
        print("\nSignup successful! Login.")
                
            
    else:
      print("\nInvalid Condition!")
  elif check=="e" or check=="E":
         
    #login creditionals
    username = str(input("\nEnter username: "))
    password = str(input("Enter password: "))
    
    cursor = mycon.cursor()
    query = "select user from users where username='{}' and password='{}'".format(username,password)
    cursor.execute(query)
    user = cursor.fetchall()

    if user==[]:
      print("Oops! Wrong Creditionals. Try again!")
      continue
    else:
      print("Login Success!")
      print("Logged in as "+str(user[0][0]))
      loopCondition = 1 #loop condition
        
      while loopCondition:
        print("What would you like to do?")
        print("1. Register a bill \n2. Display bill \n3. Insert stock \n4. update stock \n5. Check Stock \n6. Confirm Order \n7. Show orders \n8. Logout")
        choice = int(input("Enter Operation: "))
        if choice==1:
          registerABill()
                
        elif choice==2:
          displayBill()
                
        elif choice==3:
          insertStock()
                
        elif choice==4:
          updateStock()

        elif choice==5:
          CheckStock()

        elif choice==6:
          confirmOrder()

        elif choice==7:
          showorders()

        elif choice==8:
          loopCondition = 0

        else:
          print("Invalid Choice!\n")
  else:
    print("\nInvalid Choice!\n")
                
            
