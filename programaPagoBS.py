#Programa para llevar un registro de los Bolivares que se han pagado en Boom pagos
from tkinter import *
from PIL import ImageTk, Image
from datetime import *
import os
import sqlite3

def main():
    pass
    # Directorio principal
    #///////////////////////
    carpeta_principal = os.path.dirname(__file__)
    # Directorio de imágenes
    carpeta_imagenes = os.path.join(carpeta_principal, "images")


    #AQUI VA LA APP EN SI
    app_Bs = Tk()

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

    app_Bs.configure(background="#0068FF")

    app_Bs.title("Pago de Bs - Boom Pagos")

    app_Bs.resizable(0,0)

    app_Bs.iconbitmap(os.path.join(carpeta_imagenes,"Flag_of_Venezuela.ico"))

    #IMAGENES
    img = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "Boompagosfoto1.png")).resize((250,100)))

    boton_image_verificar_Colocar = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "botonRedondeadoAzulVerificar.png")).resize((100,80)))

    boton_image_borrar_Colocar = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "botonRedondeadoAzulBorrar.png")).resize((100,80)))

    #VARIABLES
    fecha_hoy = date.today()

    #Esos nombres de variables hace referencia a DataBase o Base de datos. Son listas
    db_ref = ["0"]

    db_bs_depositados = ["0"]

    db_fecha_registro = ["0"]


    #FUNCIONES PROGRAMA PRINCIPAL
    def borrarTodoTexto():

        ref_pago_entry.delete(0, END)

        monto_bs_entry.delete(0, END)

        fecha_entry_registro.set("")

        ref_entry_result.set("")

        monto_entry_result.set("")

        estado_entry_SV.set("")

    def verificarElPago():

        referencia_del_pago = ref_pago_entry.get()

        bolivares_depositados = monto_bs_entry.get()
    
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

            def ventana_error():

                ventana_Erro = Toplevel(app_Bs)

                ventana_Erro.title("Error")

                ventana_Erro.geometry("300x200+700+400")

                ventana_Erro.iconbitmap(os.path.join(carpeta_imagenes,"Flag_of_Venezuela.ico"))

                ventana_Erro.resizable(0,0)

                #FUNCIONES

                #LABEL

                msj_error = Label(ventana_Erro, text= "Debe escribir la información en las cajas de texto!!!", bg="Black", fg="White")
                msj_error.place(x=15, y=60)

                #BOTONES

                continuar_Boton = Button(ventana_Erro, text="CONTINUAR", command= ventana_Erro.destroy)
                continuar_Boton.place(x=110, y=125)

            ventana_error()
    
        else:

            referencia_del_pago = ref_pago_entry.get()

            bolivares_depositados = True

            if referencia_del_pago == "" and bolivares_depositados == True:

                def ventanaError2():
                    nuevaVenta2 = Toplevel(app_Bs)

                    nuevaVenta2.title("Error!")

                    nuevaVenta2.geometry("320x190+700+400")

                    nuevaVenta2.iconbitmap(os.path.join(carpeta_imagenes,"Flag_of_Venezuela.ico"))

                    nuevaVenta2.resizable(0,0)

                    #FUNCIONES

                    #LABEL

                    msj_error2 = Label(nuevaVenta2, text= "¡Debe escribir en las dos cajas de texto, no solo en una!", bg="Black", fg="White")
                    msj_error2.place(x=15, y=60)

                    #BOTONES

                    continuar_Boton2 = Button(nuevaVenta2, text="CONTINUAR", command= nuevaVenta2.destroy)
                    continuar_Boton2.place(x=110, y=125)

                ventanaError2()

        
            else:    

                bolivares_depositados = monto_bs_entry.get()  

                referencia_del_pago = True

                if referencia_del_pago == True  and bolivares_depositados == "" :

                    def ventanaError2():
                        nuevaVenta2 = Toplevel(app_Bs)

                        nuevaVenta2.title("Error!")

                        nuevaVenta2.geometry("320x190+700+400")

                        nuevaVenta2.iconbitmap(os.path.join(carpeta_imagenes,"Flag_of_Venezuela.ico"))

                        nuevaVenta2.resizable(0,0)

                        #FUNCIONES

                        #LABEL

                        msj_error2 = Label(nuevaVenta2, text= "¡Debe escribir en las dos cajas de texto, no solo en una!", bg="Black", fg="White")
                        msj_error2.place(x=15, y=60)

                        #BOTONES

                        continuar_Boton2 = Button(nuevaVenta2, text="CONTINUAR", command= nuevaVenta2.destroy)
                        continuar_Boton2.place(x=110, y=125)

                    ventanaError2()

                else:

                    referencia_del_pago = ref_pago_entry.get()

                    bolivares_depositados = monto_bs_entry.get()

                    def nuevaVentana():
                        nuevaVenta = Toplevel(app_Bs)

                        nuevaVenta.title("Confirmación!")

                        nuevaVenta.geometry("320x190+700+400")

                        nuevaVenta.iconbitmap(os.path.join(carpeta_imagenes,"Flag_of_Venezuela.ico"))

                        nuevaVenta.resizable(0,0)

                        #FUNCIONES

                        def accion_del_si():

                            agregar_datos(fecha_hoy,referencia_del_pago, bolivares_depositados)

                            msj_exitoso = Label(nuevaVenta, text="""
La referencia y el monto en Soberanos
se acaban de registar correctamente!!!""", bg="Black", fg="White")
                            msj_exitoso.place(x=60, y=120)

                            def OcultarVentana():
                                nuevaVenta.withdraw()

                                nuevaVenta.after(500)

                                nuevaVenta.destroy()

                                borrarTodoTexto()

                            nuevaVenta.after(5000, OcultarVentana)

                        def accion_del_no():

                            nuevaVenta.destroy()
                            borrarTodoTexto()

                        #LABEL

                        msj_confirma = Label(nuevaVenta, text= "¿Deseas registrar esta operación?", bg="Black", fg="White")
                        msj_confirma.place(x=70, y=40)

                        msj_no_pagado = Label(nuevaVenta, text= "¡Este pago no se ha pagado!", bg="Black", fg="White")
                        msj_no_pagado.place(x=75, y=0)

                        #Botones

                        boton_si = Button(nuevaVenta, text=" SI ", command= accion_del_si)
                        boton_si.place(x=100, y=80)

                        boton_no = Button(nuevaVenta, text=" NO ", command= accion_del_no)
                        boton_no.place(x=160, y=80)

                    nuevaVentana()

    #BOTONES PROGRAMA PRINCIPAL
    verificar_pago = Button(app_Bs, text="Verificar", font=("Arial", 15), bg="White", fg="Black", command= verificarElPago, image= boton_image_verificar_Colocar, borderwidth=0, background="#0068FF")
    verificar_pago.place(x=350, y=330)

    borrar_todo = Button(app_Bs, text="Borrar", font=("Arial", 15), bg="White", fg="Black", command= borrarTodoTexto, image= boton_image_borrar_Colocar, borderwidth=0, background="#0068FF")
    borrar_todo.place(x=230, y=330)




    #CUADROS DE TEXTO PROGRAMA PRINCIPAL
    ref_entry_text = StringVar()

    monto_entry_text = StringVar()

    fecha_entry_registro = StringVar()

    ref_entry_result = StringVar()

    monto_entry_result = StringVar()

    estado_entry_SV = StringVar()

    ref_pago_entry = Entry(app_Bs, fg="Black", justify="center", font=("Arial", 16), textvariable= ref_entry_text, bg="#00B9E2")

    ref_pago_entry.place(x=280, y=255)

    monto_bs_entry = Entry(app_Bs, fg="Black", justify="center", font=("Arial", 16), textvariable= monto_entry_text, bg="#00B9E2")

    monto_bs_entry.place(x=280, y=305)

    fecha_registro_pago = Entry(app_Bs, justify="center", font=("Arial", 16), state= "readonly", textvariable= fecha_entry_registro)

    fecha_registro_pago.place(x=25 , y=540, width= 160, height=50)

    referencia_cuadro_resultado = Entry(app_Bs, justify="center", font=("Arial", 16), state="readonly", textvariable= ref_entry_result)

    referencia_cuadro_resultado.place(x=250 , y=540, width= 120, height=50)

    monto_cuadro_resultado = Entry(app_Bs, justify="center", font=("Arial", 16), state="readonly", textvariable= monto_entry_result)

    monto_cuadro_resultado.place(x=430 , y=540, width= 130, height=50)

    estado_cuadro_resultado = Entry(app_Bs, justify="center", font=("Arial", 16), state="readonly", textvariable= estado_entry_SV)

    estado_cuadro_resultado.place(x=620 , y=540, width= 110, height=50)


    #ETIQUETAS PROGRAMA PRINCIPAL

    titulo_principal = Label(app_Bs, text="PAGO DE BOLIVARES"  ,bg="#00CB97", fg="Black",font=("Arial",25))
    titulo_principal.place(x=200 , y=170)

    nombre_del_local = Label(app_Bs, text="BOOM PAGOS"  ,bg="#00CB97", fg="Black",font=("Arial",15))
    nombre_del_local.place(x=400 , y=18)

    ref_pago_texto = Label(app_Bs, text="Referencia de pago: "  ,bg="#00CB97", fg="Black",font=("Arial",19))
    ref_pago_texto.place(x=25 , y=250)

    monto_bs_texto = Label(app_Bs, text="Monto en Bolivares: "  ,bg="#00CB97", fg="Black",font=("Arial",19))
    monto_bs_texto.place(x=25 , y=300)

    label_img = Label(app_Bs, image= img, bg="#0068FF")
    label_img.place(x=550 , y= -5)

    fecha_registro = Label(app_Bs, text="Fecha de registro",bg="#00CB97", fg="Black",font=("Arial",15))
    fecha_registro.place(x=25 , y=500)

    refe_result_text = Label(app_Bs, text="Referencia #",bg="#00CB97", fg="Black",font=("Arial",15))
    refe_result_text.place(x=250 , y=500)

    monto_depositados_client = Label(app_Bs, text="Monto",bg="#00CB97", fg="Black",font=("Arial",19))
    monto_depositados_client.place(x=455 , y=498)

    texto_bs = Label(app_Bs, text="BS",bg="#00CB97", fg="Black",font=("Arial",18))
    texto_bs.place(x=530 , y=303)

    fecha_actual = Label(app_Bs,text= fecha_hoy ,bg="#00CB97", fg="Black",font=("Arial",18))
    fecha_actual.place(x=102 , y=10)

    fecha_label = Label(app_Bs,text= "Fecha: " ,bg="#00CB97", fg="Black",font=("Arial",18))
    fecha_label.place(x=15 , y=10)

    estado_transferencia = Label(app_Bs, text= "Estado" , bg="#00CB97", fg="Black",font=("Arial",18))
    estado_transferencia.place(x=635 , y=498)

    #FUNCIONES PROGRAMA PRINCIPAL
    def limitador(ref_entry_text):
        if len(ref_entry_text.get()) > 0:
            #donde esta el :5 limitas la cantidad d caracteres
            ref_entry_text.set(ref_entry_text.get()[:4])

    def limitador2(monto_entry_text):
        if len(monto_entry_text.get()) > 0:
            #donde esta el :5 limitas la cantidad d caracteres
            monto_entry_text.set(monto_entry_text.get()[:20])

    ref_entry_text.trace("w", lambda *args: limitador(ref_entry_text))
    monto_entry_text.trace("w", lambda *args: limitador2(monto_entry_text))

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

#empezar

if __name__ == '__main__':
    main()