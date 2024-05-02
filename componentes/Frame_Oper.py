from customtkinter import * 
from .Matriz import *
from validaciones.Errors import Errors
from .Frame_Sol_operaciones import Solution_Operaciones

class Frame_Operaciones:

    root : CTk
    main : CTkFrame
    frame_oper : CTkFrame
    col : int = 0
    row : int = 0

    options_size_row : CTkEntry
    options_size_column : CTkEntry

    @staticmethod
    def define_root(app, frame_main):
        Frame_Operaciones.root = app
        Frame_Operaciones.main = frame_main

    @staticmethod
    def show_frame_op():
        Frame_Operaciones.frame_oper.pack(fill="both", expand=1)
        Frame_Operaciones.main.pack_forget()

    @staticmethod
    def to_back():
        Frame_Operaciones.main.pack(fill="both", expand=1)
        Frame_Operaciones.frame_oper.pack_forget()
        Errors.hide_label()

    @staticmethod
    def send_col_row():
        try:
            column=int(Frame_Operaciones.options_size_column.get())
            row = int(Frame_Operaciones.options_size_row.get())
            if column>0 and row>0 :
                Matriz.createMatriz_oper(row, column)
                Errors.hide_label()

        except ZeroDivisionError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy()            
            Errors.msg_error = "División por cero"
            Errors.show_label()
        except IndexError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Campo(s) nulo"
            Errors.show_label()
        except KeyError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Campo(s) nulo"
            Errors.show_label()
        except AttributeError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Campo(s) nulo"
            Errors.show_label()
        except ArithmeticError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Operación no válida o posible división por cero"
            Errors.show_label()
        except ValueError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Campo(s) nulo"
            Errors.show_label()
        except TypeError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Operación no válida"
            Errors.show_label()
        except SyntaxError:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = "Operación no válida"
            Errors.show_label()
        except Exception as e:
            Matriz.frame1.destroy()
            Matriz.frame2.destroy() 
            Errors.msg_error = e
            Errors.show_label()

    @staticmethod
    def create_frame():
        Frame_Operaciones.frame_oper = CTkFrame(Frame_Operaciones.root, border_width=3, fg_color="dark slate gray", corner_radius=10)


        frame_left = CTkScrollableFrame(Frame_Operaciones.frame_oper)
        # frame_left.pack(fill="both", expand=1, side="left")
        frame_left.grid(row=0, column=0, sticky="nsew")
        frame_right = CTkFrame(Frame_Operaciones.frame_oper)
        # frame_right.pack(fill="both", expand=1, side="left")
        frame_right.grid(row=0, column=1, sticky="nsew")

        bt = CTkButton(Frame_Operaciones.frame_oper, text="Back", width=40, command=Frame_Operaciones.to_back)
        bt.place(x=10, y=10)

        Frame_Operaciones.frame_oper.columnconfigure(0,weight=3)
        Frame_Operaciones.frame_oper.columnconfigure(1,weight=1)
        Frame_Operaciones.frame_oper.rowconfigure(0,weight=1)

        container = CTkFrame(frame_left)

        label_defineSize = CTkLabel(container, text="Define el tamaño de la matriz: ", corner_radius=5, fg_color="LightCyan3", text_color="black",font=("Arial", 16))
        label_defineSize.grid(row=0, column=0, columnspan=2)


        Frame_Operaciones.options_size_row = CTkEntry(container, placeholder_text="Filas", width=80, font=("Arial", 16), justify="center") 
        Frame_Operaciones.options_size_row.grid(row=1, column=0, pady=20, ipady=5, ipadx=5)
        
        Frame_Operaciones.options_size_column = CTkEntry(container, placeholder_text="Columnas", width=80, font=("Arial", 16), justify="center") 
        Frame_Operaciones.options_size_column.grid(row=1, column=1, pady=20, padx=20, ipady=5, ipadx=5) 

        btn_generate = CTkButton(container, text="Generar", command=Frame_Operaciones.send_col_row, width=80)
        btn_generate.grid(row=2, column=0)

        container.pack(pady=50)

        div_operaciones = CTkFrame(frame_left, fg_color="azure")
        div_operaciones.pack()

        div_btns = CTkFrame(frame_left)
        btn_calculate_sum = CTkButton(div_btns, text="CALCULAR SUMA", command=Solution_Operaciones.show_frame_sol_oper_sum, font=("Arial", 16))
        btn_calculate_sum.grid(row=0, column=0)
        btn_calculate_rest = CTkButton(div_btns, text="CALCULAR RESTA", command=Solution_Operaciones.show_frame_sol_oper_rest, font=("Arial", 16))
        btn_calculate_rest.grid(row=0, column=1, padx=40)
        div_btns.pack(pady=30)



        label_error = CTkLabel(frame_right, wraplength=200, font=('Arial', 16), fg_color="red4", justify="left", corner_radius=5)

        Matriz.defineRoot_oper(div_operaciones)
        Errors.defineroot(label_error)
        Solution_Operaciones.define_root(Frame_Operaciones.root, Frame_Operaciones.frame_oper)
