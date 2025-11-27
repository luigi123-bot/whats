import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import pywhatkit as kit
import pyautogui
import time
import threading

class WhatsAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enviar Mensajes WhatsApp")
        self.root.geometry("700x800")
        self.root.resizable(True, True)
        
        # Variable para controlar el envío
        self.enviando = False
        
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Pestaña 1: Configuración
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="📱 Números")
        self.setup_tab1()
        
        # Pestaña 2: Mensaje
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="💬 Mensaje")
        self.setup_tab2()
        
        # Pestaña 3: Configuración avanzada
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="⚙️ Opciones")
        self.setup_tab3()
        
        # Pestaña 4: Registro
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="📋 Registro")
        self.setup_tab4()
    
    def setup_tab1(self):
        """Pestaña para ingresar números de teléfono"""
        frame_title = ttk.Label(self.tab1, text="Números de Teléfono", font=("Arial", 12, "bold"))
        frame_title.pack(pady=10)
        
        frame_info = ttk.Label(self.tab1, text="Ingresa los números separados por saltos de línea (sin +)", 
                               font=("Arial", 9), foreground="gray")
        frame_info.pack(pady=5)
        
        # Text widget para números
        self.text_numbers = scrolledtext.ScrolledText(self.tab1, height=15, width=50, wrap=tk.WORD)
        self.text_numbers.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Botones
        frame_buttons = ttk.Frame(self.tab1)
        frame_buttons.pack(padx=10, pady=10, fill="x")
        
        btn_load = ttk.Button(frame_buttons, text="📂 Cargar desde archivo", command=self.load_numbers)
        btn_load.pack(side="left", padx=5)
        
        btn_clear = ttk.Button(frame_buttons, text="🗑️ Limpiar", command=lambda: self.text_numbers.delete("1.0", tk.END))
        btn_clear.pack(side="left", padx=5)
        
        # Agregar número de ejemplo
        example_text = "573012906861\n573001234567\n573009876543"
        self.text_numbers.insert("1.0", example_text)
    
    def setup_tab2(self):
        """Pestaña para el mensaje"""
        frame_title = ttk.Label(self.tab2, text="Mensaje a Enviar", font=("Arial", 12, "bold"))
        frame_title.pack(pady=10)
        
        # Text widget para el mensaje
        self.text_message = scrolledtext.ScrolledText(self.tab2, height=20, width=50, wrap=tk.WORD)
        self.text_message.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Mensaje por defecto
        default_message = """Hola queridos estudiantes interesados en el curso de inyectología.

Recuerden que se llevará a cabo el 8 y 15 de Nov. De 1pm a 5pm.

Por un valor de $100.000, que deben estar pagos para separar tu cupo el 4 de Noviembre.

Cupos limitados, no te quedes sin el tuyo.

Realiza tu pago al número de cuenta habitual y envía el comprobante aquí con tu nombre completo.

Comunícate: 302 5270747"""
        
        self.text_message.insert("1.0", default_message)
        
        # Botón para limpiar
        btn_clear = ttk.Button(self.tab2, text="🗑️ Limpiar mensaje", 
                               command=lambda: self.text_message.delete("1.0", tk.END))
        btn_clear.pack(padx=10, pady=5)
    
    def setup_tab3(self):
        """Pestaña para configuración avanzada"""
        frame_title = ttk.Label(self.tab3, text="Configuración Avanzada", font=("Arial", 12, "bold"))
        frame_title.pack(pady=10)
        
        # Tiempo de espera
        frame_wait = ttk.Frame(self.tab3)
        frame_wait.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(frame_wait, text="Tiempo de espera entre mensajes (segundos):", width=35).pack(side="left")
        self.var_wait_time = tk.IntVar(value=15)
        ttk.Spinbox(frame_wait, from_=5, to=60, textvariable=self.var_wait_time, width=10).pack(side="left", padx=5)
        
        # Tiempo de espera antes de enviar
        frame_tab_wait = ttk.Frame(self.tab3)
        frame_tab_wait.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(frame_tab_wait, text="Tiempo para cargar WhatsApp Web (segundos):", width=35).pack(side="left")
        self.var_tab_wait = tk.IntVar(value=20)
        ttk.Spinbox(frame_tab_wait, from_=5, to=60, textvariable=self.var_tab_wait, width=10).pack(side="left", padx=5)
        
        # Cerrar pestaña automáticamente
        frame_close = ttk.Frame(self.tab3)
        frame_close.pack(pady=10, padx=10, fill="x")
        
        self.var_tab_close = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame_close, text="Cerrar pestaña automáticamente después de enviar", 
                       variable=self.var_tab_close).pack(anchor="w")
        
        # Frame para botones de acción
        frame_action = ttk.LabelFrame(self.tab3, text="Acciones", padding=10)
        frame_action.pack(pady=20, padx=10, fill="both", expand=True)
        
        btn_send = ttk.Button(frame_action, text="▶️ Iniciar Envío", command=self.start_sending)
        btn_send.pack(pady=5, fill="x")
        
        self.btn_stop = ttk.Button(frame_action, text="⏹️ Detener", command=self.stop_sending, state="disabled")
        self.btn_stop.pack(pady=5, fill="x")
        
        # Label de estado
        self.label_status = ttk.Label(frame_action, text="Estado: Listo", font=("Arial", 10))
        self.label_status.pack(pady=10)
    
    def setup_tab4(self):
        """Pestaña para el registro de envíos"""
        frame_title = ttk.Label(self.tab4, text="Registro de Envíos", font=("Arial", 12, "bold"))
        frame_title.pack(pady=10)
        
        # Text widget para el log
        self.text_log = scrolledtext.ScrolledText(self.tab4, height=20, width=50, wrap=tk.WORD)
        self.text_log.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Configurar colores
        self.text_log.tag_config("info", foreground="black")
        self.text_log.tag_config("success", foreground="green")
        self.text_log.tag_config("error", foreground="red")
        self.text_log.tag_config("warning", foreground="orange")
        
        # Botón para limpiar log
        btn_clear_log = ttk.Button(self.tab4, text="🗑️ Limpiar log", 
                                   command=lambda: self.text_log.delete("1.0", tk.END))
        btn_clear_log.pack(padx=10, pady=5)
    
    def load_numbers(self):
        """Cargar números desde un archivo"""
        file_path = filedialog.askopenfilename(
            title="Selecciona archivo de números",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    numbers = f.read()
                self.text_numbers.delete("1.0", tk.END)
                self.text_numbers.insert("1.0", numbers)
                self.log_message(f"✅ Se cargaron números desde: {file_path}", "success")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
                self.log_message(f"❌ Error al cargar archivo: {e}", "error")
    
    def log_message(self, message, tag="info"):
        """Agregar mensaje al log"""
        self.text_log.insert(tk.END, message + "\n", tag)
        self.text_log.see(tk.END)
        self.text_log.update()
    
    def start_sending(self):
        """Iniciar el envío de mensajes en un hilo separado"""
        # Obtener números y mensaje
        numbers_text = self.text_numbers.get("1.0", tk.END).strip()
        message = self.text_message.get("1.0", tk.END).strip()
        
        if not numbers_text:
            messagebox.showwarning("Advertencia", "Por favor ingresa al menos un número de teléfono.")
            return
        
        if not message:
            messagebox.showwarning("Advertencia", "Por favor ingresa un mensaje.")
            return
        
        # Confirmar inicio
        numbers = [n.strip() for n in numbers_text.split('\n') if n.strip()]
        respuesta = messagebox.askyesno("Confirmación", 
                                       f"¿Enviar mensaje a {len(numbers)} número(s)?\n\n"
                                       "Asegúrate de tener WhatsApp Web abierto.")
        
        if respuesta:
            # Deshabilitar botones
            self.btn_stop.config(state="normal")
            self.notebook.tab(1, state="disabled")
            self.notebook.tab(2, state="disabled")
            self.notebook.tab(3, state="disabled")
            
            # Crear y ejecutar hilo
            self.enviando = True
            thread = threading.Thread(target=self.send_messages, args=(numbers, message))
            thread.daemon = True
            thread.start()
    
    def stop_sending(self):
        """Detener el envío de mensajes"""
        self.enviando = False
        self.log_message("⏸️ Envío detenido por el usuario.", "warning")
        self.update_status("Detenido")
    
    def send_messages(self, numbers, message):
        """Enviar mensajes"""
        try:
            self.update_status("Preparando envío...")
            self.log_message(f"📤 Iniciando envío de {len(numbers)} mensaje(s)...", "info")
            time.sleep(3)
            
            for i, numero in enumerate(numbers, 1):
                if not self.enviando:
                    break
                
                phone = f"+{numero.strip()}"
                self.update_status(f"Enviando {i}/{len(numbers)}...")
                self.log_message(f"\n[{i}/{len(numbers)}] Enviando mensaje a {phone}...", "info")
                
                try:
                    # Enviar mensaje
                    kit.sendwhatmsg_instantly(
                        phone, 
                        message, 
                        wait_time=self.var_tab_wait.get(), 
                        tab_close=self.var_tab_close.get()
                    )
                    
                    self.log_message(f"⏳ Esperando {self.var_wait_time.get()} segundos...", "warning")
                    
                    # Esperar
                    for _ in range(self.var_wait_time.get()):
                        if not self.enviando:
                            break
                        time.sleep(1)
                    
                    if self.enviando:
                        # Presionar ENTER
                        pyautogui.press("enter")
                        self.log_message(f"✅ Mensaje enviado correctamente a {phone}", "success")
                        time.sleep(5)
                    
                except Exception as e:
                    self.log_message(f"❌ Error al enviar a {phone}: {str(e)}", "error")
                    time.sleep(3)
            
            if self.enviando:
                self.log_message("\n✅ Proceso completado. Todos los mensajes fueron enviados o intentados.", "success")
                self.update_status("Completado")
            else:
                self.update_status("Detenido")
        
        except Exception as e:
            self.log_message(f"\n❌ Error general: {str(e)}", "error")
            self.update_status("Error")
        
        finally:
            # Habilitar botones
            self.btn_stop.config(state="disabled")
            self.notebook.tab(1, state="normal")
            self.notebook.tab(2, state="normal")
            self.notebook.tab(3, state="normal")
            self.enviando = False
    
    def update_status(self, status):
        """Actualizar el estado"""
        self.label_status.config(text=f"Estado: {status}")
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppGUI(root)
    root.mainloop()
