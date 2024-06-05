#Programa para llevar un registro de los Bolivares que se han pagado en Boom pagos
import tkinter as tk
from PIL import ImageTk, Image
from datetime import date
import os
import sqlite3
from tkinter import messagebox

def main():
    pass
    # Directorio principal
    #///////////////////////
    carpeta_principal = os.path.dirname(__file__)
    # Directorio de imágenes
    carpeta_imagenes = os.path.join(carpeta_principal, "images")


    #AQUI VA LA APP EN SI
    app_Bs = tk.Tk()

    #CENTRAR APP EN LA MITAD DE LA PANTALLA

    #  Actualizamos todo el contenido de la ventana (la ventana pude crecer si se le agrega
    #  mas widgets).Esto actualiza el ancho y alto de la ventana en caso de crecer.

    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = app_Bs.winfo_screenwidth()

    htotal = app_Bs.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 750

    hventana = 600

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)

    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    app_Bs.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    app_Bs.configure(background="#000000")

    app_Bs.title("Pago de Bs - Boom Pagos")

    app_Bs.resizable(0,0)

    app_Bs.iconbitmap(os.path.join(carpeta_imagenes,"Flag_of_Venezuela.ico"))

    #IMAGENES

    boton_image_verificar_Colocar = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "botonRedondeadoAzulVerificar.png")).resize((100,80)))

    boton_image_borrar_Colocar = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "botonRedondeadoAzulBorrar.png")).resize((100,80)))

    #VARIABLES
    fecha_hoy = date.today()

    #FUNCIONES PROGRAMA PRINCIPAL
    def borrarTodoTexto():

        ref_pago_entry.delete(0, tk.END)

        monto_bs_entry.delete(0, tk.END)

        fecha_entry_registro.set("")

        ref_entry_result.set("")

        monto_entry_result.set("")

        estado_entry_SV.set("")

    def verificarElPago():

        referencia_del_pago = ref_pago_entry.get()

        bolivares_depositados = monto_bs_entry.get()

        if len(referencia_del_pago) != 6:
            messagebox.showwarning(message="La referencia de pago debe tener exactamente 6 caracteres.", title="Pago de Bs - Boom Pagos")
            return
    
        if verificar_datos(referencia_del_pago, bolivares_depositados):

            def añadirTextoGUI():

                tupla_datos = verificar_datos(referencia_del_pago, bolivares_depositados)

                for i in tupla_datos:
                    pass

                    fecha_entry_registro.set(i[1])

                    ref_entry_result.set(i[2])

                    monto_entry_result.set(i[3])

                    estado_entry_SV.set("PAGADO")

            añadirTextoGUI()

        elif referencia_del_pago == "" and bolivares_depositados == "":
            
            error_sin_texto()
    
        else:

            referencia_del_pago = ref_pago_entry.get()

            bolivares_depositados = True

            if referencia_del_pago == "" and bolivares_depositados == True:

                error_sin_texto_2()

        
            else:    

                bolivares_depositados = monto_bs_entry.get()  

                referencia_del_pago = True

                if referencia_del_pago == True  and bolivares_depositados == "" :

                    error_sin_texto_2()

                else:
                
                    referencia_del_pago = ref_pago_entry.get()
                    bolivares_depositados = monto_bs_entry.get()

                    if ventana_si_no():         
                        agregar_datos(fecha_hoy,referencia_del_pago, bolivares_depositados)
                        borrarTodoTexto()
                        ref_pago_entry.focus()
                        
                    else:
                        borrarTodoTexto()

    #BOTONES PROGRAMA PRINCIPAL
    verificar_pago = tk.Button(app_Bs, text="Verificar", font=("Arial", 15), bg="#000000", fg="#FFFFFF", command= verificarElPago, image= boton_image_verificar_Colocar, borderwidth=0, background="#000000")
    verificar_pago.place(x=350, y=330)

    borrar_todo = tk.Button(app_Bs, text="Borrar", font=("Arial", 15), bg="#000000", fg="#FFFFFF", command= borrarTodoTexto, image= boton_image_borrar_Colocar, borderwidth=0, background="#000000")
    borrar_todo.place(x=230, y=330)

    #CUADROS DE TEXTO PROGRAMA PRINCIPAL
    ref_entry_text = tk.StringVar()

    monto_entry_text = tk.StringVar()

    fecha_entry_registro = tk.StringVar()

    ref_entry_result = tk.StringVar()

    monto_entry_result = tk.StringVar()

    estado_entry_SV = tk.StringVar()

    ref_pago_entry = tk.Entry(app_Bs, fg="Black", justify="center", font=("Arial", 16), textvariable= ref_entry_text, bg="#FFFFFF")

    ref_pago_entry.focus()

    ref_pago_entry.place(x=280, y=255)

    monto_bs_entry = tk.Entry(app_Bs, fg="Black", justify="center", font=("Arial", 16), textvariable= monto_entry_text, bg="#FFFFFF")

    monto_bs_entry.place(x=280, y=305)

    fecha_registro_pago = tk.Entry(app_Bs, justify="center", font=("Arial", 16), state= "readonly", textvariable= fecha_entry_registro)

    fecha_registro_pago.place(x=25 , y=540, width= 160, height=50)

    referencia_cuadro_resultado = tk.Entry(app_Bs, justify="center", font=("Arial", 16), state="readonly", textvariable= ref_entry_result)

    referencia_cuadro_resultado.place(x=250 , y=540, width= 120, height=50)

    monto_cuadro_resultado = tk.Entry(app_Bs, justify="center", font=("Arial", 16), state="readonly", textvariable= monto_entry_result)

    monto_cuadro_resultado.place(x=430 , y=540, width= 130, height=50)

    estado_cuadro_resultado = tk.Entry(app_Bs, justify="center", font=("Arial", 16), state="readonly", textvariable= estado_entry_SV)

    estado_cuadro_resultado.place(x=620 , y=540, width= 110, height=50)

    #ETIQUETAS PROGRAMA PRINCIPAL

    titulo_principal = tk.Label(app_Bs, text="PAGO DE BOLIVARES"  ,bg="#000000", fg="#FFFFFF",font=("Arial",25))
    titulo_principal.place(x=200 , y=170)

    ref_pago_texto = tk.Label(app_Bs, text="Referencia de pago: "  ,bg="#000000", fg="#FFFFFF",font=("Arial",19))
    ref_pago_texto.place(x=25 , y=250)

    monto_bs_texto = tk.Label(app_Bs, text="Monto en Bolivares: "  ,bg="#000000", fg="#FFFFFF",font=("Arial",19))
    monto_bs_texto.place(x=25 , y=300)

    fecha_registro = tk.Label(app_Bs, text="Fecha de registro",bg="#000000", fg="#FFFFFF",font=("Arial",15))
    fecha_registro.place(x=25 , y=500)

    refe_result_text = tk.Label(app_Bs, text="Referencia #",bg="#000000", fg="#FFFFFF",font=("Arial",15))
    refe_result_text.place(x=250 , y=500)

    monto_depositados_client = tk.Label(app_Bs, text="Monto",bg="#000000", fg="#FFFFFF",font=("Arial",19))
    monto_depositados_client.place(x=455 , y=498)

    fecha_actual = tk.Label(app_Bs,text= fecha_hoy ,bg="#000000", fg="#FFFFFF",font=("Arial",18))
    fecha_actual.place(x=102 , y=10)

    fecha_label = tk.Label(app_Bs,text= "Fecha: " ,bg="#000000", fg="#FFFFFF",font=("Arial",18))
    fecha_label.place(x=15 , y=10)

    estado_transferencia = tk.Label(app_Bs, text= "Estado" , bg="#000000", fg="#FFFFFF",font=("Arial",18))
    estado_transferencia.place(x=635 , y=498)

    #FUNCIONES PROGRAMA PRINCIPAL
    def limitador(ref_entry_text):
        if len(ref_entry_text.get()) > 0:
            #donde esta el :5 limitas la cantidad d caracteres
            ref_entry_text.set(ref_entry_text.get()[:6])

    def limitador2(monto_entry_text):
        if len(monto_entry_text.get()) > 0:
            #donde esta el :5 limitas la cantidad d caracteres
            monto_entry_text.set(monto_entry_text.get()[:20])

    ref_entry_text.trace("w", lambda *args: limitador(ref_entry_text))
    monto_entry_text.trace("w", lambda *args: limitador2(monto_entry_text))

    def formato_monto(*args):
        # Obtener el texto actual del Entry
        monto = monto_bs_entry.get()
    
        # Eliminar cualquier punto existente en el texto
        monto = monto.replace(".", "")
    
        # Dividir el texto en grupos de tres caracteres desde el final
        grupos = [monto[max(i-3, 0):i] for i in range(len(monto), 0, -3)]
    
        # Unir los grupos con puntos entre ellos
        monto_formateado = ".".join(grupos[::-1])
    
        # Actualizar el texto en el Entry con el nuevo formato
        monto_bs_entry.delete(0, tk.END)
        monto_bs_entry.insert(0, monto_formateado)

    # Llamar a la función formato_monto cada vez que el texto en el Entry cambie
    monto_entry_text.trace("w", formato_monto)


    app_Bs.mainloop()


#Base de datos
def agregar_datos(fecha_hoy,referencia_del_pago, bolivares_depositados):
    pass
    carpeta_principal = os.path.dirname(__file__)
    ruta_basededatos = os.path.join(carpeta_principal, "..", "data", "database_app_bs.db")
    
    conn = sqlite3.connect(ruta_basededatos, isolation_level= None)
    cursor = conn.cursor()

    query = f"INSERT INTO pagos(id, fecha_registro, referencia_pago, bolivares_deposit) VALUES (NULL,?, ?, ?)"

    rows = cursor.execute(query, (fecha_hoy,referencia_del_pago, bolivares_depositados))

    cursor.close()
    conn.close()

def verificar_datos(referencia_del_pago, bolivares_depositados):
    pass
    carpeta_principal = os.path.dirname(__file__)
    ruta_basededatos = os.path.join(carpeta_principal, "..", "data", "database_app_bs.db")
    
    conn = sqlite3.connect(ruta_basededatos)

    cursor = conn.cursor()

    rows = cursor.execute(f"SELECT * FROM pagos WHERE referencia_pago= '{referencia_del_pago}' AND bolivares_deposit= '{bolivares_depositados}'")

    datos = rows.fetchall()

    cursor.close()
    conn.close()
    if datos == []:
        return False
    return datos
    
def error_sin_texto():
    messagebox.showwarning(message="Debes ingresar texto en las cajas!", title="Pago de Bs - Boom Pagos")
    
def error_sin_texto_2():
    messagebox.showwarning(message="Debe escribir en las dos cajas de texto, no solo en una!", title="Pago de Bs - Boom Pagos")
    
def ventana_si_no():
    return messagebox.askquestion(message="¿Deseas registrar esta operación?", title="Pago de Bs - Boom Pagos")

#empezar

if __name__ == '__main__':
    main()