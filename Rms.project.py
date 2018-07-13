from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Panda Food Restaurant")


Tops = Frame(root , width = 1600,height = 50,bg="powder blue")
Tops.pack(side=TOP)

f1 = Frame(root , width = 800,height = 700)
f1.pack(side=LEFT)

f2 = Frame(root , width = 300,height = 700)
f2.pack(side=RIGHT)
#==============================Time==================================
localtime=time.asctime(time.localtime(time.time()))
#=================================info==================================
lblinfo = Label(Tops, font=('Georgia',50,'bold'),text="Panda Food Restaurant",fg="black",bd=10, anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=('Georgia',20,'bold'),text=localtime,fg="navy blue",bd=10, anchor='w')
lblinfo.grid(row=1,column=0)

#====================================calculator====================================
text_Input = StringVar()
operator =""
txtDisplay = Entry(f2,font=('ariel',20,'bold'), textvariable='text_input', bd=10, insertwidth=10,bg="light gray",justify='right')
txtDisplay.grid(columnspan=4)

def btnclick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup =str(eval(operator))
    text_Input.set("sumup")
    operator=""

def Ref():
    x = random.randint(1,100)
    randomRef = str(x)
    rand.set(randomRef)

    cof = float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr = float(Drinks.get())
    costoffries = cof * 26
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costofcheeseburger = cochee * 50
    costoffilet = cofi * 50
    costofdrinks = codr * 35
    costofmeal = "Rs.",str('%.2f'% (costoffries + costoflargefries + costofburger + costofcheeseburger + costoffilet + costofdrinks))
    PayTax=((costoffries + costoflargefries + costofburger  + costofcheeseburger + costoffilet + costofdrinks)*0.10)
    Totalcost=(costoffries + costoflargefries + costofburger  + costofcheeseburger  + costoffilet + costofdrinks)
    Ser_Charge=((costoffries + costoflargefries + costofburger + costofcheeseburger + costoffilet + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)
    Ser_Charge.set(Service)
    costofmeal.set(costofmeal)
    Tax.set(PaidTax)
    SubTotal.set(costofmeal)
    Totalcost.set(OverAllCost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Largefries.set("")
    Cheese_burger.set("")
    Drinks.set("")
    Filet.set("")
    Cost.set("")
    Survice_Charge.set("")
    Tax.set("")
    SubTotal.set("")
    Total.set("")


btn7=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="7",bg="black", command=lambda:btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="8",bg="black", command=lambda:btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="9",bg="black", command=lambda:btnclick(9))
btn9.grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="+",bg="black", command=lambda:btnclick("+"))
Addition.grid(row=2,column=3)
#================================================================================================

btn4=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="4",bg="black", command=lambda:btnclick(4))
btn4 .grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="5",bg="black", command=lambda:btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="6",bg="black", command=lambda:btnclick(6))
btn6.grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="-",bg="black", command=lambda:btnclick("-"))
Subtraction.grid(row=3,column=3)
#=================================================================================================

btn1=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="1",bg="black", command=lambda:btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="2",bg="black", command=lambda:btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="3",bg="black", command=lambda:btnclick(3))
btn3.grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="*",bg="black", command=lambda:btnclick("*"))
Multiply.grid(row=4,column=3)
#================================================================================================


btn0=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="0",bg="black", command=lambda:btnclick("0"))
btn0 .grid(row=5,column=0)
btnc=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="C",bg="black",command=clrdisplay)
btnc .grid(row=5,column=1)
btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="gray", font=('arial',20,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)
Decimal=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text=".",bg="black", command=lambda:btnclick("."))
Decimal.grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=4, fg="gray", font=('arial',20,'bold'),text="/",bg="black", command=lambda:btnclick("/"))
Division.grid(row=5,column=3)


#=======================================Restaurant info 1=======================================
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Cheese_burger = StringVar()

lblReference = Label(f1,font=('Georgia',10,'bold'),text="Reference",bd=8,anchor="w")
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('Georgia',10,'bold'),textvariable=random,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('Georgia',10,'bold'),text="Fries Meal",bd=8,anchor="w")
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('Georgia',10,'bold'),textvariable=Fries,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('Georgia',10,'bold'),text="Burger Meal",bd=8,anchor="w")
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('Georgia',10,'bold'),textvariable=Burger,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtBurger.grid(row=2,column=1)

lblLargefries = Label(f1,font=('Georgia',10,'bold'),text="Lunch Meal",bd=8,anchor="w")
lblLargefries.grid(row=3,column=0)
txtLargefries=Entry(f1,font=('Georgia',10,'bold'),textvariable=Largefries,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtLargefries.grid(row=3,column=1)

lblFilet = Label(f1,font=('Georgia',10,'bold'),text="Pizza Meal",bd=8,anchor="w")
lblFilet.grid(row=4,column=0)
txtFilet=Entry(f1,font=('Georgia',10,'bold'),textvariable=Filet,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtFilet.grid(row=4,column=1)

lblCheeseburger = Label(f1,font=('Georgia',10,'bold'),text="Cheese burger ",bd=8,anchor="w")
lblCheeseburger.grid(row=5,column=0)
txtCheeseburger=Entry(f1,font=('Georgia',10,'bold'),textvariable=Cheese_burger,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtCheeseburger.grid(row=5,column=1)

#=======================================Restaurant info 2===================================

Drinks = StringVar()
Cheese_burger = StringVar()
Cost = StringVar()
Survice_Charge = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

lblDrink = Label(f1,font=('Georgia',10,'bold'),text="cold drink",bd=8,anchor="w")
lblDrink.grid(row=0,column=3)
txtDrink=Entry(f1,font=('Georgia',10,'bold'),textvariable=Drinks,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtDrink.grid(row=0,column=5)


lblCost = Label(f1,font=('Georgia',10,'bold'),text=" Cost ",bd=8,anchor="w")
lblCost.grid(row=1,column=3)
txtCost=Entry(f1,font=('Georgia',10,'bold'),textvariable=Cost,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtCost.grid(row=1,column=5)

lblSurvice_Charge = Label(f1,font=('Georgia',10,'bold'),text="Survice Charge",bd=8,anchor="w")
lblSurvice_Charge.grid(row=2,column=3)
txtSurvice_Charge=Entry(f1,font=('Georgia',10,'bold'),textvariable=Survice_Charge,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtSurvice_Charge.grid(row=2,column=5)

lblTax = Label(f1,font=('Georgia',10,'bold'),text=" Tax",bd=8,anchor="w")
lblTax.grid(row=3,column=3)
txtTax=Entry(f1,font=('Georgia',10,'bold'),textvariable=Tax,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtTax.grid(row=3,column=5)

lblSubTotal = Label(f1,font=('Georgia',10,'bold'),text="Sub Total",bd=8,anchor="w")
lblSubTotal.grid(row=4,column=3)
txtSubTotal=Entry(f1,font=('Georgia',10,'bold'),textvariable=SubTotal,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtSubTotal.grid(row=4,column=5)

lblTotal = Label(f1,font=('Georgia',10,'bold'),text="Total Cost ",bd=8,anchor="w")
lblTotal.grid(row=5,column=3)
txtTotal=Entry(f1,font=('Georgia',10,'bold'),textvariable=Total,bd=8,insertwidth=4,bg="powder blue", justify = 'right')
txtTotal.grid(row=5,column=5)

#==============================================buttons=========================
lblTotal = Label(f1,text="--------------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)
btnTotal=Button(f1,padx=16,pady=8, bd=10, fg="black",font=('ariel',16,'bold'),width=10,text="TOTAL", bg="red",command = Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10, fg="black",font=('ariel',16,'bold'),width=10,text="RESET", bg="green",command = reset)
btnreset.grid(row=7, column=3)

btnexit=Button(f1,padx=16,pady=8, bd=10, fg="black",font=('arial',16,'bold'),width=10,text="EXIT", bg="yellow",command = qexit)
btnexit.grid(row=7, column=5)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue",anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel',16,'bold'),width=10,text="PRICE",bg="dark gray",command =price)
btnprice.grid(row=7,column=0)
root.mainloop()

