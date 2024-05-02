
from customtkinter import *
from .Determinante import *
from validaciones.Errors import Errors

class Solution_determinante:
    root : CTk
    frame_def_determinante : CTkFrame
    solution_det : CTkFrame
    rta_funcion = []
    rta_det = " "

    @staticmethod
    def define_root(app, frame_det):
        Solution_determinante.root = app
        Solution_determinante.frame_def_determinante = frame_det

    @staticmethod
    def show_frame_sol_det():
        Solution_determinante.rta_funcion = Determinante.calculate_det()
        if Solution_determinante.rta_funcion[0]:
            Solution_determinante.rta_det = Solution_determinante.rta_funcion[1]
            Errors.hide_label()
            Solution_determinante.create_frame()
            Solution_determinante.solution_det.pack(fill="both", expand=1)
            Solution_determinante.frame_def_determinante.pack_forget()
        else:
            
            Errors.show_label()        

    @staticmethod
    def toBack():
        Solution_determinante.frame_def_determinante.pack(fill="both", expand=1)
        Solution_determinante.solution_det.pack_forget()
     
    @staticmethod
    def create_frame():
        
        Solution_determinante.solution_det = CTkFrame(Solution_determinante.root, border_width=3, corner_radius=10) #fg_color="LightBlue3",

        bt = CTkButton(Solution_determinante.solution_det, text="Back", width=40, command=Solution_determinante.toBack)
        bt.place(x=10, y=10)

        label_sol = CTkLabel(Solution_determinante.solution_det, text="El determinante es:", font=("Arial",22), fg_color="azure", text_color="black", corner_radius=10)
        label_sol.pack(ipadx=8, ipady=8, pady=50)

        label_rta = CTkLabel(Solution_determinante.solution_det, text=Solution_determinante.rta_det, width=150, height=50, corner_radius=10, fg_color="turquoise4", font=("Arial",24))
        label_rta.pack(ipadx=20, ipady=20)
        