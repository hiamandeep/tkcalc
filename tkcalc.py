from Tkinter import *
class calc:
	
	def equals(self):
		self.expression = self.e.get()
		self.value= eval(self.expression) 
		self.e.delete(0,END)
		self.e.insert(0,self.value)
	def clear1(self):
		self.e.delete(0,END)
	def action(self,argi):
		self.e.insert(END,argi)
	
	def __init__(self,master):
	 	
		master.title('Calulator')
		master.geometry()
		self.e = Entry(master)
		self.e.grid(row=0,column=0,columnspan=5,pady=5)

		self.e.focus_set()
		
		#Generating Buttons
		Button(master, text="=", width=10, command=lambda:self.equals()).grid(row=2, column=4)
		Button(master,text='AC',width=10,command=lambda:self.clear1()).grid(row=1, column=4)

		Button(master,text="+",width=5,command=lambda:self.action('+')).grid(row=4, column=3)
		Button(master,text="x",width=5,command=lambda:self.action('*')).grid(row=2, column=3)
		Button(master,text="-",width=5,command=lambda:self.action('-')).grid(row=3, column=3)
		Button(master,text="/",width=5,command=lambda:self.action('/')).grid(row=1, column=3)
		Button(master,text="%",width=5,command=lambda:self.action('%')).grid(row=4, column=2)
		Button(master,text="7",width=5,command=lambda:self.action(7)).grid(row=1, column=0)
		Button(master,text="8",width=5,command=lambda:self.action(8)).grid(row=1, column=1)
		Button(master,text="9",width=5,command=lambda:self.action(9)).grid(row=1, column=2)
		Button(master,text="4",width=5,command=lambda:self.action(4)).grid(row=2, column=0)
		Button(master,text="5",width=5,command=lambda:self.action(5)).grid(row=2, column=1)
		Button(master,text="6",width=5,command=lambda:self.action(6)).grid(row=2, column=2)
		Button(master,text="1",width=5,command=lambda:self.action(1)).grid(row=3, column=0)
		Button(master,text="2",width=5,command=lambda:self.action(2)).grid(row=3, column=1)
		Button(master,text="3",width=5,command=lambda:self.action(3)).grid(row=3, column=2)
		Button(master,text="0",width=5,command=lambda:self.action(0)).grid(row=4, column=0)
		Button(master,text=".",width=5,command=lambda:self.action('.')).grid(row=4, column=1)
#Main
root = Tk()
obj=calc(root)
root.mainloop()
