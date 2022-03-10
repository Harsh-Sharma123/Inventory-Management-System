from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import category
from product import product
from sales import sales
from tkinter import ttk

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Harsh Sharma")
        self.root.config(bg="white")

        # ====== Variables ========
        self.var_search = StringVar() 
        self.var_cname = StringVar()
        self.var_contact = StringVar()

        #====== title =======
        self.icon_title  = Image.open("./images/logo1.png")
        self.icon_title = self.icon_title.resize((60,60), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        #====== button logout ==========
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
        #=====clock====
        self.lbl_clock=Label(self.root, text="Welcome to Inventory Management System\t\tDate : DD-MM-YYYY\t\tTime : HH:MM:SS", font=("times new roman",15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70,  relwidth=1, height=30)

        # === Product Frame =======
        productFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        productFrame1.place(x=6, y=110, width=410, height=550)

        ptitle = Label(productFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)

        productFrame2 = Frame(productFrame1, bd=4, relief=RIDGE, bg="white")
        productFrame2.place(x=6, y=42, width=394, height=90)

        lbl_search = Label(productFrame2, text="Search Product | By Name", font=("times new roman", 15, "bold"), fg="green", bg="white").place(x=2, y=5)
        lbl_name = Label(productFrame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white").place(x=2, y=45)
        txt_search = Entry(productFrame2, textvariable=self.var_search, font=("times new roman", 15), bg="lightyellow").place(x=130, y=48, width=150, height=22)
        btn_search = Button(productFrame2, text="Search", font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=285, y=47, width=100, height=25)
        btn_show = Button(productFrame2, text="Show All", font=("goudy old style", 15), bg="#083531", fg="white", cursor="hand2").place(x=285, y=15, width=100, height=25)


        productFrame3 = Frame(productFrame1, bd=3, relief=RIDGE)
        productFrame3.place(x=2, y=140, width=398, height=385)

        scrolly = Scrollbar(productFrame3, orient=VERTICAL)
        scrollx = Scrollbar(productFrame3, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(productFrame3, columns=("pid","name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.product_table.yview)
        scrollx.config(command=self.product_table.xview)

        self.product_table.heading("pid",text="PID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Qty")
        self.product_table.heading("status",text="Status")

        self.product_table["show"]="headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status", width=100)

        self.product_table.pack(fill=BOTH, expand=1)
        # self.product_table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note = Label(productFrame1, text="Note : Enter 0 quantity to remove product from the Cart.", font=("goudy old style", 12), bg="white", fg="red").pack(side=BOTTOM, fill=X)

        # === Customer Frame ===
        CustomerFrame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)

        ctitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)
        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 15), bg="white").place(x=5, y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("times new roman", 13), bg="lightyellow").place(x=80, y=35, width=180, height=22)

        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("times new roman", 15), bg="white").place(x=270, y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13), bg="lightyellow").place(x=380, y=35, width=140, height=22)


        # == Cal Cart Frame ==
        cal_cart_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        cal_cart_Frame.place(x=420, y=190, width=530, height=360)

        # === Calculator Frame =========
        cal_Frame = Frame(cal_cart_Frame, bd=3, relief=RIDGE, bg="white")
        cal_Frame.place(x=5, y=10, width=268, height=340)


        # ======== Cart Frame =======
        cart_Frame = Frame(cal_cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=280, y=8, width=245, height=342)
        cartTitle = Label(cart_Frame, text="Cart   Total Products : [0]", font=("goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.cartTable = ttk.Treeview(cart_Frame, columns=("pid","name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.cartTable.yview)
        scrollx.config(command=self.cartTable.xview)

        self.cartTable.heading("pid",text="PID")
        self.cartTable.heading("name",text="Name")
        self.cartTable.heading("price",text="Price")
        self.cartTable.heading("qty",text="Qty")
        self.cartTable.heading("status",text="Status")

        self.cartTable["show"]="headings"

        self.cartTable.column("pid", width=40)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=100)
        self.cartTable.column("qty",width=100)
        self.cartTable.column("status",width=100)

        self.cartTable.pack(fill=BOTH, expand=1)
        # self.cartTable.bind("<ButtonRelease-1>", self.get_data)

        # ==== Add Cart Widget Frame =======

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()


        add_cart_widget_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        add_cart_widget_frame.place(x=420, y=550, width=530, height=110)

        p_name = Label(add_cart_widget_frame, text="Product Name", font=("times new roman", 15), bg="white").place(x=5, y=5)
        txt_name = Entry(add_cart_widget_frame, textvariable=self.var_pname, font=("times new roman", 15), bg="lightyellow", state="readonly").place(x=5, y=35, width=190, height=22)

        p_price = Label(add_cart_widget_frame, text="Price Per Qty", font=("times new roman", 15), bg="white").place(x=230, y=5)
        txt_price = Entry(add_cart_widget_frame, textvariable=self.var_price, font=("times new roman", 15), bg="lightyellow", state="readonly").place(x=230, y=35, width=150, height=22)

        p_qty = Label(add_cart_widget_frame, text="Qty", font=("times new roman", 15), bg="white").place(x=390, y=5)
        txt_qty = Entry(add_cart_widget_frame, textvariable=self.var_qty, font=("times new roman", 15), bg="lightyellow").place(x=390, y=35, width=150, height=22)


if __name__=='__main__':
    root = Tk()
    obj = BillClass(root)
    root.mainloop()