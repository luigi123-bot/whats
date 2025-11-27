import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import pywhatkit as kit
import pyautogui
import time
import threading
from PIL import Image, ImageTk
import io

class ModernWhatsAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📱 WhatsApp Messenger - Envío Masivo")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configurar estilo
        self.setup_styles()
        
        # Variable para controlar el envío
        self.enviando = False
        
        # Crear GUI principal
        self.create_main_interface()
    
    def setup_styles(self):
        """Configurar estilos y colores"""
        self.root.configure(bg="#0f1419")
        
        # Colores del tema
        self.bg_dark = "#0f1419"
        self.bg_card = "#1e1f26"
        self.bg_hover = "#2a2c34"
        self.text_primary = "#ffffff"
        self.text_secondary = "#a0a3a8"
        self.accent_green = "#25d366"
        self.accent_blue = "#0078d4"
        self.accent_red = "#ff3b30"
        self.accent_yellow = "#ffa500"
        
        # Configurar tema
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores base
        style.configure("TFrame", background=self.bg_dark)
        style.configure("TLabel", background=self.bg_dark, foreground=self.text_primary)
        style.configure("TButton", background=self.bg_card, foreground=self.text_primary)
        style.configure("Card.TFrame", background=self.bg_card, relief="flat")
        
        # Estilos personalizados para botones
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"))
        style.configure("Secondary.TButton", font=("Segoe UI", 9))
    
    def create_main_interface(self):
        """Crear interfaz principal"""
        # Header
        self.create_header()
        
        # Contenido principal con dos columnas
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Columna izquierda
        left_column = ttk.Frame(main_frame)
        left_column.pack(side="left", fill="both", expand=True, padx=(0, 7))
        
        self.create_numbers_section(left_column)
        self.create_message_section(left_column)
        
        # Columna derecha
        right_column = ttk.Frame(main_frame)
        right_column.pack(side="right", fill="both", expand=True, padx=(7, 0))
        
        self.create_settings_section(right_column)
        self.create_log_section(right_column)
    
    def create_header(self):
        """Crear encabezado"""
        header = ttk.Frame(self.root)
        header.pack(fill="x", padx=15, pady=(15, 10))
        
        title_frame = ttk.Frame(header)
        title_frame.pack(fill="x")
        
        # Emoji + Título
        title_label = ttk.Label(title_frame, text="📱 WhatsApp Messenger", 
                               font=("Segoe UI", 24, "bold"), foreground=self.accent_green)
        title_label.pack(side="left", padx=0)
        
        # Subtítulo
        subtitle = ttk.Label(header, text="Envía mensajes masivos de forma fácil y rápida", 
                            font=("Segoe UI", 10), foreground=self.text_secondary)
        subtitle.pack(side="left", anchor="w", padx=0, pady=(10, 0))
    
    def create_numbers_section(self, parent):
        """Sección de números"""
        # Card
        card = ttk.Frame(parent, style="Card.TFrame")
        card.pack(fill="both", padx=0, pady=(0, 10))
        
        # Título con icono
        title_frame = ttk.Frame(card)
        title_frame.pack(fill="x", padx=15, pady=(15, 10))
        
        title = ttk.Label(title_frame, text="📞 Números de Teléfono", 
                         font=("Segoe UI", 12, "bold"), foreground=self.accent_blue)
        title.pack(anchor="w")
        
        info = ttk.Label(title_frame, text="Ingresa los números separados por saltos de línea (sin +)", 
                        font=("Segoe UI", 8), foreground=self.text_secondary)
        info.pack(anchor="w", padx=0, pady=(5, 0))
        
        # Text widget
        self.text_numbers = scrolledtext.ScrolledText(
            card, height=8, width=40, wrap=tk.WORD,
            bg=self.bg_dark, fg=self.text_primary, insertbackground=self.accent_green,
            font=("Consolas", 9), relief="solid", borderwidth=1
        )
        self.text_numbers.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        
        # Botones
        btn_frame = ttk.Frame(card)
        btn_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        btn_load = ttk.Button(btn_frame, text="📂 Cargar archivo", command=self.load_numbers)
        btn_load.pack(side="left", padx=(0, 5))
        
        btn_clean = ttk.Button(btn_frame, text="🧹 Limpiar números", command=self.clean_and_format_numbers)
        btn_clean.pack(side="left", padx=5)
        
        btn_clear = ttk.Button(btn_frame, text="🗑️ Limpiar", 
                              command=lambda: self.text_numbers.delete("1.0", tk.END))
        btn_clear.pack(side="left", padx=5)
        
        # Número de teléfono contador
        self.label_count_numbers = ttk.Label(btn_frame, text="0 números", 
                                            font=("Segoe UI", 9), foreground=self.text_secondary)
        self.label_count_numbers.pack(side="right", padx=0)
        
        # Agregar números de ejemplo
        example_text = "573012906861\n573001234567\n573009876543"
        self.text_numbers.insert("1.0", example_text)
        self.update_numbers_count()
        
        # Bind para actualizar contador
        self.text_numbers.bind("<<Change>>", lambda e: self.update_numbers_count())
        self.text_numbers.bind("<KeyRelease>", lambda e: self.update_numbers_count())
    
    def create_message_section(self, parent):
        """Sección de mensaje"""
        # Card
        card = ttk.Frame(parent, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=0, pady=(0, 0))
        
        # Título con icono
        title_frame = ttk.Frame(card)
        title_frame.pack(fill="x", padx=15, pady=(15, 10))
        
        title = ttk.Label(title_frame, text="💬 Mensaje a Enviar", 
                         font=("Segoe UI", 12, "bold"), foreground=self.accent_blue)
        title.pack(anchor="w")
        
        info = ttk.Label(title_frame, text="Personaliza el mensaje para tus contactos", 
                        font=("Segoe UI", 8), foreground=self.text_secondary)
        info.pack(anchor="w", padx=0, pady=(5, 0))
        
        # Text widget
        self.text_message = scrolledtext.ScrolledText(
            card, height=12, width=40, wrap=tk.WORD,
            bg=self.bg_dark, fg=self.text_primary, insertbackground=self.accent_green,
            font=("Segoe UI", 9), relief="solid", borderwidth=1
        )
        self.text_message.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        
        # Botón de limpiar
        btn_frame = ttk.Frame(card)
        btn_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        btn_clear = ttk.Button(btn_frame, text="🗑️ Limpiar mensaje", 
                              command=lambda: self.text_message.delete("1.0", tk.END))
        btn_clear.pack(side="left")
        
        # Contador de caracteres
        self.label_char_count = ttk.Label(btn_frame, text="0 caracteres", 
                                         font=("Segoe UI", 9), foreground=self.text_secondary)
        self.label_char_count.pack(side="right")
        
        # Mensaje por defecto
        default_message = """Hola queridos estudiantes interesados en el curso de inyectología.

Recuerden que se llevará a cabo el 8 y 15 de Nov. De 1pm a 5pm.

Por un valor de $100.000, que deben estar pagos para separar tu cupo el 4 de Noviembre.

Cupos limitados, no te quedes sin el tuyo.

Realiza tu pago al número de cuenta habitual y envía el comprobante aquí con tu nombre completo.

Comunícate: 302 5270747"""
        
        self.text_message.insert("1.0", default_message)
        self.update_char_count()
        
        # Bind para actualizar contador
        self.text_message.bind("<KeyRelease>", lambda e: self.update_char_count())
    
    def create_settings_section(self, parent):
        """Sección de configuración"""
        # Card
        card = ttk.Frame(parent, style="Card.TFrame")
        card.pack(fill="x", padx=0, pady=(0, 10))
        
        # Título
        title = ttk.Label(card, text="⚙️ Configuración", 
                         font=("Segoe UI", 12, "bold"), foreground=self.accent_blue)
        title.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Tiempo de espera entre mensajes
        frame1 = ttk.Frame(card)
        frame1.pack(fill="x", padx=15, pady=7)
        
        ttk.Label(frame1, text="Espera entre mensajes (seg):", font=("Segoe UI", 9)).pack(side="left")
        self.var_wait_time = tk.IntVar(value=15)
        ttk.Spinbox(frame1, from_=5, to=60, textvariable=self.var_wait_time, width=8).pack(side="right")
        
        # Tiempo para cargar WhatsApp
        frame2 = ttk.Frame(card)
        frame2.pack(fill="x", padx=15, pady=7)
        
        ttk.Label(frame2, text="Tiempo para cargar WhatsApp (seg):", font=("Segoe UI", 9)).pack(side="left")
        self.var_tab_wait = tk.IntVar(value=20)
        ttk.Spinbox(frame2, from_=5, to=60, textvariable=self.var_tab_wait, width=8).pack(side="right")
        
        # Cerrar pestaña
        frame3 = ttk.Frame(card)
        frame3.pack(fill="x", padx=15, pady=10)
        
        self.var_tab_close = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame3, text="Cerrar pestaña automáticamente", 
                       variable=self.var_tab_close).pack(anchor="w")
        
        ttk.Separator(card, orient="horizontal").pack(fill="x", padx=15, pady=(10, 0))
    
    def create_log_section(self, parent):
        """Sección de registro"""
        # Card
        card = ttk.Frame(parent, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=0)
        
        # Título
        title = ttk.Label(card, text="📋 Registro de Envíos", 
                         font=("Segoe UI", 12, "bold"), foreground=self.accent_blue)
        title.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Text widget
        self.text_log = scrolledtext.ScrolledText(
            card, height=15, width=35, wrap=tk.WORD,
            bg=self.bg_dark, fg=self.text_primary, insertbackground=self.accent_green,
            font=("Consolas", 8), relief="solid", borderwidth=1
        )
        self.text_log.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        
        # Configurar etiquetas de color
        self.text_log.tag_config("info", foreground="#ffffff")
        self.text_log.tag_config("success", foreground=self.accent_green)
        self.text_log.tag_config("error", foreground=self.accent_red)
        self.text_log.tag_config("warning", foreground=self.accent_yellow)
        
        # Botones de acción
        btn_frame = ttk.Frame(card)
        btn_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        # Botón Enviar
        self.btn_send = tk.Button(btn_frame, text="▶️ INICIAR ENVÍO", 
                                  command=self.start_sending, font=("Segoe UI", 11, "bold"),
                                  bg=self.accent_green, fg="#000000", relief="flat",
                                  activebackground="#1fb854", activeforeground="#000000",
                                  cursor="hand2", padx=20, pady=10)
        self.btn_send.pack(side="left", padx=(0, 5), fill="x", expand=True)
        
        # Botón Detener
        self.btn_stop = tk.Button(btn_frame, text="⏹️ DETENER", 
                                 command=self.stop_sending, font=("Segoe UI", 11, "bold"),
                                 bg=self.accent_red, fg="#ffffff", relief="flat", state="disabled",
                                 activebackground="#cc2f24", activeforeground="#ffffff",
                                 cursor="hand2", padx=20, pady=10)
        self.btn_stop.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botón Limpiar Log
        btn_clear_log = tk.Button(btn_frame, text="🗑️", 
                                 command=lambda: self.text_log.delete("1.0", tk.END),
                                 font=("Segoe UI", 10), bg=self.bg_card, fg=self.text_secondary,
                                 relief="flat", activebackground=self.bg_hover,
                                 cursor="hand2", width=3, pady=8)
        btn_clear_log.pack(side="left", padx=5)
        
        # Estado
        self.label_status = ttk.Label(card, text="🟢 Listo", 
                                     font=("Segoe UI", 10, "bold"), foreground=self.accent_green)
        self.label_status.pack(anchor="w", padx=15, pady=(0, 10))
    
    def update_numbers_count(self):
        """Actualizar contador de números"""
        numbers_text = self.text_numbers.get("1.0", tk.END).strip()
        count = len([n for n in numbers_text.split('\n') if n.strip()])
        self.label_count_numbers.config(text=f"{count} número(s)")
    
    def update_char_count(self):
        """Actualizar contador de caracteres"""
        message = self.text_message.get("1.0", tk.END).strip()
        count = len(message)
        self.label_char_count.config(text=f"{count} carácter(es)")
    
    def load_numbers(self):
        """Cargar números desde un archivo"""
        file_path = filedialog.askopenfilename(
            title="Selecciona archivo de números",
            filetypes=[("Archivos de texto", "*.txt"), ("CSV", "*.csv"), ("Todos", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    numbers = f.read()
                self.text_numbers.delete("1.0", tk.END)
                self.text_numbers.insert("1.0", numbers)
                self.log_message(f"✅ Se cargaron números desde: {file_path}", "success")
                self.update_numbers_count()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
                self.log_message(f"❌ Error al cargar archivo: {e}", "error")
    
    def clean_and_format_numbers(self):
        """Limpiar y formatear números de teléfono"""
        numbers_text = self.text_numbers.get("1.0", tk.END).strip()
        
        if not numbers_text:
            messagebox.showwarning("Advertencia", "No hay números para limpiar.")
            return
        
        # Procesar números
        cleaned_numbers = []
        for line in numbers_text.split('\n'):
            # Limpiar espacios en blanco
            number = line.strip()
            
            if not number:
                continue
            
            # Remover caracteres especiales comunes
            number = number.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
            number = number.replace('+', '')  # Remover + si existe
            
            # Remover 0 al inicio si existe (para números colombianos)
            if number.startswith('0'):
                number = number[1:]
            
            # Agregar código de país si no lo tiene
            if not number.startswith('57'):
                number = '57' + number
            
            # Solo agregar si tiene una longitud razonable
            if len(number) >= 10:  # Mínimo para un número colombiano
                cleaned_numbers.append(number)
        
        if cleaned_numbers:
            # Mostrar números limpios en el text widget
            self.text_numbers.delete("1.0", tk.END)
            cleaned_text = '\n'.join(cleaned_numbers)
            self.text_numbers.insert("1.0", cleaned_text)
            
            # Actualizar contador
            self.update_numbers_count()
            
            # Log
            duplicados_removidos = len(numbers_text.split('\n')) - len(cleaned_numbers)
            self.log_message(f"✅ Números limpios: {len(cleaned_numbers)}", "success")
            if duplicados_removidos > 0:
                self.log_message(f"   📍 Se removieron {duplicados_removidos} líneas vacías/inválidas", "warning")
            self.log_message(f"   ✓ Código de país (+57) agregado", "success")
        else:
            messagebox.showwarning("Advertencia", "No se encontraron números válidos para limpiar.")
            self.log_message("❌ No se encontraron números válidos", "error")
    
    def log_message(self, message, tag="info"):
        """Agregar mensaje al log"""
        timestamp = time.strftime("%H:%M:%S")
        self.text_log.insert(tk.END, f"[{timestamp}] {message}\n", tag)
        self.text_log.see(tk.END)
        self.text_log.update()
    
    def start_sending(self):
        """Iniciar el envío de mensajes"""
        numbers_text = self.text_numbers.get("1.0", tk.END).strip()
        message = self.text_message.get("1.0", tk.END).strip()
        
        if not numbers_text:
            messagebox.showwarning("Advertencia", "Por favor ingresa al menos un número de teléfono.")
            return
        
        if not message:
            messagebox.showwarning("Advertencia", "Por favor ingresa un mensaje.")
            return
        
        numbers = [n.strip() for n in numbers_text.split('\n') if n.strip()]
        respuesta = messagebox.askyesno("Confirmación", 
                                       f"¿Enviar mensaje a {len(numbers)} número(s)?\n\n"
                                       "⚠️ Asegúrate de tener WhatsApp Web abierto.")
        
        if respuesta:
            # Deshabilitar UI
            self.btn_send.config(state="disabled")
            self.btn_stop.config(state="normal")
            self.text_numbers.config(state="disabled")
            self.text_message.config(state="disabled")
            
            # Ejecutar en hilo
            self.enviando = True
            thread = threading.Thread(target=self.send_messages, args=(numbers, message))
            thread.daemon = True
            thread.start()
    
    def stop_sending(self):
        """Detener el envío"""
        self.enviando = False
        self.log_message("⏸️ Envío detenido por el usuario.", "warning")
        self.update_status("Detenido")
    
    def update_status(self, status):
        """Actualizar estado"""
        status_icons = {
            "Listo": "🟢",
            "Enviando": "🔵",
            "Completado": "✅",
            "Detenido": "🟡",
            "Error": "🔴"
        }
        icon = status_icons.get(status, "🔘")
        self.label_status.config(text=f"{icon} {status}")
        self.root.update()
    
    def send_messages(self, numbers, message):
        """Enviar mensajes"""
        try:
            self.update_status("Enviando")
            self.log_message(f"📤 Iniciando envío de {len(numbers)} mensaje(s)...", "info")
            self.log_message("=" * 40, "info")
            time.sleep(2)
            
            for i, numero in enumerate(numbers, 1):
                if not self.enviando:
                    break
                
                # Formatar número con + si no lo tiene
                numero_limpio = numero.strip()
                if not numero_limpio.startswith('+'):
                    phone = f"+{numero_limpio}"
                else:
                    phone = numero_limpio
                
                self.log_message(f"📍 [{i}/{len(numbers)}] {phone}", "info")
                
                try:
                    # Enviar mensaje
                    kit.sendwhatmsg_instantly(
                        phone, 
                        message, 
                        wait_time=self.var_tab_wait.get(), 
                        tab_close=self.var_tab_close.get()
                    )
                    
                    self.log_message(f"   ⏳ Esperando {self.var_wait_time.get()}s...", "warning")
                    
                    # Esperar
                    for _ in range(self.var_wait_time.get()):
                        if not self.enviando:
                            break
                        time.sleep(1)
                    
                    if self.enviando:
                        # Presionar ENTER
                        pyautogui.press("enter")
                        self.log_message(f"   ✅ Enviado", "success")
                        time.sleep(3)
                    
                except Exception as e:
                    self.log_message(f"   ❌ Error: {str(e)}", "error")
                    time.sleep(2)
            
            self.log_message("=" * 40, "info")
            
            if self.enviando:
                self.log_message("✅ ¡Proceso completado exitosamente!", "success")
                self.update_status("Completado")
                messagebox.showinfo("Éxito", "¡Todos los mensajes fueron enviados!")
            else:
                self.update_status("Detenido")
        
        except Exception as e:
            self.log_message(f"❌ Error general: {str(e)}", "error")
            self.update_status("Error")
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
        
        finally:
            # Habilitar UI
            self.btn_send.config(state="normal")
            self.btn_stop.config(state="disabled")
            self.text_numbers.config(state="normal")
            self.text_message.config(state="normal")
            self.enviando = False

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernWhatsAppGUI(root)
    root.mainloop()
