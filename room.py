from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import random

class Room_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ===== TITLE =====
        title = Label(self.root,
                      text="ROOM BOOKING",
                      font=("times new roman",30,"bold"),
                      bg="black", fg="gold")
        title.place(x=0,y=0,width=1295,height=50)

        # ===== VARIABLES =====
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = IntVar()
        self.var_paidtax = DoubleVar()
        self.var_subtotal = DoubleVar()
        self.var_total = DoubleVar()

        # ===== LEFT FRAME =====
        left_frame = LabelFrame(self.root,text="Booking Details",
                                font=("times new roman",12,"bold"),
                                bd=2,relief=RIDGE)
        left_frame.place(x=5,y=50,width=425,height=490)

        labels = ["Contact","Check-in","Check-out","Room Type","Room Available",
                  "Meal","No. of Days","Paid Tax","Subtotal","Total"]

        for i,text in enumerate(labels):
            Label(left_frame,text=text,font=("times new roman",12,"bold")).grid(row=i,column=0,padx=5,pady=5,sticky=W)

        Entry(left_frame,textvariable=self.var_contact).grid(row=0,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_checkin).grid(row=1,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_checkout).grid(row=2,column=1,padx=5,pady=5)

        roomtype_combo = ttk.Combobox(left_frame,textvariable=self.var_roomtype,state="readonly",width=18)
        roomtype_combo["values"] = ("Single","Double","Luxury")
        roomtype_combo.current(0)
        roomtype_combo.grid(row=3,column=1,padx=5,pady=5)

        roomavail_combo = ttk.Combobox(left_frame,textvariable=self.var_roomavailable,state="readonly",width=18)
        roomavail_combo["values"] = ("Yes","No")
        roomavail_combo.current(0)
        roomavail_combo.grid(row=4,column=1,padx=5,pady=5)

        Entry(left_frame,textvariable=self.var_meal).grid(row=5,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_noofdays).grid(row=6,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_paidtax).grid(row=7,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_subtotal).grid(row=8,column=1,padx=5,pady=5)
        Entry(left_frame,textvariable=self.var_total).grid(row=9,column=1,padx=5,pady=5)

        # ===== BUTTON FRAME =====
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=40)

        Button(btn_frame,text="Add",width=10,bg="black",fg="gold",command=self.add_data).grid(row=0,column=0,padx=5)
        Button(btn_frame,text="Update",width=10,bg="black",fg="gold",command=self.update_data).grid(row=0,column=1,padx=5)
        Button(btn_frame,text="Delete",width=10,bg="black",fg="gold",command=self.delete_data).grid(row=0,column=2,padx=5)
        Button(btn_frame,text="Reset",width=10,bg="black",fg="gold",command=self.reset_data).grid(row=0,column=3,padx=5)

        # ===== RIGHT FRAME =====
        right_frame = LabelFrame(self.root,text="View & Search",
                                 font=("times new roman",12,"bold"),
                                 bd=2,relief=RIDGE)
        right_frame.place(x=435,y=50,width=850,height=490)

        Label(right_frame,text="Search By Contact",font=("times new roman",12,"bold"),
              bg="red",fg="white").grid(row=0,column=0,padx=5,pady=10)

        self.txt_search = Entry(right_frame,width=20)
        self.txt_search.grid(row=0,column=1,padx=5)

        Button(right_frame,text="Search",bg="black",fg="gold",command=self.search_data).grid(row=0,column=2,padx=5)
        Button(right_frame,text="Show All",bg="black",fg="gold",command=self.fetch_data).grid(row=0,column=3,padx=5)

        # ===== TABLE =====
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=50,width=830,height=400)

        columns = ("contact","checkin","checkout","roomtype","roomavailable",
                   "meal","noofdays","paidtax","subtotal","total")

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, columns=columns, show="headings",
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        for col in columns:
            self.room_table.heading(col, text=col.capitalize())
        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

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
        if self.var_contact.get() == "":
            messagebox.showerror("Error","Contact required")
            return
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO room VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(),
            self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(),
            self.var_noofdays.get(), self.var_paidtax.get(), self.var_subtotal.get(),
            self.var_total.get()
        ))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success","Room booked successfully")

    # ===== FETCH =====
    def fetch_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room")
        rows = cursor.fetchall()
        self.room_table.delete(*self.room_table.get_children())
        for row in rows:
            self.room_table.insert("", END, values=row)
        conn.close()

    # ===== GET CURSOR =====
    def get_cursor(self, event=""):
        row = self.room_table.focus()
        data = self.room_table.item(row)["values"]
        if data:
            self.var_contact.set(data[0])
            self.var_checkin.set(data[1])
            self.var_checkout.set(data[2])
            self.var_roomtype.set(data[3])
            self.var_roomavailable.set(data[4])
            self.var_meal.set(data[5])
            self.var_noofdays.set(data[6])
            self.var_paidtax.set(data[7])
            self.var_subtotal.set(data[8])
            self.var_total.set(data[9])

    # ===== UPDATE =====
    def update_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("""UPDATE room SET checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s,
                          meal=%s, noofdays=%s, paidtax=%s, subtotal=%s, total=%s
                          WHERE contact=%s""",(
            self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
            self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(),
            self.var_paidtax.get(), self.var_subtotal.get(), self.var_total.get(),
            self.var_contact.get()
        ))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Update","Booking Updated")

    # ===== DELETE =====
    def delete_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM room WHERE contact=%s", (self.var_contact.get(),))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Booking Deleted")

    # ===== RESET =====
    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("Single")
        self.var_roomavailable.set("Yes")
        self.var_meal.set("")
        self.var_noofdays.set(0)
        self.var_paidtax.set(0.0)
        self.var_subtotal.set(0.0)
        self.var_total.set(0.0)

    # ===== SEARCH =====
    def search_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room WHERE contact=%s", (self.txt_search.get(),))
        rows = cursor.fetchall()
        self.room_table.delete(*self.room_table.get_children())
        for row in rows:
            self.room_table.insert("", END, values=row)
        conn.close()


# ===== RUN =====
if __name__=="__main__":
    root = Tk()
    obj = Room_Win(root)
    root.mainloop()
