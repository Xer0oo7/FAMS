import mysql.connector
import csv

def produce():
   
  with open('record.csv', 'r') as file:
    reader = csv.reader(file)
    first_row = next(reader)

  mydb = mysql.connector.connect(
   host=first_row[0],
   user=first_row[1],
   password=first_row[2],
   database="financial",
  )

 
  mycursor = mydb.cursor(buffered=True)

  query = 'select * from checked'
  mycursor.execute(query)

  current_user = mycursor.fetchone()
  
  query1 = f"SELECT * FROM {current_user[0]}_expense"
 
 
  mycursor.execute(query1)

 
  result = mycursor.fetchall()

 
  csv_file_path = 'output.csv'
  field_names = [i[0] for i in mycursor.description]

 
  with open(csv_file_path, mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(field_names)  # write header row
     writer.writerows(result)  # write data rows


  import subprocess

  subprocess.run(['notepad', 'output.csv'])

 