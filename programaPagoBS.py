import tkinter as tk
from PIL import ImageTk, Image
from datetime import date
import os
import sqlite3
from tkinter import messagebox
import json  # Importamos la librería json para manejar el archivo de configuración

# Ruta del archivo de configuración
CONFIG_FILE = "config.json"

# Función para cargar la configuración
def cargar_configuracion():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"PIN_ACTIVADO": True}  # Valor por defecto si el archivo no existe

# Función para guardar la configuración
def guardar_configuracion(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

# Cargar la configuración al inicio
config = cargar_configuracion()
PIN_ACTIVADO = config["PIN_ACTIVADO"]
PIN = "242526"  # PIN por defecto

def solicitar_pin():
    def verificar_pin():
        if entrada_pin.get() == PIN:
            ventana_pin.destroy()
            main()
        else:
            messagebox.showerror("Error", "PIN incorrecto")
            entrada_pin.delete(0, tk.END)

    if not PIN_ACTIVADO:
        main()
        return

    ventana_pin = tk.Tk()
    ventana_pin.title("Ingrese el PIN")
    ventana_pin.configure(background="#000000")

    # Centrar la ventana en la pantalla
    wtotal = ventana_pin.winfo_screenwidth()
    htotal = ventana_pin.winfo_screenheight()
    wventana = 300
    hventana = 150
    pwidth = round(wtotal/2 - wventana/2)
    pheight = round(htotal/2 - hventana/2)
    ventana_pin.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")
    ventana_pin.resizable(0, 0)

    label_pin = tk.Label(ventana_pin, text="Ingrese el PIN:", bg="#000000", fg="#FFFFFF", font=("Arial", 14))
    label_pin.pack(pady=10)

    entrada_pin = tk.Entry(ventana_pin, show="*", font=("Arial", 14))
    entrada_pin.pack(pady=10)

    boton_verificar = tk.Button(ventana_pin, text="Verificar", font=("Arial", 14), command=verificar_pin)
    boton_verificar.pack(pady=10)

    ventana_pin.mainloop()

def main():
    global PIN_ACTIVADO

    # Directorio principal
    carpeta_principal = os.path.dirname(__file__)
    # Directorio de imágenes
    carpeta_imagenes = os.path.join(carpeta_principal, "images")

    # Crear la ventana principal
    app_Bs = tk.Tk()

    # Centrar la ventana en la pantalla
    wtotal = app_Bs.winfo_screenwidth()
    htotal = app_Bs.winfo_screenheight()
    wventana = 750
    hventana = 600
    pwidth = round(wtotal/2 - wventana/2)
    pheight = round(htotal/2 - hventana/2)
    app_Bs.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

    app_Bs.configure(background="#000000")
    app_Bs.title("Pago de Bs - Boom Pagos")
    app_Bs.resizable(0, 0)
    app_Bs.iconbitmap(os.path.join(carpeta_imagenes, "Flag_of_Venezuela.ico"))

    # Función para alternar el estado del PIN
    def toggle_pin():
        global PIN_ACTIVADO
        PIN_ACTIVADO = not PIN_ACTIVADO
        estado = "Activado" if PIN_ACTIVADO else "Desactivado"
        messagebox.showinfo("Estado del PIN", f"PIN {estado}")
        # Guardar el estado en el archivo de configuración
        config["PIN_ACTIVADO"] = PIN_ACTIVADO
        guardar_configuracion(config)

    # Botón oculto para alternar el estado del PIN
    def mostrar_boton_oculto(event=None):
        boton_toggle_pin.place(x=10, y=10)

    # Botón para alternar el estado del PIN
    boton_toggle_pin = tk.Button(app_Bs, text="Toggle PIN", font=("Arial", 12), command=toggle_pin, bg="#ffffff", fg="#000000")
    boton_toggle_pin.place_forget()  # Ocultar el botón inicialmente

    # Vincular la combinación de teclas (Ctrl + Alt + P) para mostrar el botón oculto
    app_Bs.bind("<Control-Alt-p>", mostrar_boton_oculto)

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
        ref_pago_entry.focus()

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
                    if ventana_si_no() == "yes":         
                        agregar_datos(fecha_hoy,referencia_del_pago, bolivares_depositados)
                        borrarTodoTexto()
                        ref_pago_entry.focus()
                    else:
                        borrarTodoTexto()
                        ref_pago_entry.focus()

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
            ref_entry_text.set(ref_entry_text.get()[:6])

    def limitador2(monto_entry_text):
        if len(monto_entry_text.get()) > 0:
            monto_entry_text.set(monto_entry_text.get()[:20])

    ref_entry_text.trace("w", lambda *args: limitador(ref_entry_text))
    monto_entry_text.trace("w", lambda *args: limitador2(monto_entry_text))

    def formato_monto(*args):
        monto = monto_bs_entry.get()
        monto = monto.replace(".", "")
        grupos = [monto[max(i-3, 0):i] for i in range(len(monto), 0, -3)]
        monto_formateado = ".".join(grupos[::-1])
        monto_bs_entry.delete(0, tk.END)
        monto_bs_entry.insert(0, monto_formateado)

    monto_entry_text.trace("w", formato_monto)

    app_Bs.mainloop()

#Base de datos
def agregar_datos(fecha_hoy,referencia_del_pago, bolivares_depositados):
    carpeta_principal = os.path.dirname(__file__)
    ruta_basededatos = os.path.join(carpeta_principal, "..", "data", "database_app_bs.db")
    
    conn = sqlite3.connect(ruta_basededatos, isolation_level= None)
    cursor = conn.cursor()

    query = f"INSERT INTO pagos(id, fecha_registro, referencia_pago, bolivares_deposit) VALUES (NULL,?, ?, ?)"

    rows = cursor.execute(query, (fecha_hoy,referencia_del_pago, bolivares_depositados))

    cursor.close()
    conn.close()

def verificar_datos(referencia_del_pago, bolivares_depositados):
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
    solicitar_pin()