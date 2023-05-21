import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkfontchooser import askfont
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog as fd
import pyqrcode
import png
import cv2
import os

class QrCoder(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.qr = master        
        font = ['Courier', '13', 'normal']
        self.fontcmd = ['Consolas', '10', 'normal']
        self.sw = self.qr.winfo_screenwidth()      #### screen width
        self.sh = self.qr.winfo_screenheight()     #### screen height
        self.w = self.sw - (self.sw/2)
        self.w = self.w - (self.sw/8)                #### calculation for window
        self.h = self.sh - (self.w/2)                
        self.xpos =(self.sw/2) - (self.w/2)          #### calculation for centre
        self.ypos =(self.sh/2) - (self.h/2)
        self.qr.geometry('%dx%d+%d+%d' % (self.w, self.h, self.xpos, self.ypos))
        self.dislbl = Label(master, text = "Enter text to generate QR", bg = '#FFFF00')
        self.dislbl.place(x = int(self.w)/2 - 60, y = int(self.h)/2 - 80)
        self.user_input = StringVar()
        self.entry = Entry(master, textvariable = self.user_input, width = 30)
        self.entry.place(x = int(self.w)/2 - 80, y = int(self.h)/2 - 50)
        self.img_lbl = Label(master, bg = '#FFFF00')
        self.img_lbl.place(x = int(self.w)/2 - 110, y = int(self.h)/2 - 140)
        self.output = Label(master, text ="", bg = '#FFFF00')
        self.output.place(x = int(self.w)/2 - 40, y = int(self.h)/2 - 150)
        self.btn = Button(master, text = "Generate", width = 15, command = self.generate_QR)

        self.btn.place(x = int(self.w)/2 - 45, y = int(self.h)/2 - 10)
        self.btnr = Button(master, text = "Read QR", width = 15, command = self.read_qr)

        self.btnr.place(x = int(self.w)/2 - 45, y = int(self.h)/2 + 15)
        self.bck = Button(master, text = "Back", command = self.bk)
        self.svbtn = Button(master, text = "Save", command = self.sv)
    def generate_QR(self):
        self.bck.place(x = 10, y = 10)
        self.dislbl['text'] = ""
        print(self.user_input.get())
        self.btn.place_forget()
        self.btnr.place_forget()
        self.svbtn.place(x = int(self.w)/2- 10, y = int(self.h)/2 + 100)
        if len(self.user_input.get())!=0 :
            global qr,img
            qr = pyqrcode.create(self.user_input.get())
            img = BitmapImage(data = qr.xbm(scale=8))
        else:
            messagebox.showwarning('warning', 'All Fields are Required!')
            self.btn.place(x = int(self.w)/2 - 45, y = int(self.h)/2 - 10)
            self.dislbl['text'] = "Enter text to generate QR"
            self.svbtn.place_forget()
            self.bck.place_forget()
            self.btnr.place(x = int(self.w)/2 - 45, y = int(self.h)/2 + 15)
            
        try:
            self.display_code()
        except:
            pass
    def sv(self):
        #qr.svg("qr.svg", scale = 14)
        data = self.user_input.get()
        qrc = pyqrcode.QRCode(data)
        qrc.png('qrcode.png', scale = 10)
        messagebox.showinfo("Boom Baby", "Image is Saved")
    def bk(self):
        self.dislbl.place(x = int(self.w)/2 - 60, y = int(self.h)/2 - 80)
        self.entry.place(x = int(self.w)/2 - 80, y = int(self.h)/2 - 50)
        self.btn.place(x = int(self.w)/2 - 45, y = int(self.h)/2 - 10)
        self.img_lbl['image'] = ''
        self.dislbl['text'] = "Enter text to generate QR"
        
        self.output['text'] = ""
        self.btnr.place(x = int(self.w)/2 - 45, y = int(self.h)/2 + 15)
        self.bck.place_forget()
        self.svbtn.place_forget()
        
    def display_code(self):
        self.img_lbl.config(image = img)
        self.output.config(text="QR code of " + self.user_input.get())
        
    def read_qr(self):
        file = fd.askopenfile(mode='r', filetypes=[('PNG Files', '*.png')])
        if file:
            filepath = os.path.abspath(file.name)
        image = cv2.imread(filepath)
        qr_det = cv2.QRCodeDetector()
        data = qr_det.detectAndDecode(image)
        self.entry.place_forget()
        self.btn.place_forget()
        self.dislbl.place_forget()
        self.btnr.place_forget()
        self.bck.place(x = 10, y = 10)
        self.output['text'] = "The content of QR is :  " + data[0]
        self.output['font'] = ["Times", 14, "bold"]
        self.output.place(x = int(self.w)/2 - 100, y = int(self.h)/2 - 50)
        
def main():
    root = Tk()
    root.title("QrCode Generator cosmos_dx")
    root.config(bg = '#FFFF00')
    root.resizable(False, False)
    QrCoder(root)
    root.mainloop()

if __name__ == "__main__":
    main()

### Abhishek Gupta ###
    ### Follow Insta - @abhishek.gupta0118 ###
