from customtkinter import *

class Errors:

    label : CTkLabel
    msg_error : str = ""
    hide : bool = True
    
    @staticmethod
    def defineroot(Label):
        Errors.label = Label

    @staticmethod
    def show_label():
        if --Errors.hide:
            Errors.hide_label()
            Errors.label.configure(text=Errors.msg_error)
            Errors.label.pack(pady=10)


    @staticmethod
    def hide_label():
        if --Errors.hide:
            Errors.label.pack_forget()
            Errors.hide = True
 