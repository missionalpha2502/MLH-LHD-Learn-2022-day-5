def billing(): # to create bills for customer-------------------------------------------------------------BILLING system
    global c, cur, apt, flag, t, name, name1, add, st, names, qty, sl, qtys, vc_id, n, namee, lb1
    t=0
    vc_id=''
    names=&#91;]
    qty=&#91;]
    sl=&#91;]
    n=&#91;]
    qtys=&#91;'']*10
    cur.execute("select *from med")
    for i in cur:
        n.append(i&#91;1])
    c.commit()
    if flag=='st':
        st.destroy()
    else:
        apt.destroy()
    flag='st'
    st=Tk()
    st.title('BILLING SYSTEM')
    Label(st,text='-'*48+'BILLING SYSTEM'+'-'*49).grid(row=0,column=0,columnspan=7)
    Label(st,text='Enter Name: ').grid(row=1,column=0)
    name1=Entry(st)
    name1.grid(row=1, column=1)
    Label(st,text='Enter Address: ').grid(row=2,column=0)
    add=Entry(st)
    add.grid(row=2, column=1)
    Label(st,text="Value Id (if available)").grid(row=3, column=0)
    vc_id=Entry(st)
    vc_id.grid(row=3, column=1)
    Button(st,text='Check V.C.', bg='green', fg='white', command=blue).grid(row=4, column=0)
    Label(st,text='-'*115).grid(row=6, column=0,columnspan=7)
    Label(st,text='SELECT PRODUCT',width=25,relief='ridge').grid(row=7, column=0)
    Label(st,text=' RACK  QTY LEFT     COST          ',width=25,relief='ridge').grid(row=7, column=1)
    Button(st,text='Add to bill', bg='blue', fg='white', width=15,command=append2bill).grid(row=8, column=6)
    Label(st,text='QUANTITY',width=20,relief='ridge').grid(row=7, column=5)
    qtys=Entry(st)
    qtys.grid(row=8,column=5)
    refresh()
    Button(st,width=15,text='Main Menu', bg='green', fg='white', command=main_menu).grid(row=1,column=6)
    Button(st,width=15,text='Refresh Stock',bg='skyblue', fg='black', command=refresh).grid(row=3,column=6)
    Button(st,width=15,text='Reset Bill', bg='red', fg='white', command=billing).grid(row=4,column=6)
    Button(st,width=15,text='Print Bill', bg='orange', fg='white', command=print_bill).grid(row=5,column=6)
    Button(st,width=15,text='Save Bill', bg='blue', fg='white', command=make_bill).grid(row=7,column=6)
    
    st.mainloop()
