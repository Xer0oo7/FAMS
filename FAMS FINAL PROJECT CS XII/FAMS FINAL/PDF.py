import mysql.connector
from fpdf import FPDF
import webbrowser
import csv

def PDF():
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


  query = f"SELECT * FROM {current_user[0]}_expense"
  mycursor.execute(query)
  data = mycursor.fetchall()


  
 


  PAGE_WIDTH = 210
  PAGE_HEIGHT = 297
  MARGIN = 10
 
  col_widths = [30, 30, 30, 30]   
  row_height = 10

 
  table_width = sum(col_widths) + (len(col_widths) - 1) * MARGIN
 
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size=12)

  logo_path = 'dash.png'
  logo_x = 75
  logo_y = 0
  logo_width = 50
  logo_height = 0

  pdf.image(logo_path, x=logo_x, y=logo_y, w=logo_width, h=logo_height)

  table_x = 10
  table_y = 50

  pdf.set_xy(table_x, table_y)

 
  pdf.cell(col_widths[1] + MARGIN, row_height, "SL_NO", border=0)
  pdf.cell(col_widths[1] + MARGIN, row_height, "EXPENSE", border=0)
  pdf.cell(col_widths[1] + MARGIN, row_height, "DATE", border=0)
  pdf.cell(col_widths[1] + MARGIN, row_height, "CATEGORY", border=0)

  pdf.ln()

 
  for row in data:
    pdf.cell(col_widths[0], row_height, str(row[0]), border=1)
    pdf.cell(col_widths[1] + MARGIN, row_height, str(row[1]), border=1)
    pdf.cell(col_widths[2] + MARGIN, row_height, str(row[2]), border=1)
    pdf.cell(col_widths[3] + MARGIN, row_height, str(row[3]), border=1)
    pdf.ln()

 
  pdf_file = "Expenses.pdf"
  pdf.output(pdf_file)

 
  mydb.close()


  webbrowser.open_new(pdf_file)
