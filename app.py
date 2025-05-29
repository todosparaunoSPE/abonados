# -*- coding: utf-8 -*-
"""
Created on Thu May 29 12:31:37 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
from streamlit_folium import folium_static
import time

# -----------------------------------------------
# Configuración inicial de la página
# -----------------------------------------------
st.set_page_config(
    page_title="¡Soy Javier Horacio Pérez ricárdez | Asesor Jr. de Abonados - Atlético de San Luis",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------
# CSS Personalizado (para estilo del equipo)
# -----------------------------------------------
st.markdown("""
<style>
    .stApp { background-color: #F0F2F6; }
    .css-1d391kg { padding-top: 3rem; }
    h1 { color: #E30613; }  /* Rojo del equipo */
    .st-bb { background-color: #E30613; }
    .st-at { background-color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------
# Header con Logo y Título
# -----------------------------------------------
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Escudo_del_Atl%C3%A9tico_de_San_Luis.svg/1200px-Escudo_del_Atl%C3%A9tico_de_San_Luis.svg.png", width=150)
with col2:
    st.title("Asesor Jr. de Atención al Abonado")
    st.markdown("**¡Hola reclutadores! Soy [Tu Nombre], y quiero fortalecer la conexión entre el club y su afición.** ⚽")

# -----------------------------------------------
# Sección 1: Importancia del Abonado
# -----------------------------------------------
st.header("📊 La importancia estratégica del abonado")
st.write("""
Los abonados representan el **80% de los ingresos recurrentes** de un club (Forbes, 2023).  
Mi enfoque: **proactividad + personalización** para fidelizarlos.
""")

# Gráfico de satisfacción
data = pd.DataFrame({
    "Año": [2021, 2022, 2023],
    "Satisfacción (%)": [65, 75, 82]
})
fig, ax = plt.subplots()
ax.plot(data["Año"], data["Satisfacción (%)"], marker="o", color="#E30613", linewidth=3)
ax.set_facecolor("#F5F5F5")
ax.set_title("Tendencia de Satisfacción de Abonados", pad=20, fontweight="bold")
st.pyplot(fig)

# -----------------------------------------------
# Sección 2: Mapa Interactivo del Estadio
# -----------------------------------------------
st.header("🏟️ Mapa del Estadio Alfonso Lastras")
st.write("Zonas clave para la experiencia del abonado:")

# Configuración del mapa
m = folium.Map(location=[22.1194, -100.9375], zoom_start=16)
folium.Marker(
    [22.1194, -100.9375],
    popup="<b>Zona Abonados</b><br>Acceso preferencial",
    tooltip="Taquillas Centrales",
    icon=folium.Icon(color="red", icon="ticket")
).add_to(m)
folium.CircleMarker(
    [22.1196, -100.9380],
    radius=50,
    popup="<b>Área VIP</b>",
    color="#E30613",
    fill=True
).add_to(m)
folium_static(m, width=800)

# -----------------------------------------------
# Sección 3: Simulador de Atención al Abonado
# -----------------------------------------------
st.header("⚡ Simulador: Resolución de Casos Reales")
caso = st.selectbox("**Selecciona un escenario:**", [
    "Abonado enojado por cambio de asiento",
    "Socio que no recibió su beneficio",
    "Fan que quiere cancelar su membresía"
])

if st.button("🔍 Mostrar mi estrategia", type="primary"):
    if caso == "Abonado enojado por cambio de asiento":
        st.success("""
        🎯 **Solución propuesta:**  
        1. **Empatizar**: *"Sr. González, lamento el inconveniente. Su comodidad es prioridad."*  
        2. **Explicar**: Razones técnicas (ej: reacondicionamiento para su seguridad).  
        3. **Compensar**: Ofrecer 2 invitaciones al palco VIP + descuento del 20% en mercancía.  
        """)
    elif caso == "Socio que no recibió su beneficio":
        st.success("""
        🎯 **Solución propuesta:**  
        1. **Validar**: Verificar en sistema + foto de comprobante (si aplica).  
        2. **Resolver**: Enviar beneficio por mensajería urgente + bonificación del 10%.  
        3. **Prevenir**: Crear checklist digital para próximas entregas.  
        """)
    else:
        st.success("""
        🎯 **Solución propuesta:**  
        1. **Diagnosticar**: *"¿Qué motivo la cancelación, Sra. Pérez?"* (escucha activa).  
        2. **Retener**: Upgrade a membresía Gold por 3 meses sin costo.  
        3. **Feedback**: Implementar encuesta de salida para mejorar.  
        """)

# -----------------------------------------------
# Sección 4: Calendario de Partidos + Eventos
# -----------------------------------------------
st.header("📅 Agenda del Club (Próximos 30 días)")
calendario = pd.DataFrame({
    "Fecha": ["15/03/2024", "22/03/2024", "05/04/2024"],
    "Rival": ["América", "Monterrey", "Santos"],
    "Localía": ["Casa", "Fuera", "Casa"],
    "Evento": ["Día del Niño", "Meet & Greet", "Noche de Museos"],
    "Prioridad Abonados": ["Alta", "Media", "Alta"]
})
st.dataframe(
    calendario.style.applymap(
        lambda x: "background-color: #FFE6E6" if x == "Alta" else "",
        subset=["Prioridad Abonados"]
    ),
    hide_index=True,
    use_container_width=True
)

# -----------------------------------------------
# Sección 5: Encuesta de Satisfacción Interactiva
# -----------------------------------------------
st.header("📝 Simulador de Encuesta NPS")
col1, col2 = st.columns(2)
with col1:
    nps = st.slider("**Del 0 al 10, ¿recomendarías el club?**", 0, 10)
with col2:
    if nps >= 9:
        st.metric(label="Promotor", value="👍", delta="+5% vs 2023")
    elif nps >= 7:
        st.metric(label="Neutral", value="😐", delta="-2% vs 2023")
    else:
        st.metric(label="Detractor", value="👎", delta="¡Necesitamos mejorar!")

# -----------------------------------------------
# Sección 6: Dashboard de Métricas Clave
# -----------------------------------------------
st.header("📊 KPI's de Abonados (Simulados)")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Abonados 2024", "9,421", "+18% YoY")
kpi2.metric("Retención", "87%", "Meta: 90%")
kpi3.metric("Tiempo Respuesta", "1.8 hrs", "🔽 0.5 hrs")
kpi4.metric("Eventos", "24/30", "+120% participación")

# -----------------------------------------------
# Sección 7: Video Embed (Motivación Personal)
# -----------------------------------------------
st.header("🎥 Auténticos GOLAZOS del ATLÉTICO DE SAN LUIS en el ALFONSO LASTRAS | 2024/2025 | Liga MX")
st.video("https://www.youtube.com/watch?v=oiGL43BlIsw")  # Reemplaza con tu video

# -----------------------------------------------
# Footer con Contacto
# -----------------------------------------------
st.markdown("---")
st.markdown("""
**⚡ ¿Listos para llevar la experiencia del abonado al siguiente nivel?**  
📩 Contáctame: [jahoperi@gmail.com] | 📱 [+52 56 1056 4095]  
""")

# -----------------------------------------------
# Bonus: Efecto de confeti al cargar (opcional)
# -----------------------------------------------
st.balloons()
