from datetime import datetime

now = datetime.now()
print(f"Hola, Manuel!")
print(f"Son las {now.strftime('%H:%M:%S')} del {now.strftime('%d/%m/%Y')}.")
