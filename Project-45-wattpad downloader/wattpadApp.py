import tkinter as tk
import tkinter.font as tkFont
# from turtle import right
from wattpad_scraper import Wattpad

root = tk.Tk()


#setting title
root.title("Wattpad downloader")
#setting window size
width=600
height=120
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
#variable
isMature=False
isCompleted=False
bookLimit=0

def Download_button_command(url):
    w=Wattpad()
    book=w.get_book_by_url(url.get())
    book.convert_to_epub(loc='C:/Users/HP/Downloads')


def SearchButton_command(title,limit,mature,Completed):
    w=Wattpad()
    if bookLimit.isdigit():
        lit_box.insert("error only input integer")
    books=w.search_books(title,limit,mature,Completed)


def completedCheckBox_command(self):
    if(isCompleted==True):
        isCompleted=False
    else:
        isCompleted=True

def matureCheckBox_command(self):
    if(isMature==True):
        isMature=False
    else:
        isMature=True



url_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
url_label["font"] = ft
url_label["fg"] = "#333333"
url_label["justify"] = "center"
url_label["text"] = "URL:"
url_label.place(x=0,y=40,width=70,height=25)

url_entry=tk.Entry(root)
url_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
url_entry["font"] = ft
url_entry["fg"] = "#333333"
url_entry["justify"] = "center"
url_entry["text"] = "Entry"
url_entry.place(x=70,y=40,width=529,height=30)

Download_button=tk.Button(root)
Download_button["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
Download_button["font"] = ft
Download_button["fg"] = "#000000"
Download_button["justify"] = "center"
Download_button["text"] = "Download"
Download_button.place(x=250,y=80,width=70,height=25)
Download_button["command"] = lambda:Download_button_command(url_entry)

  
root.mainloop()
