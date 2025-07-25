import  customtkinter as ctk
import mysql.connector as mysql
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import datetime
import calendar as c
import json
import requests

class window:

    def __init__(self,title,geo):
       self.title = title
       self.geo = geo
    
    def create_window(self):
        self.app = ctk.CTk()
        self.app.title(self.title)
        self.app.geometry(self.geo)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')
        return self.app

    def create_button(self,master,width = 150,height = 150,x = 0,y = 0,command = None,text = '',state = 'normal',corner = None,font = ('One Day ',15,'bold')):# commd default is none 
        button = ctk.CTkButton(master = master,width=width,height=height,command = command,text = text,state=state,corner_radius=corner,font = font)
        button.place(x = x , y = y)
        return button

    def create_frame(self,master = None,width = 0,height = 0 ,x = 0,y = 0,corner = 0 ,fg_color = None
                     ,relx = None,rely = None,anchor = None,border_width = None,border_color = None):# here note for frame if height and width is 0 then nothign will be shown
        self.frame = ctk.CTkFrame(master=master,width = width , height = height,corner_radius= corner 
                                  ,fg_color=fg_color,border_width=border_width,border_color=border_color)
        self.frame.place(x = x , y = y,relx=relx,rely = rely )
        return self.frame

    def create_label_image(self,master,image,anchor = None):# label for images
        label = ctk.CTkLabel(master = master,image=image,text='')
        label.pack(anchor = anchor)

    def create_label(self,master,width = 0,height = 0,text = '',font = ('One Day ',23,'bold')
                     ,bg_color = ('#303030'),x = 0 , y = 0,text_color = '#07ffda'
                     ,corner = 0,fg_color = None):
        label = ctk.CTkLabel(master = master,text = text, font = font , bg_color= bg_color,height = height,width = width,text_color=text_color
                            ,corner_radius = corner,fg_color=fg_color)
        label.place(x= x , y= y)
        return label

    def create_entry(self,master,width = 150,height =150,place_text = '',place_color = 'black',corner = 15
                     ,font = ('One Day ',15,'bold'),x = 0 ,y = 0,fg_color = 'white',show = None,text_color = 'Black',state = 'normal'):
        
        entry = ctk.CTkEntry(master = master,width = width,placeholder_text=place_text,placeholder_text_color=place_color
                             ,corner_radius=corner,font=font,fg_color=fg_color,show = show,text_color=text_color,state=state)
        entry.place(x = x ,y = y)

        return entry
    
    def create_tab(self,padx = 20 , pady = 7,width = 1200 , height = 680,corner = 50,text_color = '#07ffda'):
        self.tabview = ctk.CTkTabview(self.app,width = width,height = height,corner_radius = corner,text_color= text_color)
        self.tabview.pack(padx = padx, pady= pady)
        return self.tabview 
 
    
    def create_add_tab_in_tab_view(self,name = 'sample'):
        x = self.tabview
        y = x.add(name)
        return y
    
    def create_textbox(self,master ,fg_color='white',width  = 400 , height = 0,border_spacing= 30,border_width=3,corner=15
                          ,text_color= 'black',font = ('arial',15,'bold'),x= 240,y = 126):
        
        self.text = ctk.CTkTextbox(master = master,fg_color= fg_color,width  = width , height = height,border_spacing= border_spacing
                                   ,border_width=border_width,corner_radius=corner,text_color= text_color,font = font)
        self.text.place(x=x, y=y)
        return self.text
    
 
    def create_canvas(self,master,x = 0 ,y = 0):
        canvas = ctk.CTkCanvas(master = master)
        canvas.place(x=x,y=y)
        return canvas
    
    def create_option_menu(self,master,command,values=["option 1", "option 2"],x = 0,y = 0,dropdown_text_color = '#07ffda',width = 140,height = 28):
        option_menu = ctk.CTkOptionMenu(master = master,values=values,dropdown_text_color=dropdown_text_color,width=width,height=height)
        option_menu.place(x=x,y=y)
        return option_menu
    
    def create_toplevel(self):
        toplevel  = ctk.CTkToplevel()
        return toplevel





 



    def end(self):
        self.app.mainloop()

    def destroy(self):
        self.app.destroy()

class time:

    def __init__(self):
        pass

    def year(self):
        self.response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')
        self.data = json.loads(self.response.text)
        self.current_date = self.data["datetime"].split("T")[0]
        y = self.current_date 
        return y
    
    def current_time(self):
        self.response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')
        self.data = json.loads(self.response.text)
        self.current_time = self.data["datetime"].split("T")[1]
        y = str(self.current_time)[0:8]
        return y
    def autocompete_date(self,x):
        y = x[3:5]
        y = y.lstrip('0')
        print(y)
        stephen = c.monthrange(2023,int(y))# notice the year 2020
        arc = stephen[1]
        start_date_obj = datetime.datetime.strptime(x, '%d/%m/%Y')
        end_date_obj = start_date_obj + datetime.timedelta(days=arc)
        end_date = end_date_obj.strftime('%d/%m/%Y')
        return end_date
    
    def current_date(self):
        response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')
        if response.status_code == 200:
            data = response.json()
            current_date = data["datetime"].split("T")[0]
            return current_date
         
        
        else:
            print('Failed to fetch time:', response.status_code)

    def scramble(self,a):
        """used for converting date
           in the format dd/mm/yyyy
           to yyyy/mm/dd"""
        dat =  a
        x = dat[0:2]
        y = dat[3:6]
        z = dat[6:10] +'/'
        dat = z+y +x

        return dat

    def scramble_yyyy_mm_dd(self,a):#  
        
        """used for converting date
           in the format yyyy/mm/dd  
           to dd/mm/yyyy"""
        
        dat =  a
        x = '/'+dat[0:4]
        y = dat[4:7]
        z = dat[8:10] 
        dat = z+y+x

        return dat
    
    def connection(self):
        try:
            response = requests.get("https://www.google.com")
            return True
        
        except:
            return False
    
        


class sql:

    def __init__(self,x = 'localhost',y = 'root',z = 'pias_well'):
        
        self.mydb = mysql.connect(host = x,user= y ,passwd= z )
        self.mycursor = self.mydb.cursor(buffered=True)
        self.mycursor.execute('create   database if not exists financial')
        self.mycursor.execute('use financial')
         

    def user(self):
        query = 'create table if not exists checked (username varchar(20))'
        self.mycursor.execute(query)
        query = 'select * from checked'
        self.mycursor.execute(query)
        data =self.mycursor.fetchone()
        x = data[0]
        return x 




    
    def create_expense_table(self):
        query = f'create table if not exists {self.user()}_expense( SL_NO integer primary key, EXPENSE integer,date date,category varchar(50))'
        data = self.mycursor.fetchall()# this is for releasing data in resultset so that unread result error wont come essentially cleanng the resultset
        self.mycursor.execute(query)
        self.mydb.commit()

    

    def insert_expense(self,sl =1,expense='',date = '',category = ''):
        query = 'insert into {}_expense values({},"{}","{}","{}")'.format( self.user(),sl,expense,date,category) 
        self.mycursor.execute(query)
        self.mydb.commit()

    def create_monthly_goals_table(self):
        query = 'create table if not exists {}_monthly_goals(`{}` date ,`{}` date, {} INTEGER )'.format(self.user(),'FROM','TO','GOAL_MONEY')
        print(query)
        self.mycursor.execute(query)

 
    
    def insert_monthly_goal(self,From = '2023/03/22',to = '2023/03/22',goal = 23):
        query = 'insert into {}_monthly_goals values("{}","{}",{})'.format( self.user(),From,to,goal)
        print(query)
        self.mycursor.execute(query)
        self.mydb.commit()
 

    def create_temporary_source_of_income(self):
        query = f'create table if not exists {self.user()}_temporary_source_of_income(SL_NO integer primary key,income integer,date date, category varchar(20) )'
        self.mycursor.execute(query)
    
    def insert_temporary_source_of_income(self,slno,income,date,goal):
        query = f'insert into {self.user()}_temporary_source_of_income values({slno},{income},"{date}","{goal}")' 
        self.mycursor.execute(query)
 
    def select_monthly_goal_label(self):
        query = 'select `TO` from {}_monthly_goals'.format(self.user())
        zero = self.mycursor.fetchall()
        self.mycursor.execute(query)
        data = self.mycursor.fetchone()
        if data == None:
            x = 'YYYY/MM/DD'
        else:
            x = data[0]

        return str(x) 
    
    def select_yearly_goal_label(self):
        query = 'select `TO` from {}_yearly_goals'.format(self.user())
        zero = self.mycursor.fetchall()
        self.mycursor.execute(query)
        data = self.mycursor.fetchone()
        if data == None:
            x = 'YYYY/MM/DD'
        else:
            x = data[0]

        return x 
    
    def select_goal_money_monthly_goals(self):
        query = 'select * from {}_monthly_goals'.format(self.user())
        self.mycursor.execute(query)
        data = self.mycursor.fetchone()
        a  =  data[2]
        
        if data == None:
            x = 'YYYY/MM/DD'
        else:
            pass
         
        return a
    
    def delete_from_monthly_goals(self):
        query = f'delete from {self.user()}monthly_goals'
        self.mycursor.execute(query)


    def create_months(self):
        query = 'create table if not exists month(SL_NO integer primary key,MONTH varchar(10),NO_OF_DAYS varchar(10))'
        self.mycursor.execute(query)

    def insert_months(self):
        month_dict = {1: ('January', '31'),2: ('February', '28/29'),3: ('March', '31'),4: ('April', '30'),5: ('May', '31')
                      ,6: ('June', '30'),7: ('July', '31'),8: ('August', '31'),9: ('September', '30'),10: ('October', '31')
                      ,11: ('November', '30'),12: ('December', '31')}
        
        query = 'select * from month'
        self.mycursor.execute(query)
        data = self.mycursor.fetchone()
        if data == None :
            for i in month_dict:
                month = month_dict[i][0]
                no_of_days = month_dict[i][1]
                query = f'insert into month values({i},"{month}","{no_of_days}")'
                self.mycursor.execute(query)
                self.mydb.commit()

        else:
            pass


    def select_expense(self):
        query = f'select * from {self.user()}_expense;'
        data = self.mycursor.fetchall()
        data = None
        self.mycursor.execute(query)
        x = self.mycursor.fetchall()
        print(x)

    def plot(self):
        

        date_x = []
        amount_y = []

        query = f'select sum(expense),date from {self.user()}_expense group by date'
        self.mycursor.execute(query)

        data = self.mycursor.fetchall()
        print(data)



        for i in data:

            date_x.append(str(i[1])[8:10])
            amount_y.append(i[0])

 
        fig, ax = plt.subplots()

 
        ax.plot(date_x, amount_y,marker = 'o')
       

        query = f'select * from {self.user()}_monthly_goals'
         
        self.mycursor.execute(query)
        budget = self.mycursor.fetchone()
        budget = budget[2]


        ax.axhline(y=budget, linestyle='--', color='grey')


        ax.set_xlabel('date')
        ax.set_ylabel('expense')
        ax.set_title('EXPENSE PER DAY')

        plt.show()

    def pie(self):  
        query = f'select category,sum(expense) from {self.user()}_expense group by category'
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        list1 = []
        list2 = []

        for i in data:
            list1.append(i[0])
            list2.append(i[1])

        explode = [0.6,0.6,0.6,0.6,0,0.6]
         
       

    


        plt.pie(list2 )
        plt.legend(list1)
        plt.show()



    def close(self):
        self.mydb.commit()
        self.mydb.close()


    
