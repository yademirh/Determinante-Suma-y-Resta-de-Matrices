
from customtkinter import *
from componentes import Frame_determinante
from componentes.Frame_Oper import Frame_Operaciones

app = CTk()
app.title("Parcial 2 - Análisis Numérico")
app.geometry("850x550")
 
app.resizable(0,0)
app.configure(padx=20, pady=10)
# poner icono

#-----------------------------------------------------------------------------

frame_main = CTkFrame(master=app, border_width=3, corner_radius=10, width= 700, height=400)
frame_main.pack(fill="both", expand=1)

btn_determinante = CTkButton(master=frame_main, text="DETERMINANTE DE UNA MATRIZ", command=Frame_determinante.Frame_determinante.show_frame_det)
btn_determinante.place(rely=0.5, relx = 0.3, anchor="center") 
btn_determinante.configure(width=60, height=50)
btn_sumRest = CTkButton(master=frame_main, text="SUMA Y RESTA DE MATRICES", command=Frame_Operaciones.show_frame_op)
btn_sumRest.place(rely=0.5, relx = 0.7, anchor="center")
btn_sumRest.configure(width=60, height=50)

Frame_determinante.Frame_determinante.define_root(app, frame_main)
Frame_determinante.Frame_determinante.create_frame()

Frame_Operaciones.define_root(app, frame_main)
Frame_Operaciones.create_frame()

#-----------------------------------------------------------------------------

app.mainloop()