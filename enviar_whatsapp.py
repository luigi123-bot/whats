import pywhatkit as kit
import time
import pyautogui

# 📱 Lista de números de los estudiantes
numbers = [
    '573012906861',
  
]

# 💬 Mensaje
mensaje = (
    "Hola queridos estudiantes interesados en el curso de inyectología.\n\n"
    "Recuerden que se llevará a cabo el 8 y 15 de Nov. De 1pm a 5pm.\n\n"
    "Por un valor de $100.000, que deben estar pagos para separar tu cupo el 4 de Noviembre.\n\n"
    "Cupos limitados, no te quedes sin el tuyo.\n\n"
    "Realiza tu pago al número de cuenta habitual y envía el comprobante aquí con tu nombre completo.\n\n"
    "Comunícate: 302 5270747"
)

# ⏰ Tiempo de espera después de abrir WhatsApp Web
tiempo_espera = 15  # segundos

print("Abre WhatsApp Web en tu navegador antes de continuar.\n")
time.sleep(5)

for i, numero in enumerate(numbers, 1):
    phone = f"+{numero}"
    print(f"[{i}/{len(numbers)}] Enviando mensaje a {phone}...")
    try:
        # Abre WhatsApp y espera
        kit.sendwhatmsg_instantly(phone, mensaje, wait_time=20, tab_close=True)
        print(f"Esperando {tiempo_espera} segundos para que cargue WhatsApp Web...")
        time.sleep(tiempo_espera)

        # Presiona ENTER para enviar el mensaje
        pyautogui.press("enter")

        print(f"[OK] Mensaje enviado correctamente a {phone}\n")
        time.sleep(5)  # espera antes de pasar al siguiente número

    except Exception as e:
        print(f"[ERROR] No se pudo enviar el mensaje a {phone}: {e}\n")
        time.sleep(3)

print("✅ Proceso completado. Todos los mensajes fueron enviados o intentados.")
