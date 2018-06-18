from tkinter import *



# def kg_to_multipleunits():

# def km_to_miles():
	
# 	miles=float(e1_value.get())*1.609
# 	t1.insert(END,miles)
def kg_to_grams():
   
   grams=1000*float(e1_value.get())
   t1.insert(END,grams)

def kg_to_pounds():
	pounds=2.200*float(e1_value.get())
	t2.insert(END,pounds);

def kg_to_ounces():
	kg_to_grams()
	kg_to_pounds()
	ounces=36*float(e1_value.get())
	t3.insert(END,ounces);




window=Tk()	








b1=Button(window,text="Convert",command=kg_to_ounces);
b1.pack()
b1.grid(row=0,column=2)
e2=Label(window,text="Kg")
e2.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value);
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20);
t1.grid(row=1,column=0)
t2=Text(window,height=1,width=20);
t2.grid(row=1,column=1)
t3=Text(window,height=1,width=20);
t3.grid(row=1,column=2)




window.mainloop()