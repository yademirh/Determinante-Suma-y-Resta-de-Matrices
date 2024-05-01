from customtkinter import *

class Targets:

    root : CTkFrame
    
    @staticmethod
    def defineroot(frame:CTkFrame):
        Targets.root = frame
        pass

    @staticmethod
    def show_msg_error(msg: str):
        label_error = CTkLabel(Targets.root, text=msg, text_color="red", fg_color="")
        pass