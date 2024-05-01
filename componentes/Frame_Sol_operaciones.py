from customtkinter import *
from componentes.Suma_Resta import *
from validaciones.Errors import Errors

class Solution_Operaciones:
    root : CTk
    frame_oper : CTkFrame
    solution_oper : CTkFrame
    rta_funcion : bool = []
    rta_oper = []   

    @staticmethod
    def define_root(app, frame_oper):
        Solution_Operaciones.root = app
        Solution_Operaciones.frame_oper = frame_oper

    @staticmethod
    def show_frame_sol_oper():
        Solution_Operaciones.rta_funcion = Suma_Resta.calculate_oper()