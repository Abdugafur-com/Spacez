import tkinter as tk
from tkinter import PhotoImage


class SampleAPP(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, EndPage, ChooseBack):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('Diagnostik')
        self.controller.state('zoomed')
        self.controller.geometry('1250x650')
        self.controller.resizable(0, 0)


        self.backGroundImage = PhotoImage(file=r"images/diagnostik1.png")
        self.backGroundImage_Label = tk.Label(self, width=1350, height=800, image=self.backGroundImage)
        self.backGroundImage_Label.place(x=0, y=0)

        big_label = tk.Label(self, text=('Diagnostik Center'), font=('Bernard MT Condensed', 50, 'bold'), fg="blue"
                              , bg="#fff")
        big_label.pack(pady=40)


        login_label = tk.Label(self, text="ENTER YOUR LOGIN", font=('Bernard MT Condensed', 15, 'bold'), fg="blue",
                               bg="#fff")
        login_label.pack()

        my_login = tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, font=('Bernard MT Condensed', 15, 'bold'), fg="green",
                               bg="#fff")
        login_entry.pack(pady=30)


        password_label = tk.Label(self, text="ENTER YOUR PASSWORD", font=('Bernard MT Condensed', 15, 'bold'),
                                  fg="blue", bg="#fff")
        password_label.pack(pady=30)

        my_password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font=('Bernard MT Condensed', 15, 'bold'), fg="green",
                                  bg="#fff")
        password_entry.pack()

        def check_password():
            if my_password.get() == "0102" and my_login.get() == "Fayoza" :
                controller.show_frame('ChooseBack')

            elif my_password.get() == "0102" and my_login.get() == "Fayoza" :
                right_label['text'] = "Wrong passport "
            elif my_password.get() != "0102" and my_login.get() == "Fayoza" :
                right_label['text'] = "Wrong password "
            elif my_password.get() == "0102" and my_login.get() != "Fayoza" :
                right_label['text'] = "Wrong login "
            elif my_password.get() == "" and my_login.get() == "" :
                right_label['text'] = "FILL IN THE BLANKS!!! "
            else:
                right_label['text'] = "Wrong login or password "

        password_button = tk.Button(self, text="enter", command=check_password,
                                    font=('Bernard MT Condensed', 15, 'bold'), fg="blue", bg="#fff", width='25')

        password_button.pack(pady=40)
        right_label = tk.Label(self, font=('Bernard MT Condensed', 50, 'bold'), fg="red", bg="#eee")
        right_label.pack()

class ChooseBack(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r"images/diagnostik2.png")
        self.backGroundImage_Label = tk.Label(self, width=1350, height=800, image=self.backGroundImage)
        self.backGroundImage_Label.place(x=0, y=0)
        def return_page():
            controller.show_frame('StartPage')

        return_button = tk.Button(self, text="Orqaga", command=return_page,
                                  font=('Bernard MT Condensed', 15, 'bold'), fg="blue", bg="#fff")
        return_button.pack()
        def choose_Omg():
            controller.show_frame('MenuPage')
        cash_button = tk.Button(self, text="Information", command=choose_Omg,
                                font=('Bernard MT Condensed', 40, 'bold'), fg="#333", bg="orange", width='20')
        cash_button.pack(pady=50)

        def choose_contact():
            controller.show_frame('EndPage')
        cash_button = tk.Button(self, text="Contact", command=choose_contact,
                                font=('Bernard MT Condensed', 40, 'bold'), fg="#333", bg="green", width='20')
        cash_button.pack(pady=50)





class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r"images/diagnostik.png")
        self.backGroundImage_Label = tk.Label(self, width=1350, height=800, image=self.backGroundImage)
        self.backGroundImage_Label.place(x=0, y=0)
        big_lable = tk.Label(self, text="Diagnostik", font=('Bernard MT Condensed', 50, 'bold'),
                             fg="#fff", bg="blue")
        big_lable.place(x=0 ,y=0)

        def return_page():
            controller.show_frame('ChooseBack')

        return_button = tk.Button(self, text="Orqaga", command=return_page,
                                  font=('Bernard MT Condensed', 15, 'bold'), fg="blue", bg="#fff")
        return_button.pack()

        in_money_label = tk.Label(self, text="treatment type", font=('Bernard MT Condensed', 15, 'bold'),
                                  fg="blue", bg="#fff")
        in_money_label.place(x=100,y=100)
        in_money = tk.StringVar()

        in_money_entry = tk.Entry(self, textvariable=in_money, font=('Bernard MT Condensed', 15, 'bold'), fg="green", bg="#fff")
        in_money_entry.place(x=100, y=150)

        def choose_diagnostik():
            global new_cash
            if in_money.get()=="fullbody"and my_cash.get()=="fast":
                new_cash = int(2) * int(250000)
                cash_label['text'] = new_cash
            elif in_money.get()=="foot"and my_cash.get()=="fast":
                new_cash = int(2) * int(120000)
                cash_label['text'] = new_cash
            elif in_money.get()=="hand"and my_cash.get()=="fast":
                new_cash = int(2) * int(80000)
                cash_label['text'] = new_cash
            elif in_money.get()=="head" and my_cash.get()=="fast":
                new_cash = int(2) * int(180000)
                cash_label['text'] = new_cash
            elif in_money.get()=="fullbody"and my_cash.get()=="normal":
                new_cash = int(1) * int(250000)
                cash_label['text'] = new_cash
            elif in_money.get()=="foot"and my_cash.get()=="normal":
                new_cash = int(1) * int(120000)
                cash_label['text'] = new_cash
            elif in_money.get()=="hand"and my_cash.get()=="normal":
                new_cash = int(1) * int(80000)
                cash_label['text'] = new_cash
            elif in_money.get()=="head" and my_cash.get()=="normal":
                new_cash = int(1) * int(180000)
                cash_label['text'] = new_cash
            else :
                new_cash = int(0)
                cash_label['text'] = new_cash
        cash_label = tk.Label(self, text="time", font=('Bernard MT Condensed', 15, 'bold'),
                      fg="blue", bg="#fff")
        cash_label.place(x=100 , y=250)
        my_cash = tk.StringVar()
        cash_entry = tk.Entry(self, textvariable=my_cash, font=('Bernard MT Condensed', 15, 'bold'), fg="green", bg="#fff")
        cash_entry.place(x=100, y=300)


        cash_label = tk.Label(self, font=('Bernard MT Condensed', 40, 'bold'),
                      fg="#fff", bg="blue")
        cash_label.place(x=100,y=550)

        cash_button = tk.Button(self, text="enter", command=choose_diagnostik,
                        font=('Bernard MT Condensed', 15, 'bold'), fg="blue", bg="#fff", width='25')
        cash_button.place(x=100, y=400)

        text1_label = tk.Label(self, text="fullbody:250000", font=('Bernard MT Condensed', 25, 'bold'),
                              fg="blue", bg="#fff")
        text1_label.place(x=800, y=100)
        text2_label = tk.Label(self, text="foot:    120000", font=('Bernard MT Condensed', 25, 'bold'),
                              fg="blue", bg="#fff")
        text2_label.place(x=800, y=200)
        text3_label = tk.Label(self, text="hand:     80000", font=('Bernard MT Condensed', 25, 'bold'),
                              fg="blue", bg="#fff")
        text3_label.place(x=800, y=300)
        text4_label = tk.Label(self, text="head:    180000", font=('Bernard MT Condensed', 25, 'bold'),
                              fg="blue", bg="#fff")
        text4_label.place(x=800, y=400)
        text5_label = tk.Label(self, text="Time", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="#fff", bg="blue")
        text5_label.place(x=800, y=520)
        text6_label = tk.Label(self, text="fast: equal", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="#fff", bg="blue")
        text6_label.place(x=800, y=600)
        text7_label = tk.Label(self, text="normal", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="#fff", bg="blue")
        text7_label.place(x=800, y=650)
class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#FF7578")
        self.controller = controller
        self.controller.title('Diagnostik')

        self.backGroundImage = PhotoImage(file=r"images/diagnostik3.png")
        self.backGroundImage_Label = tk.Label(self, width=1350, height=800, image=self.backGroundImage)
        self.backGroundImage_Label.place(x=0, y=0)
        big_lable = tk.Label(self, text="Contact", font=('Bernard MT Condensed', 50, 'bold'), fg="green",
                             bg="#fff")
        big_lable.place(x=0 , y=0)

        def return_page():
            controller.show_frame('ChooseBack')

        return_button = tk.Button(self, text="Orqaga", command=return_page,
                                  font=('Bernard MT Condensed', 15, 'bold'), fg="green", bg="#fff")
        return_button.pack()


        text1_label = tk.Label(self, text="Address:", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="#000", bg="#fff")
        text1_label.pack(pady=50)
        text2_label = tk.Label(self, text="Toshkent city, Yunus-Obod, Hamza Street", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="blue", bg="#fff")
        text2_label.pack()
        text3_label = tk.Label(self, text="Number:+998712202002", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="blue", bg="#fff")
        text3_label.pack(pady=70)
        text4_label = tk.Label(self, text="Email:diagnostik@mail.uz", font=('Bernard MT Condensed', 25, 'bold'),
                               fg="blue", bg="#fff")
        text4_label.pack(pady=50)

if __name__== "__main__":
    app = SampleAPP()
    app.mainloop()