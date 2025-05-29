# -*- coding: utf-8 -*-
"""
Created on Thu May 29 12:31:37 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
st.set_page_config(page_title="¡Hola, Atlético de San Luis!", page_icon="⚽", layout="wide")

# Logo y título
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_del_Atl%C3%A9tico_de_San_Luis.svg/1200px-Escudo_del_Atl%C3%A9tico_de_San_Luis.svg.png", width=150)
with col2:
    st.title("Asesor Jr. de Atención al Abonado")
    st.markdown("**¡Hola reclutadores! Soy [Tu Nombre], y quiero ayudar a conectar el club con su afición.**")

# Sección 1: Por qué el abonado es lo primero
st.header("📊 La importancia del abonado en el fútbol")
st.write("""El 80% de los ingresos de un club viene de sus fans (ESPN, 2023). 
Mi rol sería asegurar que cada abonado se sienta **escuchado y valorado**.""")

# Gráfico de satisfacción (ejemplo)
data = pd.DataFrame({
    "Año": [2021, 2022, 2023],
    "Satisfacción": [65, 75, 82]  # Datos ficticios
})
fig, ax = plt.subplots()
ax.plot(data["Año"], data["Satisfacción"], marker="o", color="red")
ax.set_title("Satisfacción de Abonados (2021-2023)")
st.pyplot(fig)

# Sección 2: Simulador de atención al abonado
st.header("⚡ Simulador: Resolución de Casos")
problema = st.selectbox("**Selecciona un caso hipotético:**", [
    "Abonado enojado por cambio de asiento",
    "Socio que no recibió su beneficio",
    "Fan que quiere cancelar su membresía"
])

if st.button("¿Cómo lo resolvería?"):
    if problema == "Abonado enojado por cambio de asiento":
        st.success("""
        1. **Empatizar**: *"Entiendo su frustración, Sr. López."*  
        2. **Explicar**: Razones del cambio (ej. mantenimiento).  
        3. **Compensar**: Ofrecer descuento en próxima compra o meet-and-greet con jugador.  
        """)
    elif problema == "Socio que no recibió su beneficio":
        st.success("""
        1. **Verificar datos**: Confirmar en sistema.  
        2. **Solución rápida**: Enviar beneficio + bono adicional.  
        3. **Prevenir**: Reportar falla a TI para evitar repetición.  
        """)
    else:
        st.success("""
        1. **Escuchar**: ¿Por qué quiere cancelar?  
        2. **Retener**: Ofrecer upgrade gratis por 1 mes.  
        3. **Feedback**: Registrar causa para mejorar.  
        """)

# Sección 3: Tu valor agregado
st.header("🌟 ¿Por qué yo?")
st.markdown("""
- ✅ **Pasión por el fútbol**: Seguidor del Atlético desde [año].  
- ✅ **Habilidades blandas**: Comunicación asertiva (ejemplo: lideré quejas en mi trabajo anterior).  
- ✅ **Tecnología**: Uso de CRM como HubSpot o Zendesk (certificación opcional).  
- ✅ **Disponibilidad total**: ¡Incluso en Clásicos!  
""")

# Bonus: Link a video (opcional)
st.markdown("---")
st.video("https://youtu.be/ejemplo")  # Reemplaza con un video tuyo de 1 minuto

# Footer
st.markdown("**¡Gracias por la oportunidad!** ⚽ Contacto: [tu@email.com]")
