from tkinter import *
import pyrebase
config = {
  "apiKey": "AIzaSyDir5gCTjlHspkw7DpA7jlLtrZ6u2kyV_A",
  "authDomain": "crested-idiom-216905.firebaseapp.com",
  "databaseURL": "https://crested-idiom-216905.firebaseio.com",
  "storageBucket": "",
  "serviceAccount": "cred.json"
}
firebase = pyrebase.initialize_app(config)
# import gtk,webkit
root = Tk()
root.wm_attributes("-topmost", 1)
root.attributes("-fullscreen", True)
root.bind("<Alt-Key-F4>", lambda: closes_gracefully())
def closeButton():
   root.destroy()

But = Button(text ="Close", command = closeButton)
Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=1)
login = Button(text ="Login")

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
But.grid(row=2,column=1)
login.grid(row=2,column=0)

root.mainloop()
