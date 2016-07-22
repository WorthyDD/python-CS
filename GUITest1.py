from Tkinter import *
import tkMessageBox

class Application(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel.pack()
        # self.helloLabel = Label(self, text = '               Hello world!               ')
        # self.quitBtn = Button(self, text ='Quit', command = self.quit)
        # self.quitBtn.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertBtn = Button(self, text = 'Hello', command = self.hello)
        self.alertBtn.pack()

    def hello(self):
        name = self.nameInput.get() or ' World'
        tkMessageBox.showinfo('Message', 'Hello, %s ' % name)


app = Application()
app.master.title('Hello World!')
app.mainloop()