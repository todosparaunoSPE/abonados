# -*- coding: utf-8 -*-
"""
Created on Thu May 29 12:31:37 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
from io import StringIO

# --- Simular abonados de ejemplo ---
def simular_abonados():
    datos = {
        "ID": [str(uuid.uuid4())[:8] for _ in range(5)],
        "Nombre": ["Carlos Pérez", "Ana García", "Luis Torres", "Marta León", "José Ruiz"],
        "Email": ["carlos@mail.com", "ana@mail.com", "luis@mail.com", "marta@mail.com", "jose@mail.com"],
        "Teléfono": ["5551234567", "5552345678", "5553456789", "5554567890", "5555678901"],
        "Estatus": ["Activo", "Vencido", "Activo", "Cancelado", "Activo"],
        "Última Situación": ["Ninguna"]*5,
        "Fecha Última Actualización": [datetime.now().strftime("%Y-%m-%d %H:%M")]*5
    }
    return pd.DataFrame(datos)

# Inicializar sesión con datos simulados
if "abonados" not in st.session_state:
    st.session_state.abonados = simular_abonados()

st.title("📋 Gestión de Abonados - Atlético de San Luis")

# --- Agregar nuevo abonado ---
st.sidebar.header("➕ Registrar Abonado Nuevo")
with st.sidebar.form("nuevo_abonado"):
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono")
    estatus = st.selectbox("Estatus", ["Activo", "Vencido", "Cancelado"])
    submit = st.form_submit_button("Guardar")
    if submit and nombre and email:
        nuevo = {
            "ID": str(uuid.uuid4())[:8],
            "Nombre": nombre,
            "Email": email,
            "Teléfono": telefono,
            "Estatus": estatus,
            "Última Situación": "Ninguna",
            "Fecha Última Actualización": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        st.session_state.abonados = pd.concat([st.session_state.abonados, pd.DataFrame([nuevo])], ignore_index=True)
        st.success("✅ Abonado registrado exitosamente.")

# --- Mostrar y filtrar abonados ---
st.subheader("📄 Lista de Abonados")
filtro_estatus = st.selectbox("Filtrar por estatus", ["Todos"] + list(st.session_state.abonados["Estatus"].unique()))
df_filtrado = st.session_state.abonados if filtro_estatus == "Todos" else st.session_state.abonados[st.session_state.abonados["Estatus"] == filtro_estatus]
st.dataframe(df_filtrado, use_container_width=True)

# --- Registrar situación ---
st.subheader("📝 Registrar Situación o Incidencia")
abonado_nombres = st.session_state.abonados["Nombre"].tolist()

if abonado_nombres:
    seleccionado = st.selectbox("Seleccionar abonado", abonado_nombres)
    situacion = st.text_area("Descripción de la situación")
    guardar_situacion = st.button("Registrar situación")

    if guardar_situacion and situacion:
        index = st.session_state.abonados[st.session_state.abonados["Nombre"] == seleccionado].index[0]
        st.session_state.abonados.at[index, "Última Situación"] = situacion
        st.session_state.abonados.at[index, "Fecha Última Actualización"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.success("📌 Situación registrada exitosamente.")

# --- Exportar datos a CSV ---
st.sidebar.header("📤 Exportar datos")

csv_buffer = StringIO()
st.session_state.abonados.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

st.sidebar.download_button(
    label="📥 Descargar Abonados CSV",
    data=csv_data,
    file_name="abonados.csv",
    mime="text/csv"
)
