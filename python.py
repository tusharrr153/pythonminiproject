import tkinter
window=tkinter.Tk()
window.title("Form")
window.state('zoom')
window.geometry('600x600')
s1=tkinter.StringVar()
s2=tkinter.StringVar()
s3=tkinter.StringVar()
s4=tkinter.StringVar()
s5=tkinter.StringVar()
s6=tkinter.StringVar()
s7=tkinter.StringVar()
s8=tkinter.StringVar()
s9=tkinter.StringVar()
s10=tkinter.StringVar()



l1=tkinter.Label(window,text="Registration Form",bg="red",fg="white",font=("fixedsys",20))
l2=tkinter.Label(window,text="FirstName:",font=20)
l3=tkinter.Label(window,text="Middlename:",font=20)
l4=tkinter.Label(window,text="LastName:",font=20)
l5=tkinter.Label(window,text="Contact No.:",font=20)
l6=tkinter.Label(window,text="Gmail ID:",font=20)
l7=tkinter.Label(window,text="Age:",font=20)
l8=tkinter.Label(window,text="Address:",font=20)
l9=tkinter.Label(window,text="Gender:",font=20)
l10=tkinter.Label(window,text="Blood Group:",font=20)
l11=tkinter.Label(window,text="Caste:",font=20)



e1=tkinter.Entry(window,textvariable=s1)
e1.grid(row=2,column=2,sticky='w',padx=10,pady=10)
e2=tkinter.Entry(window,textvariable=s2)
e2.grid(row=3,column=2,sticky='w',padx=10,pady=10)
e3=tkinter.Entry(window,textvariable=s3)
e3.grid(row=4,column=2,sticky='w',padx=10,pady=10)
e4=tkinter.Entry(window,textvariable=s4)
e4.grid(row=5,column=2,sticky='w',padx=10,pady=10)
e5=tkinter.Entry(window,textvariable=s5)
e5.grid(row=6,column=2,sticky='w',padx=10,pady=10)
e6=tkinter.Entry(window,textvariable=s6)
e6.grid(row=7,column=2,sticky='w',padx=10,pady=10)
e7=tkinter.Entry(window,textvariable=s7)
e7.grid(row=8,column=2,sticky='w',padx=10,pady=10)
e8=tkinter.Entry(window,textvariable=s8)
e8.grid(row=9,column=2,sticky='w',padx=10,pady=10)
e9=tkinter.Entry(window,textvariable=s9)
e9.grid(row=10,column=2,sticky='w',padx=10,pady=10)
e10=tkinter.Entry(window,textvariable=s10)
e10.grid(row=11,column=2,sticky='w',padx=10,pady=10)



l1.grid(row=1,column=2,padx=400,pady=10)
l2.grid(row=2,column=1,padx=10,pady=10)
l3.grid(row=3,column=1,padx=10,pady=10)
l4.grid(row=4,column=1,padx=10,pady=10)
l5.grid(row=5,column=1,padx=10,pady=10)
l6.grid(row=6,column=1,padx=10,pady=10)
l7.grid(row=7,column=1,padx=10,pady=10)
l8.grid(row=8,column=1,padx=10,pady=10)
l9.grid(row=9,column=1,padx=10,pady=10)
l10.grid(row=10,column=1,padx=10,pady=10)
l11.grid(row=11,column=1,padx=10,pady=10)



window.mainloop
