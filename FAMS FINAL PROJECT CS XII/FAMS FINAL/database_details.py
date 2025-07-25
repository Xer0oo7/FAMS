def database():
    import mic as m
    d1 = m.window('DATABASE DETAILS','500x500')
    bind = d1.create_window()

    d1.create_label(master = bind,text = 'HOST    :',x= 120, y = 30)
    d1.create_label(master = bind,text = 'USER    :',x= 120, y = 90)
    d1.create_label(master = bind,text = 'PASSWORD:',x= 120, y = 150)

    host      = d1.create_entry(master = bind ,corner = 30 ,x = 270 ,y = 30)
    user      = d1.create_entry(master = bind ,corner = 30 ,x = 270 ,y = 90)
    password  = d1.create_entry(master = bind ,corner = 30 ,x = 270 ,y = 150)

    def gather():
        global hoster
        global username
        global passwording
        hoster      = host.get()
        username    = user.get()
        passwording = password.get()
        bind.destroy()

        

    d1.create_button(master = bind,corner = 15,text = 'CONNECT',x = 120 , y = 200,width=295,command = gather)


    d1.end()
    return [hoster,username,passwording]

 
