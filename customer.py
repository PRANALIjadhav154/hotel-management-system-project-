from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ===== HEADER IMAGE =====
        img1 = Image.open(r"C:\Users\HOME\OneDrive\Desktop\image download\hotel images\logohotel.png")   # logo file same folder me rakho
        img1 = img1.resize((200,80))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=0)
        lblimg.place(x=0, y=0, width=200, height=80)

    # ===== HEADER TITLE =====
        title = Label(self.root,
                      text="HOTEL MANAGEMENT SYSTEM",
                      font=("times new roman",30,"bold"),
                      bg="black", fg="gold")
        title.place(x=200,y=0,width=1095,height=80)


        lbl_title = Label(self.root,text="CUSTOMER DETAILS",
                          font=("times new roman",23,"bold"),
                          bg="black",fg="white")
        lbl_title.place(x=0,y=80,width=1295,height=40)

        # ===== VARIABLES =====
        self.var_ref = StringVar()
        self.var_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        # ===== LEFT FRAME =====
        left_frame = LabelFrame(self.root,text="Customer Details",
                                font=("times new roman",12,"bold"),
                                bd=2,relief=RIDGE)
        left_frame.place(x=5,y=130,width=425,height=420)

        labels = ["Customer Ref","Name","Mother Name","Gender","Post Code",
                  "Mobile","Email","Nationality","ID Proof","ID Number","Address"]

        for i,text in enumerate(labels):
            Label(left_frame,text=text,font=("times new roman",12,"bold")).grid(row=i,column=0,padx=5,pady=5,sticky=W)

        Entry(left_frame,textvariable=self.var_ref,state="readonly").grid(row=0,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_name).grid(row=1,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_mother).grid(row=2,column=1,padx=5,pady=5)

        gender_combo=ttk.Combobox(left_frame,textvariable=self.var_gender,state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=5,pady=5)

        Entry(left_frame,textvariable=self.var_post).grid(row=4,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_mobile).grid(row=5,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_email).grid(row=6,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_nationality).grid(row=7,column=1,padx=5,pady=5)

        id_combo=ttk.Combobox(left_frame,textvariable=self.var_idproof,state="readonly",width=18)
        id_combo["values"]=("Aadhar","PAN","Driving License","Passport")
        id_combo.current(0)
        id_combo.grid(row=8,column=1,padx=5,pady=5)

        Entry(left_frame,textvariable=self.var_idnumber).grid(row=9,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_address).grid(row=10,column=1,padx=5,pady=5)

        # ===== BUTTON FRAME =====
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=360,width=412,height=40)

        Button(btn_frame,text="Add",width=10,bg="black",fg="gold",
               command=self.add_data).grid(row=0,column=0,padx=5)

        Button(btn_frame,text="Update",width=10,bg="black",fg="gold",
               command=self.update_data).grid(row=0,column=1,padx=5)

        Button(btn_frame,text="Delete",width=10,bg="black",fg="gold",
               command=self.delete_data).grid(row=0,column=2,padx=5)

        Button(btn_frame,text="Reset",width=10,bg="black",fg="gold",
               command=self.reset_data).grid(row=0,column=3,padx=5)

        # ===== RIGHT FRAME =====
        right_frame = LabelFrame(self.root,text="View & Search",
                                 font=("times new roman",12,"bold"),
                                 bd=2,relief=RIDGE)
        right_frame.place(x=435,y=130,width=850,height=420)

        Label(right_frame,text="Search By",font=("times new roman",12,"bold"),
              bg="red",fg="white").grid(row=0,column=0,padx=5,pady=10)

        self.combo_search=ttk.Combobox(right_frame,width=15,state="readonly")
        self.combo_search["values"]=("Mobile","Ref")
        self.combo_search.current(0)
        self.combo_search.grid(row=0,column=1,padx=5)

        self.txt_search=Entry(right_frame,width=20)
        self.txt_search.grid(row=0,column=2,padx=5)

        Button(right_frame,text="Search",bg="black",fg="gold",
               command=self.search_data).grid(row=0,column=3,padx=5)

        Button(right_frame,text="Show All",bg="black",fg="gold",
               command=self.fetch_data).grid(row=0,column=4,padx=5)

        # ===== TABLE =====
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=50,width=830,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.cust_table=ttk.Treeview(table_frame,
            columns=("ref","name","mother","gender","post","mobile","email","nation","idproof","idnumber","address"),
            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_table.xview)
        scroll_y.config(command=self.cust_table.yview)

        headings=["Ref","Name","Mother","Gender","Post","Mobile","Email","Nationality","ID Proof","ID Number","Address"]
        for i,h in enumerate(headings):
            self.cust_table.heading(i,text=h)

        self.cust_table["show"]="headings"
        self.cust_table.pack(fill=BOTH,expand=1)
        self.cust_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ===== DB CONNECT =====
    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="hotel_management"
        )

    # ===== ADD =====
    def add_data(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","Name required")
            return
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_ref.get(),self.var_name.get(),self.var_mother.get(),
            self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),
            self.var_email.get(),self.var_nationality.get(),
            self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get()))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success","Customer Added")

    # ===== FETCH =====
    def fetch_data(self):
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("select * from customer")
        rows=cursor.fetchall()
        self.cust_table.delete(*self.cust_table.get_children())
        for row in rows:
            self.cust_table.insert("",END,values=row)
        conn.close()

    def get_cursor(self,event=""):
        row=self.cust_table.focus()
        data=self.cust_table.item(row)["values"]
        if data:
            self.var_ref.set(data[0])
            self.var_name.set(data[1])
            self.var_mother.set(data[2])
            self.var_gender.set(data[3])
            self.var_post.set(data[4])
            self.var_mobile.set(data[5])
            self.var_email.set(data[6])
            self.var_nationality.set(data[7])
            self.var_idproof.set(data[8])
            self.var_idnumber.set(data[9])
            self.var_address.set(data[10])

    def update_data(self):
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("""update customer set name=%s,mother=%s,gender=%s,post=%s,
        mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s""",(
        self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),
        self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),
        self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get(),self.var_ref.get()))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Update","Customer Updated")

    def delete_data(self):
        conn=self.connect_db()
        cursor=conn.cursor()
        cursor.execute("delete from customer where ref=%s",(self.var_ref.get(),))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Customer Deleted")

    def reset_data(self):
        self.var_name.set("")
        self.var_mobile.set("")
        self.var_ref.set(str(random.randint(1000,9999)))

    def search_data(self):
        conn=self.connect_db()
        cursor=conn.cursor()
        if self.combo_search.get()=="Mobile":
            cursor.execute("select * from customer where mobile=%s",(self.txt_search.get(),))
        else:
            cursor.execute("select * from customer where ref=%s",(self.txt_search.get(),))
        rows=cursor.fetchall()
        self.cust_table.delete(*self.cust_table.get_children())
        for row in rows:
            self.cust_table.insert("",END,values=row)
        conn.close()

# ===== RUN =====
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()

