from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Harsh Sharma")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========= All Variables ==========
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # == Search Frame =====
        # searchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE)
        # searchFrame.place(x=250, y=20, width=600, height=70)

        # ==== Options ==========
        lbl_search = Label(self.root, text="Invoice No. ", font=("goudy old style", 15), bg="white")
        lbl_search.place(x=700, y=80)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=805, y=80, width=150)
        btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=960, y=77, width=120, height=30)

        # === title ====
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").place(x=50, y=10, width=1000, height=40)

        # ===== Content =====
        # ==== row1 ======
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50, y=80)
        
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=80, width=180)
        # txt_gender = Entry(self.root, textvariable=self.var_gender,   font=("goudy old style", 15), bg="white").place(x=500, y=150, width=180)
        

        # Row 2
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=120, width=180)

        # Row 3

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=160, width=180)
        

        # Row 4
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=200)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=470, height=90)
        
        # ==Buttons==
        
        btn_add = Button(self.root, text="Save", command=self.add, font=("oudy old style", 15), bg="#2196f3", fg="white", cursor='hand2').place(x=180, y=350, width=110, height=35)
        btn_update = Button(self.root, text="Update", command=self.update, font=("oudy old style", 15), bg="#4caf50", fg="white", cursor='hand2').place(x=300, y=350, width=110, height=35)
        btn_delete = Button(self.root, text="Delete", font=("oudy old style", 15), command=self.delete, bg="#f44336", fg="white", cursor='hand2').place(x=420, y=350, width=110, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("oudy old style", 15), bg="#607f8b", fg="white", cursor='hand2').place(x=540, y=350, width=110, height=35)

        # ====== Employee Details ==========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=700, y=120, width=380, height=370)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice","name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.supplierTable.yview)
        scrollx.config(command=self.supplierTable.xview)

        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()
        

# =================================================================================
    def add(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. is Required!", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(), ))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice No. is already assigned, try different one.")
                else:
                    cur.execute("Insert into supplier(invoice, name, contact, desc) values(?,?,?,?)", 
                    (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                     ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully.", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice is empty!")
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("update supplier set name=?, contact=?, desc=? where invoice=?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully!")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def delete(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice No. is Required!", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_sup_invoice.get(), ))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(), ))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier Deleted Successfully", parent=self.root)
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Invoice No. Should be Required!", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(), ))
                row = cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=='__main__':
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()