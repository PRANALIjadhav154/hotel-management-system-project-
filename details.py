from tkinter import *
from tkinter import ttk
import mysql.connector

class Details_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking Details")
        self.root.geometry("1000x500+250+200")

        title = Label(self.root, text="ALL BOOKINGS", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        title.pack(fill=X)

        # Table
        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=980, height=430)

        columns = ("contact","checkin","checkout","roomtype","roomavailable",
                  "meal","noofdays","paidtax","subtotal","total")

        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col.capitalize())
            self.table.column(col, width=90)
        self.table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    def connect_db(self):
        return mysql.connector.connect(host="localhost", user="root", password="root", database="hotel_management")

    def fetch_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room")
        rows = cursor.fetchall()
        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", END, values=row)
        conn.close()
