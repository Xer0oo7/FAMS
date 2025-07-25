import subprocess
import importlib

modules = ['requests','matplotlib','customtkinter','plyer','pillow','pygame','moviepy']
avail = []

def module_exists(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

def install_module(module_name):
    try:
        subprocess.run(['pip', 'install', module_name], check=True)
        print(f"Successfully installed {module_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {module_name}")

for i in modules:
    avail.append(module_exists(i))


for i in range(0,7):
    print(modules[i])
    if avail[i] == False:
        print(modules[i])
        install_module(modules[i])
    
    else:
        pass

import mic as m
from  PIL import ImageTk,Image
import mysql.connector  as mysql
import database_details as d
import csv
import os
import pygame 
 
def access():
    csv_file_path = 'record.csv'
 
    if os.path.exists(csv_file_path):
        pass

    else:
        details = d.database()
        host = details[0]
        user = details[1]
        password = details[2]
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([host,user,password])
            writer.writerows(details) 

    with open('record.csv', 'r') as file:
        reader = csv.reader(file)
        first_row = next(reader)
    
    one = first_row[0]
    teo = first_row[1]
    three = first_row[2]

    d1 = m.window(title = 'FAMS:LOGIN',geo ='1000x1000+200+0')
    bind = d1.create_window()
    

    sql  = m.sql(x = one,y = teo,z = three)
    query1 = 'create table if not exists login(username varchar(10) primary key , password varchar(12))'
    sql.mycursor.execute(query1)
   
    def end(x):
        d1.destroy()
    
    logo = ImageTk.PhotoImage(Image.open('pattern.png'))
    d1.create_label_image(master = bind,image = logo,anchor = 'center')
 
    def retrieve():
        user = entry_username.get()
        passwd = entry_password.get()
        query =  'select *  from login where username = "{}"'.format(user)
        sql.mycursor.execute(query)
        result = sql.mycursor.fetchall()
        
        if len(result) != 0:
            query1 = 'select * from login where username = "{}" and password = "{}"'.format(user,passwd)
            sql.mycursor.execute(query1)
            virat = sql.mycursor.fetchall()
            print(virat)
            if len(virat) != 0:
                query = 'create table if not exists checked(name varchar(20))'
                sql.mycursor.execute(query)
                query = 'insert into checked values("{}")'.format(user)
                sql.mycursor.execute(query)
                sql.mydb.commit()
                bind.destroy()

                from moviepy.editor import VideoFileClip
                video = VideoFileClip('popup.mp4')
                video.preview()
                pygame.quit()

                import fams
                fams.fams()

            else:
                error.configure(text = 'incorrect password')

        
        else:
            error.configure(text = 'incorrect username')
            
    def register():
        from plyer import notification
        end('x')

        query1 = 'create table if not exists login(username varchar(10) primary key, password varchar(12))'
        sql.mycursor.execute(query1)

        d2 = m.window('FAMS: REGISTER',"1000x1000+200+0")
        app = d2.create_window()

        fact= d2.create_frame(width = 328,height = 390,x = 330, y = 180)

        def devan_akshay_praveen_adithya():
            d2.destroy()
            access()

        d2.create_label(master = fact, text = 'REGISTER', x = 109 , y = 10)
        d2.create_label(master = fact,text = 'USERNAME :',x = 10 , y = 100,font = ('One Day ',20,'bold'))
        d2.create_label(master = fact,text = 'PASSWORD :',x = 10 , y = 160,font = ('One Day ',20,'bold'))
        error = d2.create_button(master = fact,x = 10, y = 200,width = 310,height=119,command = devan_akshay_praveen_adithya,text = 'CONTINUE TO LOGIN')

        user     = d2.create_entry(master = fact,x = 150 , y = 97,height =10,place_text='USERNAME')
        password = d2.create_entry(master = fact,x = 150 , y = 157,height =10,place_text='PASSWORD')

        def computer():
            username = user.get()
            passwd = password.get()
            query = f'insert into login values("{username}","{passwd}")'
            sql.mycursor.execute(query)
            sql.mydb.commit()
            notification.notify(title = "FAMS",message= f" Dear user your username {username} and password {passwd} has been added successfully",timeout=10)

        d2.create_button(master = fact,x= 10,y = 330,text = 'REGISTER',command = computer,width = 310,height = 50)
        
        d2.end()
        access()
            
    frame = d1.create_frame(master = bind ,width = 328,height = 390,corner = 15,x= 350, y = 180)
    l2 = d1.create_label(master = frame , text = 'F.A.M.S \nLOGIN/REGISTER',font = ('One Day ',23,'bold'),bg_color = ('#2C2C2C'),x = 75, y = 10)
  
    d1.create_label(master = frame ,text = 'USERNAME:',bg_color = ('#2C2C2C'),x = 10, y= 90)
    d1.create_label(master = frame ,text = 'PASSWORD:',bg_color = ('#2C2C2C'),x = 10, y= 140)
    error = d1.create_label(master = frame,x = 10, y = 260,width = 310,height=119,text_color='#1DCA80')
    
  
    entry_username = d1.create_entry(master = frame ,corner = 30,x = 155,y = 90)
    entry_password = d1.create_entry(master = frame ,corner = 30,show = '*',x = 157,y = 140)
    
    login = d1.create_button(master = frame,text = 'LOGIN',command =  retrieve,x = 10 ,y = 200,height = 50)
    sign_up = d1.create_button(master = frame,text = 'REGISTER',command = register,x = 170 ,y = 200,height = 50)
    
    bind.bind('<Escape>',end)
    d1.end()

access()