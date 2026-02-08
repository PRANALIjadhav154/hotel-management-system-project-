from tkinter import *
from tkinter import ttk
import mysql.connector

class Report_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Report")
        self.root.geometry("700x400+300+200")

        title = Label(self.root, text="HOTEL REPORT", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        title.pack(fill=X)

        # Frame
        frame = Frame(self.root, bd=2, relief=RIDGE)
        frame.place(x=10, y=50, width=680, height=330)

        Label(frame, text="Total Revenue", font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Label(frame, text="Total Tax", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Label(frame, text="Total Subtotal", font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky=W)

        # Data
        self.total_revenue = Label(frame, font=("times new roman", 14))
        self.total_revenue.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.total_tax = Label(frame, font=("times new roman", 14))
        self.total_tax.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.total_subtotal = Label(frame, font=("times new roman", 14))
        self.total_subtotal.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        self.fetch_report()

    def connect_db(self):
        return mysql.connector.connect(host="localhost", user="root", password="root", database="hotel_management")

    def fetch_report(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total), SUM(paidtax), SUM(subtotal) FROM room")
        data = cursor.fetchone()
        self.total_revenue.config(text=data[0])
        self.total_tax.config(text=data[1])
        self.total_subtotal.config(text=data[2])
        conn.close()
