from tkinter import *
import yagmail


def main_program(user, app_password, destination_email, subject, message):
    content = [message, ]
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(destination_email, subject, content)
        print('send...')

class Main():
    def __init__(self):
        self.win = Tk()
        
        #config
        self.config_title = 'G-sender'
        self.config_width = 450
        self.confing_heigt = 550
        self.config_resizable = [False, False]
        self.config_background = '#00a693'

        self.Load_Configs()
        self.Load_objects()

        mainloop()

    def Load_Configs(self):
        self.win.title(self.config_title)
        self.win.geometry(str(self.config_width) + 'x' + str(self.confing_heigt))
        self.win.resizable(self.config_resizable[0], self.config_resizable[1])
        self.win.config(bg = self.config_background)

    def get_info(self):
        user = self.user_input.get()
        app_password = self.pass_input.get()
        destination_email = self.to_input.get()
        subject = self.subject_input.get()
        message = self.message_input.get("1.0", "end-1c")

        main_program(user, app_password, destination_email, subject, message)

    def Load_objects(self):
        Label(
            self.win,
            text = "your email: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10) ,
        ).pack()
        user_input = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 64,
        )
        self.user_input = user_input
        user_input.pack()

        Label(
            text = " ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 8) ,
        ).pack()
        Label(
            text = "app password: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10) ,
        ).pack()
        pass_input = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 64,
        )
        self.pass_input = pass_input
        pass_input.pack()

        Label(
            text = " ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 8) ,
        ).pack()
        Label(
            text = "to: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10) ,
        ).pack()
        to_input = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 64,
        )
        self.to_input = to_input
        to_input.pack()

        Label(
            text = " ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 8) ,
        ).pack()
        Label(
            text = "subject: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10) ,
        ).pack()
        subject_input = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 64,
        )
        self.subject_input = subject_input
        subject_input.pack()

        Label(
            text = " ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 8) ,
        ).pack()
        Label(
            text = "message: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 10) ,
        ).pack()
        message_input = Text(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            height = 10,
            width = 40,
        )
        self.message_input = message_input
        message_input.pack()

        Label(
            self.win,
            text = '     ',
            background = self.config_background,
            font = ('Arial', 32)
        ).pack()

        send_button = Button(
            self.win,
            text = 'send',
            background = '#FFFFFF',
            foreground = 'black',
        )
        send_button.config(command = self.get_info)
        send_button.pack()





app = Main()