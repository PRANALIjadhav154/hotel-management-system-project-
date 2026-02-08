from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Room_Win
from details import Details_Win
from report import Report_Win


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ===== HEADER IMAGE =====
        img1 = Image.open(r"C:\Users\HOME\OneDrive\Desktop\image download\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ===== LOGO =====
        img2 = Image.open(r"C:\Users\HOME\OneDrive\Desktop\image download\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_logo = Label(self.root, image=self.photoimg2)
        lbl_logo.place(x=0, y=0, width=230, height=140)

        # ===== TITLE =====
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM",
                          font=("Times New Roman", 40, "bold"),
                          bg="black", fg="gold", bd=4, relief=RAISED)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ===== MAIN FRAME =====
        self.main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        self.main_frame.place(x=0, y=190, width=1550, height=620)

        # ===== MENU TITLE =====
        lbl_menu = Label(self.main_frame, text="MENU",
                         font=("Times New Roman", 20, "bold"),
                         bg="black", fg="gold", bd=4, relief=RAISED)
        lbl_menu.place(x=0, y=0, width=230)

        # ===== BUTTON FRAME =====
        self.btn_frame = Frame(self.main_frame, bd=2, relief=RIDGE, bg="black")
        self.btn_frame.place(x=0, y=45, width=230, height=250)

        # ===== BUTTONS =====
        self.create_buttons()

        # ===== CENTER IMAGE =====
        img3 = Image.open(r"C:\Users\HOME\OneDrive\Desktop\image download\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.main_frame, image=self.photoimg3)
        lblimg.place(x=230, y=0, width=1310, height=590)

        # ===== SIDE IMAGES =====
        side_images = [
            (r"C:\Users\HOME\OneDrive\Desktop\image download\hotel images\myh.jpg", (230, 210), 260),
            (r"C:\Users\HOME\OneDrive\Desktop\image download\hotel images\khana.jpg", (230, 190), 470)
        ]

        self.side_photo_images = []
        for path, size, y in side_images:
            img = Image.open(path).resize(size, Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.side_photo_images.append(photo)
            lbl = Label(self.main_frame, image=photo)
            lbl.place(x=0, y=y, width=size[0], height=size[1])

    # ===== CREATE BUTTONS FUNCTION =====
    def create_buttons(self):
        cust_btn = Button(self.btn_frame, text="CUSTOMER", width=22,
                          command=self.cust_details,
                          font=("Times New Roman", 14, "bold"),
                          bg="black", fg="gold", bd=3, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(self.btn_frame, text="ROOM", width=22,
                          command=self.room_details,
                          font=("Times New Roman", 14, "bold"),
                          bg="black", fg="gold", bd=3, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(self.btn_frame, text="DETAILS", width=22,
                             command=self.details_window,
                             font=("Times New Roman", 14, "bold"),
                             bg="black", fg="gold", bd=3, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(self.btn_frame, text="REPORT", width=22,
                            command=self.report_window,
                            font=("Times New Roman", 14, "bold"),
                            bg="black", fg="gold", bd=3, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(self.btn_frame, text="LOGOUT", width=22,
                            font=("Times New Roman", 14, "bold"),
                            bg="black", fg="gold", bd=3, cursor="hand2",
                            command=self.root.destroy)
        logout_btn.grid(row=4, column=0, pady=1)

    # ===== CUSTOMER WINDOW =====
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    # ===== ROOM WINDOW =====
    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Win(self.new_window)

    # ===== DETAILS WINDOW =====
    def details_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Details_Win(self.new_window)

    # ===== REPORT WINDOW =====
    def report_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Report_Win(self.new_window)


# ===== MAIN =====
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
