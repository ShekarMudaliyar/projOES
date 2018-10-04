import tkinter as tk

class Page(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		container = tk.Frame(self)
		container.pack()
		self.frames = {}
		frame = StartPage(container,self)
		self.frames[StartPage] = frame
		frame.grid(row=0,column=0,sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self,text="Login")
		label.pack()
		button = tk.Button(self, text="Login",command=lambda:controller.show_frame(PageOne))
		button.pack()

class PageOne(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1 = tk.Label(self,text="back")
		label1.pack()
		button = tk.Button(self, text="back",command=lambda:controller.show_frame(StartPage))
		button.pack()



app = Page()
app.mainloop()
