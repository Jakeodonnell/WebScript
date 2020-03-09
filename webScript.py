from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from tkinter import * 

root = Tk()
root.geometry('500x500')
l = Label(root, text = "Hello")
with open("com.txt", "a") as f:
    f.truncate(0)

def webGet():
    with open("com.txt", "a") as f:
        f.writelines("website\n")
        f.write(website.get() + "\n")
        T.insert(END,"Will open: " + website.get() + "\n")


def clicking():
    print(obj.get())
    with open("com.txt", "a") as f:
        f.write("click\n")
        f.write(obj.get() + "\n")
        T.insert(END,"Will click: " + obj.get() + "\n")

loop = False
def run():
    def click(webObject):
        fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, webObject)))
        fastrack.click()

    def select(webObject):
        s1 = Select(driver.find_element_by_xpath(webObject))
        s1.select_by_value("12")

    driver = webdriver.Chrome()
    with open("com.txt", "r") as f:
        for line in f:
            arg = line
            webObject = next(f)
            print(arg)

            if arg == "website\n":
                print("opening " + webObject)
                driver.set_window_size(1600, 1100)
                driver.get(webObject)

            if arg == "click\n":
                click(webObject)

            if arg == "select\n":
                select(webObject)

#-----------ROW 0------------
T = Text(root, height=10, width=25, undo=True)
T.grid(row = 2, columnspan = 2)

#-----------ROW 1------------
chooseWebsite = Button(root, text = "Website:  ", command = webGet, height = 2, width = 10).grid(row = 0)
website = Entry(root)
website.grid(row = 0, column = 1)
#-----------ROW 2------------
clickObj = Button(root, text = "object:  ", height = 2, width = 10, command = clicking).grid(row = 1)
obj = Entry(root)
obj.grid(row = 1, column = 1)
loop = Radiobutton(root, text="Loop", variable=loop)
loop.grid(row = 1, column = 2)

#-----------ROW 3------------
run = Button(root, text = "runScript", height = 2, width = 10, command = run).grid(row = 3)


root.mainloop()
