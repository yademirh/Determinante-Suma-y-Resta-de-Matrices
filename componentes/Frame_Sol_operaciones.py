from customtkinter import *
from componentes.Suma_Resta import *
from validaciones.Errors import Errors
from .Matriz import Matriz


class Solution_Operaciones:
    root: CTk
    frame_oper: CTkFrame
    solution_oper: CTkFrame
    rta_funcion: bool = []
    rta_oper = []

    @staticmethod
    def define_root(app, frame_oper):
        Solution_Operaciones.root = app
        Solution_Operaciones.frame_oper = frame_oper

    @staticmethod
    def show_frame_sol_oper_sum():
        Suma_Resta.band = True
        Solution_Operaciones.rta_funcion, Solution_Operaciones.rta_oper = Suma_Resta.calculate_oper()
        if Solution_Operaciones.rta_funcion:
            Errors.hide_label_oper()
            Solution_Operaciones.create_frame()
            Solution_Operaciones.solution_oper.pack(fill="both", expand=1)
            Solution_Operaciones.frame_oper.pack_forget()

        else:
            Errors.show_label_oper()

    @staticmethod
    def show_frame_sol_oper_rest():
        Suma_Resta.band = False
        Solution_Operaciones.rta_funcion, Solution_Operaciones.rta_oper = Suma_Resta.calculate_oper()
        if Solution_Operaciones.rta_funcion:
            Errors.hide_label_oper()
            Solution_Operaciones.create_frame()
            Solution_Operaciones.solution_oper.pack(fill="both", expand=1)
            Solution_Operaciones.frame_oper.pack_forget()

        else:
            Errors.show_label_oper()

    @staticmethod
    def toBack():
        Solution_Operaciones.frame_oper.pack(fill="both", expand=1)
        Solution_Operaciones.solution_oper.pack_forget()

    @staticmethod
    def create_frame():
        Solution_Operaciones.solution_oper = CTkFrame(
            Solution_Operaciones.root, border_width=3, corner_radius=10
        )

        bt = CTkButton(
            Solution_Operaciones.solution_oper,
            text="Back",
            width=40,
            command=Solution_Operaciones.toBack,
        )
        bt.place(x=10, y=10)

        label_sol = CTkLabel(
            Solution_Operaciones.solution_oper,
            text="La matriz resultante es:",
            font=("Arial", 22),
            fg_color="LightBlue3",
            text_color="black",
            corner_radius=10,
        )
        label_sol.pack(ipadx=8, ipady=8, pady=50)

        frame_sol = CTkFrame(Solution_Operaciones.solution_oper, fg_color="turquoise4",)
        frame_sol.pack()

        Matriz.show_matriz_sol(
            frame_sol,
            Suma_Resta.row,
            Suma_Resta.column,
            Solution_Operaciones.rta_oper,
        )
