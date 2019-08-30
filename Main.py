from tkinter import *
import tkinter as tk
import webbrowser
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import os
class HyperlinkManager:
    def __init__(self, text):

        self.text = text

        self.text.tag_config("hyper", foreground="blue", underline=1)

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return


def click1():
     webbrowser.open_new(r"https://notepad-plus-plus.org/")

def click2():
     webbrowser.open_new(r"https://www.gimp.org/")

def click3():
     webbrowser.open_new(r"https://www.dropbox.com/sh/apox9tiberg6pwk/AAABlDYEj0iDxfoXLHIzxKjla?dl=0")

def click4():
     webbrowser.open_new(r"https://forums.civfanatics.com/resources/modders-guide-to-civilization-v.23669/")

def click5():
     webbrowser.open_new(r"https://forums.civfanatics.com/threads/modders-starter-package.388779/#post-9729501")

def click6():
     webbrowser.open_new(r"https://drive.google.com/file/d/11u25vO4wmmZLA0weR5Wjs7vvJ232anaA/view")
def click7():
     webbrowser.open_new(r"https://r3---sn-4g5edns7.c.drive.google.com/videoplayback?expire=1554096856&ei=mGqhXL-nJcKA-QXHnoaQAg&ip=145.255.171.40&cp=QVNKVkFfVVhTR1hOOnJvSnBXa3oxZ1FHZ1hTZUdwaDNsdFdYMVJtQm11cnBsVEFLUUc3TTk3aGw&id=97cd5e157dca3fbc&itag=59&source=webdrive&requiressl=yes&ttl=transient&susc=dr&driveid=1MB9dY4q36DshZno3xrKWhRDRAJWWVzak&app=explorer&mime=video/mp4&dur=287.625&lmt=1554063014923538&sparams=expire,ei,ip,cp,id,itag,source,requiressl,ttl,susc,driveid,app,mime,dur,lmt&sig=ALgxI2wwRAIgRqk3zFe2sLj6ucwg7z0YB9-AzAjKjy8aaQXAQGLp5XICIC0NLAc0v9dhrHsEX89QOvW_vQ-13pFgX8fBBCPw9rdO&cpn=-s7cUKMMcZgTMljD&c=WEB_EMBEDDED_PLAYER&cver=20190321&redirect_counter=1&cm2rm=sn-n8vkl7s&req_id=74ad2146d5b536e2&cms_redirect=yes&mm=34&mn=sn-4g5edns7&ms=ltu&mt=1554082537&mv=m&pl=24&lsparams=mm,mn,ms,mv,pl&lsig=AHylml4wRgIhAIaZAvrBqNcu8vYayxx4RMG6v_ebOQJ2bzBS9NcdO8eyAiEAmDDLMbKvdGq0__MDTW5TM0nYzhtIegj4EGufL_2HEdA=")
def click8():
     webbrowser.open_new(r"https://drive.google.com/file/d/1zOYz3lgfoDGxPZGg3nL_TOTm1T7aXa7e/view")
def click9():
     webbrowser.open_new(r"https://drive.google.com/file/d/1vNJ6L0I8qIZ5Bg_r4CrnL-Yxln6qPTpt/view")

def click10():
     webbrowser.open_new(r"https://drive.google.com/file/d/1yaVApmbxnZWXkh9Vo9Zqm3ppJs50Yjly/view")

def click11():
     webbrowser.open_new(r"https://drive.google.com/file/d/14QLuu10iOikwImK073qfDEKwK0q2VD0F/view")


def click12():
     webbrowser.open_new(r"https://drive.google.com/file/d/1mbrceqm0e2dQUW91yRmv5qSnVbEIRCwR/view")


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#878787', bd=2)
        toolbar.configure(background="#dbe8ff")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="Tesseract.gif")
        self.add_imgs = tk.PhotoImage(file='man.gif')
        self.add_imgt = tk.PhotoImage(file='man.gif')
        self.add_imgf = tk.PhotoImage(file='man.gif')
        btn_open_dialog = tk.Button(toolbar, text='Getting Started', command=self.open_dialog1, bg='#42f4eb', bd=10,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_sdialog = tk.Button(toolbar, text='Custom Leader', command=self.open_dialog2, bg='#42f4eb', bd=10,
                                     compound=tk.TOP, image=self.add_imgs)

        btn_open_dialog.pack(side=tk.LEFT)
        btn_open_sdialog.pack(side=tk.LEFT)

    def open_dialog1(self):
        Icon1()
    def open_dialog2(self):
        Icon2()


class Icon1(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_icon()

    from PIL import Image

    def init_icon(self):
        self.geometry('1220x520+400+300')
        self.resizable(True, True)
        Sc=Scrollbar(self)
        a = Text(self,height=540, width=100,font=("Helvetica",16,"bold italic"),fg="#fffcdb")
        a.pack(side=LEFT, fill=Y)
        Sc.pack(side=RIGHT, fill=Y)
        Sc.config(command=a.yview)
        a.config(yscrollcommand=Sc.set)
        hyperlink=HyperlinkManager(a)
        a.configure(background="#dbe8ff")
        val = "1. Getting Started\na. What this tutorial is for\nWith this tutorial a user can learn to create a mod for Civilization 5 that adds in a playable\ncivilization. This section of the tutorial explains everything you’ll need before you get started.\nUsers should be aware that this tutorial won’t allow them to create more complex civilizations,\nlike ones that use custom 3D models. It is the author’s hope that this tutorial is easy to use and\nfollow.\nb. What you need to download\n"
        a.insert(END, val)
        a.insert(INSERT,"https://notepad-plus-plus.org/",hyperlink.add(click1))
        a.insert(INSERT,"The second thing you’ll need is an image editor capable of saving images as .dds files. Photoshop and gimp are both capable of this. Gimp is a free alternative to photoshop. A link is below.")
        a.insert(INSERT,"\nhttps://www.gimp.org/",hyperlink.add(click2))
        a.insert(INSERT,"\nThe third thing is you need to install the Civilization 5 SDK. This is a tool provided by Firaxis\nGames, the developers of Civilization 5 that allows you to package your mod in a way that the\ngame understands how to read it. The Civilization 5 SDK is available on Steam to owners of the\ngame (and possibly everyone else too). To find the Civilization SDK tool, use this image as\nreference. Click Library- Tools - Sid Meier’s Civilization V SDK.\n")
        #img = Image.open("this.png")

        #a.image_create(END, image=img)  # Example 1
        a.insert(INSERT,"The last thing you’ll need is the templates we use in this tutorial. Download them from this link, and use them when the tutorial directs you to.")
        a.insert(INSERT,"\nhttps://www.dropbox.com/sh/apox9tiberg6pwk/AAABlDYEj0iDxfoXLHIzxKjla?dl=0",hyperlink.add(click3))
        a.insert(INSERT,"i.Links and images\nb. How to use this tutorial\nThis tutorial will use text and video primarily to shofree w you how to create your mod. It is\nadvised that you use this tutorial in the order of its steps, but the tutorial will allow you to easily\brevisit earlier parts")
        a.insert(INSERT,"d. Other references")
        a.insert(INSERT,"If you want to explore other possibilities with your mod, or you want a purely text reference, this guide by Derek Paxton should help.")
        a.insert(INSERT,"\nhttps://forums.civfanatics.com/resources/modders-guide-to-civilization-v.23669/",hyperlink.add(click4))
        a.insert(INSERT,"This guide by user Thalassicus here has more to do with packaging and uploading your mod, which we will also go over in this tutorial.")
        a.insert(INSERT,"\nhttps://forums.civfanatics.com/threads/modders-starter-package.388779/#post-9729501",hyperlink.add(click5))
        a.insert(INSERT,"i.links")
        self.grab_set()
        self.focus_set()



def snd1():
    os.system("test.mp4")



class Icon2(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_icon()

    def init_icon(self):
        self.geometry('980x520+400+300')
        self.resizable(True, True)
        #Sc = Scrollbar(self)
        a = Text(self, height=20, width=80, font=("Helvetica", 16, "bold italic"), fg="#fffcdb")
        #a.pack(side=LEFT, fill=Y)
        a.pack()
        #Sc.pack(side=RIGHT, fill=Y)
        #Sc.config(command=a.yview)
        #a.config(yscrollcommand=Sc.set)
        hyperlink = HyperlinkManager(a)
        a.configure(background="#dbe8ff")
        a.insert(INSERT,"1. Custom Leader\n")
        a.insert(INSERT,"Overview\n")
        a.insert(INSERT,"Each civilization must have a leader. For example, America has George Washington. This guide\n")
        a.insert(INSERT,"goes over making a leader first, because the other files will reference this one. You’ll want to\n")
        a.insert(INSERT,"open up the template xml file for leader now, with whatever xml editor you chose. In the video\n")
        a.insert(INSERT,"we will use notepad++\n")
        a.insert(INSERT,"i.Video\n")
        a.insert(INSERT,"ii.")
        a.insert(INSERT,"Video 1\n",hyperlink.add(click6))
        a.insert(INSERT,"Video 2\n",hyperlink.add(click7))
        a.insert(INSERT,"Video 3\n",hyperlink.add(click8))
        a.insert(INSERT,"Video 4\n",hyperlink.add(click9))
        a.insert(INSERT,"Video 5\n",hyperlink.add(click10))
        a.insert(INSERT,"Video 6\n",hyperlink.add(click11))
        a.insert(INSERT,"Video 7\n",hyperlink.add(click12))
        self.grab_set()
        self.focus_set()
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="#dbe8ff")
    app = Main(root)
    app.pack()

    S = Scrollbar(root)
    S.configure(background="#dbe8ff")
    T = Text(root, height=40, width=100,font=("Helvetica",24,"bold italic"),fg="#fffcdb")
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = "This is a tutorial for creating mods for Civilization V that add playable civilizations."
    "If this is your first time using the tool, select Getting Started. Otherwise, navigate to the section youХd like to reference."
    T.insert(END, quote)

    root.title("Tool to create mods in Civilization V")
    root.geometry("750x650+300+200")
    root.resizable(True, True)
    root.mainloop()


