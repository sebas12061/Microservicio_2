# 📩 Microservicio de Notificaciones

## 📖 Descripción
Este microservicio se encarga de **gestionar y simular notificaciones** dentro del sistema.  
Permite crear nuevas notificaciones y listar las ya existentes.  
Las notificaciones cuentan con diferentes **tipos** (info, alerta, error, confirmación, etc.) y **estados** (enviada, pendiente, fallida).  

> 🚀 Actualmente este microservicio utiliza una **base de datos simulada en memoria**.

---

## ⚙️ Tecnologías
- Python 3.x
- Flask

---

## 🚀 Ejecución

1. Clonar el repositorio.
2. Crear entorno virtual e instalar dependencias:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # En Windows
   source .venv/bin/activate # En Linux/Mac
   pip install -r requirements.txt
3. Ejecutar:
    python app.py
4. Acceder a:
    http://127.0.0.1:5005
    
