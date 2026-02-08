from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# ===== DATABASE CONFIGURATION =====
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hotel_management"
    )

# ===== LOGIN / REGISTER APP =====
class LoginRegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Login/Register")
        self.root.geometry("900x500+200+100")
        self.root.resizable(False, False)

        # ===== BACKGROUND IMAGE =====
        try:
            bg_img = Image.open("login_bg.jpg")
            bg_img = bg_img.resize((900, 500), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_img)
            lbl_bg = Label(self.root, image=self.bg_photo)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.root.configure(bg="lightblue")  # fallback

        # ===== LOGIN FRAME =====
        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=250, y=100, width=400, height=330)

        # ===== LOGO =====
        try:
            logo_img = Image.open("logohotel.png")
            logo_img = logo_img.resize((80, 80), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_img)
            lbl_logo = Label(self.frame, image=self.logo_photo, bg="white")
            lbl_logo.place(x=160, y=10)
        except:
            pass

        # ===== TITLE =====
        Label(self.frame, text="Welcome", font=("times new roman", 20, "bold"),
              bg="white", fg="black").place(x=150, y=100)

        # ===== EMAIL & PASSWORD =====
        Label(self.frame, text="Email", font=("times new roman", 12),
              bg="white", fg="black").place(x=50, y=140)
        self.email_entry = Entry(self.frame, font=("times new roman", 12))
        self.email_entry.place(x=150, y=140, width=200)

        Label(self.frame, text="Password", font=("times new roman", 12),
              bg="white", fg="black").place(x=50, y=180)
        self.password_entry = Entry(self.frame, font=("times new roman", 12), show="*")
        self.password_entry.place(x=150, y=180, width=200)

        # ===== LOGIN / REGISTER / FORGOT BUTTONS =====
        Button(self.frame, text="Login", command=self.login, bg="black", fg="gold",
               font=("times new roman", 12), cursor="hand2").place(x=150, y=220, width=90, height=30)

        Button(self.frame, text="Register", command=self.register_window, bg="black", fg="gold",
               font=("times new roman", 12), cursor="hand2").place(x=260, y=220, width=90, height=30)

        Button(self.frame, text="Forgot Password?", command=self.forgot_password_window, bg="white", fg="black",
               font=("times new roman", 13, "underline"), bd=0, cursor="hand2").place(x=150, y=260)

    # ===== LOGIN FUNCTION =====
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
            row = cursor.fetchone()
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")
            return

        if row:
            messagebox.showinfo("Success", f"Welcome {row[1]}!")
            self.root.destroy()  # close login window

            # ===== Open HotelManagementSystem =====
            try:
                from hotel import HotelManagementSystem
                main_root = Tk()
                app = HotelManagementSystem(main_root)
                main_root.mainloop()
            except ImportError:
                messagebox.showerror("Error", "hotel.py file not found or HotelManagementSystem missing!")
        else:
            messagebox.showerror("Error", "Invalid email or password")

    # ===== REGISTER WINDOW =====
    def register_window(self):
        self.reg_win = Toplevel(self.root)
        self.reg_win.title("Register New User")
        self.reg_win.geometry("400x350+300+150")
        self.reg_win.configure(bg="white")
        self.reg_win.resizable(False, False)

        Label(self.reg_win, text="Name", bg="white", font=("times new roman", 12)).place(x=50, y=50)
        self.name_entry = Entry(self.reg_win, font=("times new roman", 12))
        self.name_entry.place(x=150, y=50, width=200)

        Label(self.reg_win, text="Email", bg="white", font=("times new roman", 12)).place(x=50, y=100)
        self.reg_email = Entry(self.reg_win, font=("times new roman", 12))
        self.reg_email.place(x=150, y=100, width=200)

        Label(self.reg_win, text="Password", bg="white", font=("times new roman", 12)).place(x=50, y=150)
        self.reg_password = Entry(self.reg_win, font=("times new roman", 12), show="*")
        self.reg_password.place(x=150, y=150, width=200)

        Button(self.reg_win, text="Register", command=self.register_user, bg="black", fg="gold",
               font=("times new roman", 12), cursor="hand2").place(x=150, y=200, width=100, height=30)

    # ===== REGISTER FUNCTION =====
    def register_user(self):
        name = self.name_entry.get()
        email = self.reg_email.get()
        password = self.reg_password.get()

        if name == "" or email == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                           (name, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful!")
            self.reg_win.destroy()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    # ===== FORGOT PASSWORD WINDOW =====
    def forgot_password_window(self):
        self.forgot_win = Toplevel(self.root)
        self.forgot_win.title("Forgot Password")
        self.forgot_win.geometry("400x250+300+180")
        self.forgot_win.configure(bg="white")
        self.forgot_win.resizable(False, False)

        Label(self.forgot_win, text="Enter your Email", bg="white", font=("times new roman", 12)).place(x=50, y=50)
        self.forgot_email = Entry(self.forgot_win, font=("times new roman", 12))
        self.forgot_email.place(x=180, y=50, width=180)

        Button(self.forgot_win, text="Get Password", command=self.get_password, bg="black", fg="gold",
               font=("times new roman", 12), cursor="hand2").place(x=150, y=120, width=120, height=30)

    # ===== GET PASSWORD FUNCTION =====
    def get_password(self):
        email = self.forgot_email.get()
        if email == "":
            messagebox.showerror("Error", "Please enter your email")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
            row = cursor.fetchone()
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")
            return

        if row:
            messagebox.showinfo("Password", f"Your password is: {row[0]}")
            self.forgot_win.destroy()
        else:
            messagebox.showerror("Error", "Email not found")


# ===== RUN APP =====
if __name__ == "__main__":
    root = Tk()
    app = LoginRegisterApp(root)
    root.mainloop()
