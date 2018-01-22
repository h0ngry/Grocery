#from selenium import webdriver


#browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
#url = "https://www.heb.com/search/?q=chicken"
#browser.get(url) #navigate to the page

from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Shopping List")

        self.label = Label(master, text="My Grocery Shopping List")
        self.label.grid(row=0, column=1)


        self.label2 = Label(master, text="Please Enter an Item")
        self.label2.grid(row=1,column=0)

        self.e1 = Entry(master)
        self.e1.grid(row=1,column=1)
        self.e1.focus_set()



        self.b = Button(master, text="Search", width=10, command=self.callback)
        self.b.grid(row=2,column=1)

        self.results = Text(master, height=50, width=40)
        self.results.grid(row=3,column=2)

        self.label3 = Label(master,text="Grocery List (Right Click to Remove from List)")
        self.label3.grid(row=2,column =3)

        self.list = Text(master, height=50, width=30)
        self.list.grid(row=3, column=3)

        self.c = Button(master, text="Add to List", width=10, command=self.callback)
        self.c.grid(row=2, column=2)




        #self.list = Text(master,height = )


    def greet(self):
        print("Greetings!")

    def callback(self):
        print (self.e1.get())


def main():
    root = Tk()
    root.geometry("900x600+30+30")

    my_gui = MyFirstGUI(root)

    root.mainloop()

main()