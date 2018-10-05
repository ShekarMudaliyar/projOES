import Tkinter as tk


class Page(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		container = tk.Frame(self)
		container.pack()
		self.frames = {}
		for F in (StartPage,PageOne):
			frame = F(container,self)
			self.frames[F] = frame
			frame.grid(row=0,column=0,sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	

	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		tk.Label(self, text="First Name").grid(row=0)
		tk.Label(self, text="Last Name").grid(row=1)
		login = tk.Button(self,text ="Login",command = lambda:controller.show_frame(PageOne))

		e1 = tk.Entry(self)
		e2 = tk.Entry(self)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)
		login.grid(row=2,column=0)

	

class PageOne(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1 = tk.Label(self,text="back")
		label1.pack()
		button = tk.Button(self, text="back",command=lambda:controller.show_frame(StartPage))
		button.pack()


app = Page()
app.wm_attributes("-topmost", 1)
# app.attributes("-fullscreen", True)
app.mainloop()
