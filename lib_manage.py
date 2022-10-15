import csv 
import os
import datetime

def heading():
  with open("Library.csv","w",newline = "") as f:
    fwriter = csv.writer(f)
    fwriter.writerow(['Book Name', 'Book Author', 'Genre', 'Availibility', 'Issued by', 'Issued on','Return Date'])
    print("Heading is added to the file")

def input_record():
  with open("Library.csv","a",newline = "") as f:
    fwriter = csv.writer(f)
    ans = 'yes'
    while ans in 'yes':
      book_name = input ("Enter the name of the book : ")
      book_author = input ("Enter the author of the book : ")
      book_genre = input ("Enter the genre of the book : ")
      book_status = "Available"
      book_issued = "N/A"
      book_issue_date = "N/A"
      book_return_date = "N/A"
      record = [book_name,book_author,book_genre,book_status,book_issued,book_issue_date,book_return_date]
      fwriter.writerow(record)
      ans = input("Do you want to enter more records (yes/no) : ")
      ans = ans.lower()

def display_record():
  with open("Library.csv","r") as f:
    freader = csv.reader(f)
    for record in freader:
      print(record)

def display_author():
  with open("Library.csv","r") as f:
    freader = csv.reader(f)
    data = []
    for record in freader:
      data.append(record)
    search = input("Enter the name of author you want to search : ")
    for i in range(1,len(data)):
      if (data[i][1].lower() == search.lower()):
        print(data[i])

def display_genre():
  with open("Library.csv","r") as f:
    freader = csv.reader(f)
    data = []
    for record in freader:
      data.append(record)
    search = input("Enter the genre of the book you want to search : ")
    for i in range(1,len(data)):
      if (data[i][2].lower() == search.lower()):
        print(data[i])

def delete_record():
  bname = input ("Enter the book of name you want to remove : ")
  ifile = open("Library.csv","r")
  ofile = open("Temp.csv","w",newline = "")
  owriter = csv.writer(ofile)
  ireader = csv.reader(ifile)
  data = []
  for record in ireader():
    data.append(record)

  owriter.writerow(data[0])
  for i in range(1,len(data)):
    if (data[i][0].lower() == bname.lower):
      pass
    else:
      owriter.writerow(data[i])
  ifile.close()
  ofile.close()
  os.remove("Library.csv")
  os.rename("Temp.csv","Library.csv")

def check_availability():
  with open("Library.csv","r") as f:
    freader = csv.reader(f)
    data = []
    book = []
    for record in freader:
      data.append(record)
    for record in freader:
      book.append(record[0].lower())
    book_search = input("Enter the name of book : ")
    if book_search.lower() not in book:
      print("%s is not available" %book_search)
    for i in range(1,len(data)):
      if (data[i][0].lower() == book_search.lower()):
        if (data[i][3] == "Available"):
          print("%s is available!" %book_search)
          break
        else:
          print("Sorry! %s is issued by someone else" %book_search)
          break
      else:
        continue

def issue_book():
  with open("Library.csv","r") as f:
    newfile = []
    book_name = input("Enter the name you want to issue : ")
    issue_name = input("Enter the ID of student : ")
    freader = csv.reader(f)
    data = []
    for record in freader:
      data.append(record)
    for i in range(len(data)):
      if data[i][0].lower() == book_name.lower():
        data[i][3] = "Not available"
        data[i][4] = issue_name
        data[i][5] = datetime.date.today()
        data[i][6] = datetime.date.today() + datetime.timedelta(days=7)
      newfile.append(data[i])

      with open("Library.csv","w",newline = "") as f:
        fwriter = csv.writer(f)
        for record in newfile:
          fwriter.writerow(record)
        print("The system is updated !!")

def student_user():
  opt = 'yes'
  while opt in 'yes':
    print("Enter 1 for list of all the books ")
    print("Enter 2 for searching the books of a particular author")
    print("Enter 3 for searching the books of a particular genre")
    print("Enter 4 for checking the availabilty of the book")
    choice = int(input("Select the menu "))
    if choice == 1:
      display_record()
    elif choice == 2:
      display_author()
    elif choice == 3:
      display_genre()
    elif choice == 4:
      check_availability()
    else:
      print("Enter a valid number")
    opt = input("Do you want to continue (yes/no) : ")
    opt = opt.lower()

def manager_user():
  opt = 'yes'
  while opt in 'yes':
    print("Enter 1 for writing the heading ")
    print("Enter 2 for writing the records ")
    print("Enter 3 for printing all the record ")
    print("Enter 4 for searching the books of a particular author")
    print("Enter 5 for searching the books of a particular genre")
    print("Enter 6 for deleting a record")
    print("Enter 7 for issuing the book and updating the records")
    choice = int(input("Select the menu "))
    if choice == 1:
      heading()
    elif choice == 2:
      input_record()
    elif choice == 3:
      display_record()
    elif choice == 4:
      display_author()
    elif choice == 5:
      display_genre()
    elif choice == 6:
      delete_record()
    elif choice == 7:
      issue_book()
    else:
      print("Enter a valid number")
    opt = input("Do you want to continue (yes/no) : ")
    opt = opt.lower()

user = input("Enter your designation (Manager/Student) : ")
if (user.lower() == 'manager'):
  manager_user()
elif (user.lower() == 'student'):
  student_user()
