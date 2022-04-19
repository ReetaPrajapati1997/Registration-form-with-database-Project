from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk    # pip install pillow
import pymysql                    # pip install pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        # Set background color
        self.root.config(bg="azure1")

        # Set background image
        self.bg = ImageTk.PhotoImage(file="C:\\Users\\geeta\\PycharmProjects\\PythonTkinter\\Login_with_database\\Images\\lili1.jpg")
        bg=Label(self.root, image=self.bg).place(x=280, y=0, relheight=1, relwidth=1)

        # Left image
        self.left = ImageTk.PhotoImage(file="C:\\Users\\geeta\\PycharmProjects\\PythonTkinter\\Login_with_database\\Images\\purpose-of-life-quotes1.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)


        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        # Set Label
        title=Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # Row 1 --------------
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # Row 2 -------------
        contant = Label(frame1, text="Contant No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contant = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contant.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email ID", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # Row 3 ----------------
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)

        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly')
        self.cmb_quest['values'] = ("Select", "In what city were you born?", "What’s your favorite movie?", "What is your favorite food?", "What high school did you attend?" )
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # Row 4 ---------------
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # -------------------Terms-------------
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text=" I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=50, y=380)

        self.btn_img = ImageTk.PhotoImage(file="C:\\Users\\geeta\\PycharmProjects\\PythonTkinter\\Login_with_database\\Images\\Button1.jpg")
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420)

        # ----------------Sign In-------------------------
        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman",20), bd=0, cursor="hand2").place(x=200, y=460, width=180)

    def login_window(self):
        self.root.destroy()
        import login

    def clear(self):
        self.txt_fname.delete(0, END),
        self.txt_lname.delete(0, END),
        self.txt_contant.delete(0, END),
        self.txt_email.delete(0, END),
        self.txt_answer.delete(0, END),
        self.txt_password.delete(0, END),
        self.txt_cpassword.delete(0, END),
        self.cmb_quest.current(0)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_contant.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree our terms & conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee1 where email = %s", self.txt_email.get())
                row = cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error", "User already exist, Please try with another email ID", parent=self.root)
                else:
                    cur.execute("insert into employee1 (f_name, l_name, contact, email, question, asnwer, password) values(%s, %s, %s, %s, %s, %s, %s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contant.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                 ))

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
                

root = Tk()
obj = Register(root)
root.mainloop()






