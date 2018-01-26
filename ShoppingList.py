from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options) #replace with .Firefox(), or with the browser of your choice

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



        self.b = Button(master, text="Search", width=10, command=self.scrape)
        self.b.grid(row=2,column=1)

        self.results_txt = Text(master, height=50, width=40)
        self.results_txt.grid(row=3,column=2)


        self.label3 = Label(master,text="Grocery List (Right Click to Remove from List)")
        self.label3.grid(row=2,column =3)

        self.list = Text(master, height=50, width=30)
        self.list.grid(row=3, column=3)

        self.c = Button(master, text="Add to List", width=10, command=self.scrape)
        self.c.grid(row=2, column=2)




        #self.list = Text(master,height = )


    def greet(self):
        print("Greetings!")

    def callback(self):
        print (self.e1.get())

    def scrape(self):
        self.results_txt.delete(1.0,END)
        self.url = "https://www.heb.com/search/?q="+ self.e1.get()
        posts = []
        while posts == []:
            browser.get(self.url)  # navigate to the page
            posts = browser.find_elements_by_class_name("responsivegriditem__title")

        # Convert web elements to text/string
        new_posts = []
        for post in posts:
            new_posts.append(post.text)

        # Remove Duplicates
        self.results = []
        for post in new_posts:
            if post not in self.results:
                self.results.append(post)

        for result in self.results:
            self.results_txt.insert(END, result + '\n')

        browser.close()





def main():
    root = Tk()
    root.geometry("900x600+30+30")

    my_gui = MyFirstGUI(root)

    root.mainloop()

main()