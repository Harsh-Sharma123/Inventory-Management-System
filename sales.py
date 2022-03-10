from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class sales:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Harsh Sharma")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_invoice = StringVar()
        self.bill_list = []

        # ==== Title =======
        lbl_title = Label(self.root, text="View Customer Bills", font=("goudy old style", 30), bg="#184a45", fg="white", bd=3,relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15), bd=3, relief=RIDGE, bg="lightyellow").place(x=180, y=100, width=180, height=28)

        btn_search = Button(self.root, text="Search", command=self.Search, font=("times new roman", 15, "bold"), cursor="hand2", bg="#2196f3", fg="white").place(x=370, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), cursor="hand2", bg="lightgray", fg="black").place(x=500, y=100, width=120, height=28)


        # ===== Bill List ========
        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, height=330, width=200)

        scrolly = Scrollbar(sales_frame, orient=VERTICAL)

        self.sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        # ==== Bill Area ========
        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=140, height=330, width=410)
        lbl_title2 = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange", fg="white", bd=3,relief=RIDGE).pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)

        self.bill_area = Text(bill_frame, font=("goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # =========== Images=========
        self.bill_photo = Image.open("./images/cat2.jpg")
        self.bill_photo = self.bill_photo.resize((450,300), Image.ANTIALIAS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lbl_image = Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=700, y=110)

        self.show()

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split(".")[0])
    
    def get_data(self, event):
        row = self.sales_list.curselection()
        file_name = self.sales_list.get(row)
        # print(file_name)
        self.bill_area.delete('1.0', END)
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def Search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error", "Invoice No. should be required!", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f"bill/{self.var_invoice.get()}.txt", "r")
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice No.!", parent=self.root)

    def clear(self):
        self.var_invoice.set("")
        self.bill_area.delete("1.0", END)



if __name__=='__main__':
    root = Tk()
    obj = sales(root)
    root.mainloop()