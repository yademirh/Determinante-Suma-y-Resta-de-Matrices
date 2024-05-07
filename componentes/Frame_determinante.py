from customtkinter import *
from .Matriz import *
from validaciones.Errors import *
from .Frame_Sol_determinante import *
from .Determinante import *


class Frame_determinante:
    root: CTk
    main: CTkFrame
    frame_def_determinante: CTkFrame
    nums: int
    array = []

    # Recibe la ventana y el frame padre
    @staticmethod
    def define_root(app: CTk, frame_main: CTkFrame):
        Frame_determinante.root = app
        Frame_determinante.main = frame_main

    # Muestra el frame y oculta al padre
    @staticmethod
    def show_frame_det():
        Frame_determinante.frame_def_determinante.pack(fill="both", expand=1)
        Frame_determinante.main.pack_forget()

    # Devolver al frame principal
    @staticmethod
    def change_destroy():
        Frame_determinante.main.pack(fill="both", expand=1)
        Frame_determinante.frame_def_determinante.pack_forget()

    # Sacar y enviar el tamaño de la matriz
    @staticmethod
    def splitChoice(choice: str):
        if choice.find("x"):
            nums = int(choice.split("x")[0])
            Determinante.row = nums
            Determinante.column = nums
            if len(Determinante.Matriz) > 0:
                Determinante.Matriz.clear()
            Matriz.createMatriz(nums, nums)

    # Crear el frame
    @staticmethod
    def create_frame():
        Frame_determinante.frame_def_determinante = CTkFrame(
            Frame_determinante.root,
            border_width=3,
            corner_radius=10,
        )

        frame_left = CTkScrollableFrame(Frame_determinante.frame_def_determinante)
        # frame_left.pack(fill="both", expand=1, side="left")
        frame_left.grid(row=0, column=0, sticky="nsew")
        frame_right = CTkFrame(Frame_determinante.frame_def_determinante)
        # frame_right.pack(fill="both", expand=1, side="left")
        frame_right.grid(row=0, column=1, sticky="nsew")

        bt = CTkButton(
            Frame_determinante.frame_def_determinante,
            text="Back",
            width=40,
            command=Frame_determinante.change_destroy,
        )
        bt.place(x=10, y=10)

        Frame_determinante.frame_def_determinante.columnconfigure(0, weight=2)
        Frame_determinante.frame_def_determinante.columnconfigure(1, weight=1)
        Frame_determinante.frame_def_determinante.rowconfigure(0,weight=1)

        container = CTkFrame(frame_left, fg_color="transparent")

        label_defineSize = CTkLabel(
            container,
            text="Define el tamaño de la matriz",
            corner_radius=5,
            fg_color="LightCyan3",
            text_color="black",
            font=("Arial", 16),
        )
        label_defineSize.grid(row=0, column=0)

        options_sizeDet = CTkComboBox(
            container,
            values=["1x1", "2x2", "3x3", "4x4", "5x5", "6x6", "7x7"],
            button_color="LightCyan3",
            dropdown_hover_color="LightCyan4",
            command=Frame_determinante.splitChoice,
            font=("Arial", 14),
        )
        options_sizeDet.grid(row=0, column=1, padx=10)
        container.pack(pady=50)

        frame_det = CTkFrame(frame_left)
        frame_det.pack()

        btn_calculate = CTkButton(
            frame_left,
            text="CALCULAR",
            command=Solution_determinante.show_frame_sol_det,
            font=("Arial", 16),
        )
        btn_calculate.pack(pady=20)

        label_aclaraciones = CTkLabel(
            frame_right,
            wraplength=200,
            text="\tNota:\nEl determinante solo está definido para matrices cuadradas",
            font=("Arial", 16),
            fg_color="CadetBlue4",
            justify="left",
            corner_radius=5,
        )
        label_aclaraciones.pack(ipady=10, ipadx=20, pady=30)

        label_instrucciones = CTkLabel(
            frame_right,
            text="          Instrucciones:\n* Permite solo el uso de punto (.) para números decimales.\n* Permite slash (/) para indicar una fraccion.\n* No permite cualquier otro tipo de caracteres ni espacio en blanco.\n* Llenar todos los campos",
            wraplength=200,
            font=("Arial", 16),
            fg_color="CadetBlue4",
            justify="left",
            corner_radius=5,
        )
        label_instrucciones.pack(pady=10, ipady=10, ipadx=20)

        label_error = CTkLabel(
            frame_right,
            wraplength=200,
            font=("Arial", 16),
            fg_color="red4",
            corner_radius=5,
        )

        # Enviar a Matriz el frame donde genera los entrys
        Matriz.defineRoot(frame_det)

        # Enviar el label donde mostrará errores de ser necesario
        Errors.defineroot_det(label_error)

        # Enviar la ventana y el frame donde estoy
        Solution_determinante.define_root(
            Frame_determinante.root, Frame_determinante.frame_def_determinante
        )
