from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import category
from product import product
from sales import sales

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Harsh Sharma")
        self.root.config(bg="white")

        #====== title =======
        self.icon_title  = Image.open("./images/logo1.png")
        self.icon_title = self.icon_title.resize((60,60), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        
        title = Label(self.root, text="Inventory Management System",image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        #====== button logout ==========
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
        #=====clock====
        self.lbl_clock=Label(self.root, text="Welcome to Inventory Management System\t\tDate : DD-MM-YYYY\t\tTime : HH:MM:SS", font=("times new roman",15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1, height=30)

        #======= Left Menu ===========
        self.MenuLogo = Image.open("./images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menulogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP, fill=X)

        self.icon_side = Image.open("./images/side.png")
        self.icon_side = self.icon_side.resize((40,40), Image.ANTIALIAS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP, fill=X)

        lbl_employee = Button(LeftMenu, text="Employee", image=self.icon_side, compound=LEFT, command=self.employee, font=("times new roman", 20, "bold"), padx=5, anchor="w", bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        lbl_supplier = Button(LeftMenu, text="Supplier", command=self.supplier, image=self.icon_side, compound=LEFT, font=("times new roman", 20, "bold"), padx=5, anchor="w", bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        lbl_category = Button(LeftMenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT, font=("times new roman", 20, "bold"), padx=5, anchor="w", bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        lbl_products = Button(LeftMenu, text="Products", command=self.product, image=self.icon_side, compound=LEFT, font=("times new roman", 20, "bold"), padx=5, anchor="w", bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        lbl_sales = Button(LeftMenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT, font=("times new roman", 20, "bold"), padx=5, anchor="w", bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)
        lbl_exit = Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT, font=("times new roman", 20, "bold"), padx=5, anchor="w", bg="white",bd=3, cursor="hand2").pack(side=TOP, fill=X)


        # ======== Content =========
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", font=("goudy old style",20,"bold"), bg="#33bbf9", fg="white", bd=5, relief=RIDGE)
        self.lbl_employee.place(x=300,y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", font=("goudy old style",20,"bold"), bg="#ff5722", fg="white", bd=5, relief=RIDGE)
        self.lbl_supplier.place(x=650,y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", font=("goudy old style",20,"bold"), bg="#009688", fg="white", bd=5, relief=RIDGE)
        self.lbl_category.place(x=1000,y=120, height=150, width=300)

        self.lbl_products = Label(self.root, text="Total Products\n[ 0 ]", font=("goudy old style",20,"bold"), bg="#307d8b", fg="white", bd=5, relief=RIDGE)
        self.lbl_products.place(x=300,y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", font=("goudy old style",20,"bold"), bg="#ffc107", fg="white", bd=5, relief=RIDGE)
        self.lbl_sales.place(x=650,y=300, height=150, width=300)

        # ====== Footer ======
        self.lbl_footer=Label(self.root, text="IMS-Inventory Management System | Developed By HARSH SHARMA\n For any Texhnical Issue Contact : 987654321", font=("times new roman",10), bg="#4d636d", fg="white")
        self.lbl_footer.pack(side=BOTTOM, fill=X)

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = category(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = product(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = sales(self.new_win)

if __name__=='__main__':
    root = Tk()
    obj = IMS(root)
    root.mainloop()