import mic as m
from  PIL import ImageTk,Image
import datetime
from plyer import notification
import requests
import csv

with open('record.csv', 'r') as file:
    reader = csv.reader(file)
    first_row = next(reader)
    
host = first_row[0]
user_name = first_row[1]
passwd = first_row[2]

def fams():
    list = ['Housing', 'Transportation', 'Food', 'Personal care', 'Entertainment', 'Travel', 'Education', 'Debt payments', 'Savings', 'Miscellaneous']
    pdflist = ['CSV','PDF']
    tablename= ['expense','temporary_source_of_income']
    time = m.time()
    
    sql  = m.sql(x = host, y = user_name,z = passwd)
    user = sql.user()
    hmm  = sql.mycursor.fetchall()
    print(hmm)
    sql.create_monthly_goals_table()
    

    d1 = m.window('FAMS','2000x2100+0+0')

    bind = d1.create_window()
    tag = d1.create_tab()
    d1.create_frame()

    dash     = d1.create_add_tab_in_tab_view('DASHBOARD')
    goal     = d1.create_add_tab_in_tab_view('BUDGET')
    expense  = d1.create_add_tab_in_tab_view('EXPENSE TRACKER')
    settings = d1.create_add_tab_in_tab_view('EXPORT')
    about    = d1.create_add_tab_in_tab_view('ABOUT')

    logo = ImageTk.PhotoImage(Image.open('dash.png'))
    d1.create_label_image(master = dash,image = logo,anchor = 'center')

    time_label = d1.create_label(dash,font = ('arial',25,'bold'),x = 400,y = 0,)
    def update_time():
        now                 = datetime.datetime.now()
        then                = datetime.date.today()
        date                = then.strftime("%d/%m/%Y")
        time_in_12hr_format = now.strftime("%I:%M:%S %p")
        time_label.configure(text = date+'  '+time_in_12hr_format,)
        time_label.after(1000,update_time)
    update_time()

    def expense_graph():
        sql.plot()

    def expense_pie():
        sql.pie()

    frame5 = d1.create_frame(master = dash,x = 20 ,y = 100,width = 250, height = 200,border_width = 5,corner=15)
    d1.create_button(master = frame5,text  = 'EXPENSE GRAPH',command = expense_graph,x = 10 , y = 130,height= 50,width = 230,corner = 5)
    d1.create_label(master = frame5,width = 240 ,height = 100,x = 5,y = 10,text = 'TOTAL EXPENSE\nPER DAY'
                    ,text_color='#f25',corner=15,bg_color='white')
    
    frame6 = d1.create_frame(master = dash ,width = 250, height = 200,border_width = 5,corner=15,x = 800, y =  100)
    d1.create_button(master = frame6,text  =   'EXPENSE\nPIECHART',command= expense_pie,x = 10 , y = 130,height =50,width = 230,corner = 5)
    d1.create_label(master = frame6,width = 240 ,height = 100,x = 5,y = 10,text = '  EXPENSE\nPIECHART'
                    ,text_color='#f25',corner=15,bg_color='white')
    
    def insert_expense():
        if time.connection() and date1.cget('state') == 'disabled':
            exp = expensive.get()
            dat = time.current_date()
            cat = category_option.get()
            sql.create_expense_table()

            query = 'select sl_no from {}_expense '.format(user)
            sql.mycursor.execute(query)
            data = sql.mycursor.fetchall()

            if len(data) == 0:
                sql.insert_expense(expense=exp,date=dat,category=cat)
                notification.notify(title = "FAMS",message= " Dear user your expense {} has been added successfully".format(exp),timeout=10)
        
            else:
                for i in max(data):
                    x = i
        
                sql.insert_expense(expense = exp,date=dat,sl = x+1 ,category=cat)
                notification.notify(title = "FAMS",message= " Dear user your expense {} has been added successfully".format(exp),timeout=10)
     
        else:
            exp = expensive.get()
            dat = time.scramble(date1.get())
            cat = category_option.get()
            sql.create_expense_table()

            query = 'select sl_no from {}_expense '.format(user)
            sql.mycursor.execute(query)
            data = sql.mycursor.fetchall()

            if len(data) == 0:
                sql.insert_expense(expense=exp,date=dat,category=cat)
                notification.notify(title = "FAMS",message= " Dear user your expense {} has been added successfully".format(exp),timeout=10)
        
            else:
                for i in max(data):
                    x = i
        
                sql.insert_expense(expense = exp,date=dat,sl = x+1 ,category=cat)
                notification.notify(title = "FAMS",message= " Dear user your expense {} has been added successfully".format(exp),timeout=10)
            
    def disable1():
        date1.configure(state = 'normal')

    astetic_frame1 = d1.create_frame(master = expense,x = 380 , y = 10,width = 350 , height = 300,corner = 48)
    frame1 = d1.create_frame(master = expense,width = 500,height = 370,corner = 15,x =  310, y = 70)
    d1.create_label(astetic_frame1,text = 'EXPENSE TRACKER',font = ('arial',30 ),x = 30,y = 20,corner= 67)
    d1.create_label(master = frame1,text_color = '#07ffda',font = ('arial',30),bg_color = '#2C2C2C',text = 'EXPENSE        :',x = 10 , y = 20)
    d1.create_label(master = frame1,text_color = '#07ffda',font = ('arial',30),bg_color = '#2C2C2C',text = 'DATE',x = 10 , y = 73)
   
    d1.create_label(master = frame1, text = 'CATEGORY     :',font = ('arial',30),bg_color = '#2C2C2C',x = 10 , y = 126)

    d1.create_button(master = frame1,text='INSERT',height = 150,width = 480,x = 10, y = 200,command=insert_expense)
    d1.create_button(master = frame1,text='ENTER MANUALLY',x = 100 , y = 79,command=disable1,width = 0 ,height = 0)
    expensive = d1.create_entry(frame1,font = ('arial',15,'bold'),fg_color='white',text_color='black',corner=48,width = 250,x = 240 , y = 25)
    date1    = d1.create_entry(frame1,font = ('arial',15,'bold'),fg_color='white',text_color='black',corner=48,width = 250,x = 240 , y = 78,state = 'disabled')
    category_option=  d1.create_option_menu(master = frame1,values = list,x = 240, y = 126,command = None,width = 250)
 
    def reset():
        query = f'delete from {user}_monthly_goals'
        sql.mycursor.execute(query)
        sql.mydb.commit()
        check()
         
    def insert_monthly_goal():
        monthly      = monthly_goal.get()
        from_monthly = from_monthly_goal.get()
        to_monthly   = time.scramble(time.autocompete_date(from_monthly))
        from_monthly = time.scramble(from_monthly)
        sql.create_monthly_goals_table()
        sql.insert_monthly_goal(from_monthly,to_monthly,monthly)
        month_goal_button.configure(state = 'disabled')
        notification.notify(title = "FAMS",message= " Dear user your monthly goal of  {} has been added successfully".format(monthly),timeout=10)
     
    astetic_frame2 = d1.create_frame(master = goal,x = 365 , y = 13,width = 350 , height = 300,corner = 48)
    d1.create_label(astetic_frame2,text = 'MONTHLY BUDGET',font = ('arial',30 ),x = 35,y = 20,corner= 67)
    frame2 = d1.create_frame(master = goal,width = 1100,height = 500,corner = 15,x = 0 , y = 70,fg_color=None)
    d1.create_label(master = frame2,text_color = '#07ffda',font = ('arial',30),bg_color = '#2C2C2C',text = 'EXPECTED MONTHLY EXPENDITURE:',x = 10 , y = 20)
    d1.create_label(master = frame2,text_color = '#07ffda',font = ('arial',30),bg_color = '#2C2C2C',text = 'FROM ',x = 10 , y = 70)

    next_monthly_goal = d1.create_label(master = frame2,text_color = '#07ffda',bg_color = '#2C2C2C',font = ('arial',15)
                                    ,text = 'YOU CAN SET YOUR NEXT\n MONTHLY BUDGETON:\nDD/MM/YYYY',x = 470 , y = 115,height=345,width = 600)
    
    
    monthly_goal      = d1.create_entry(frame2,font = ('arial',15,'bold'),fg_color='white',text_color='black',corner=48,width = 525,x = 550 , y = 25)
    from_monthly_goal = d1.create_entry(frame2,font = ('arial',15,'bold'),fg_color='white',text_color='black',corner=48,width = 525,x = 550, y = 75)


    month_goal_button= d1.create_button(master = frame2,text='SET MONTHLY GOAL',width = 450,height = 165,x = 10 , y = 115,command = insert_monthly_goal)

    reset_monthly_goal_button = d1.create_button(master = frame2,text='RESET MONTHLY GOAL',width = 450,height = 165,x = 10 , y = 295,command=reset)

    def check():
        query = f'select * from {user}_monthly_goals'
        sql.mycursor.execute(query)
        x = sql.mycursor.fetchall()
        if len(x) > 0:
            month_goal_button.configure(state = 'disabled')
        else:
            month_goal_button.configure(state = 'normal')
    check()

    def update1():
        x = sql.select_monthly_goal_label()
        x = x.replace('-','/')
        x = time.scramble_yyyy_mm_dd(x)
        next_monthly_goal.configure(text = f'YOU CAN SET YOUR NEXT\nMONTHLY BUDGET GOAL ON:\n{x}' )
        next_monthly_goal.after(1000,update1)
    update1()
 
    def delete_monthly_goals():
        query = f'select * from {user}_monthly_goals'
        sql.mycursor.execute(query)
        x = sql.mycursor.fetchall()
        if len(x) != 0:
            if time.current_date() == x[0][0]:
                y = sql.mycursor.fetchall()
                sql.delete_monthly_goals()
    
        next_monthly_goal.after(5000,update1)

    exceeded_label = d1.create_label(master = dash,x = 80 , y = 480)


    def has_the_monthly_goal_been_exeeded_by_expense():
        query = f'select goal_money from {user}_monthly_goals'
        sql.mycursor.execute(query)
        goal = sql.mycursor.fetchone()[0]
        query = f'select sum(expense) from {user}_expense'
        sql.mycursor.execute(query)
        exp= int(sql.mycursor.fetchone()[0])
        if isinstance(exp,int) :
            print('x')
            if exp>goal:
                exceeded_label.configure(text = '" Dear user your expense has exceeded user monthly goal.kindly cut down spending🤑🤑!!"')
                notification.notify(title = "FAMS",message= " Dear user your expense has exceeded user monthly goal.Kindly cut down spending😁😉!!",timeout=10)
                exceeded_label.after(1500000,has_the_monthly_goal_been_exeeded_by_expense)
            
        else:
            pass

    if time.connection():
        delete_monthly_goals()
        
 

    def pdf():
        if csvorpdf.get() == 'PDF':
            import PDF
            PDF.PDF()

        else:
            import csvproducer as c
            c.produce()


    frame4 = d1.create_frame(master = settings,width = 500,height = 150,corner = 15,x =  300, y = 70)
    d1.create_label(master = frame4,text='EXPORT EXPENSE FILE',x = 125 , y = 10,bg_color='#2C2C2C')
    csvorpdf = d1.create_option_menu(master = frame4,values = pdflist,x = 80, y = 60,command = None)
    export  = d1.create_button(master  = frame4,x = 320, y = 60,command = pdf,text = 'EXPORT',width = 120,height = 30)


    

    display1 = '''ABOUT\n\n\nADITYASHANKARPS\nAKSHAY\nPRAVEEN\nDEVANANDAN'''

    about_frame = d1.create_frame(master = about,x = 380 , y = 10,width = 350 , height = 500,corner = 48,fg_color='#5D5C5C')


    error404 = d1.create_label(master = about_frame,text = display1
                            ,x = 53, y = 0,fg_color='#2C2C2C',text_color='white',height = 350,corner = 15)



    def end(x):
        sql.mycursor.execute('delete from checked')
        sql.close()
        bind.destroy()



    bind.bind('<Escape>',end)
    d1.end()

    sql.mycursor.execute('delete from checked')
    sql.close()

