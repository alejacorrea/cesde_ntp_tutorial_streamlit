import streamlit as st
import random

st.title("Ejercicios de Streamlit")

# Ejercicio 1: Saludo Simple
st.subheader("1. Saludo Simple")

nombre = st.text_input("Escribe tu nombre: ")

if nombre:
    st.success(f"¡Hola, {nombre}!")

st.divider()

# Ejercicio 2: Calculadora de Producto

st.subheader("2. Calculadora de Producto")

num1 = st.number_input("Número 1", value=0)
num2 = st.number_input("Número 2", value=0)

resultado = num1 * num2
st.write(f"Resultado: {resultado}")

if num1 > 100 or num2 > 100:
    st.warning("Números grandes.")

st.divider()

# Ejercicio 3: Convertidor de Temperatura

st.subheader("3. Convertidor de Temperatura")

opcion = st.radio(
    "Selecciona la conversión:",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius")
)

temp = st.number_input("Ingresa la temperatura: ")

if opcion == "Celsius a Fahrenheit":
    resultado = (temp * 9/5) + 32
    st.write(f"{temp} °C = {resultado:.2f} °F")
else:
    resultado = (temp - 32) * 5/9
    st.write(f"{temp} °F = {resultado:.2f} °C")

st.divider()

# Ejercicio 4: Galeria de Mascotas

st.subheader("4. Galería de Mascotas")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.image("https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=600")
    if st.button("Me gusta el gato", key= "gato"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.image("https://images.unsplash.com/photo-1558788353-f76d92427f16?w=600")
    if st.button("Me gusta el perro", key= "perro"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.image("https://images.unsplash.com/photo-1444464666168-49d633b86797?w=600")
    if st.button("Me gusta el ave", key= "ave"):
        st.toast("Te gusta esta mascota")

st.divider()

# Ejercicio 5: Formulario

st.subheader("5. Caja de Comentarios")

with st.form("formulario"):
    asunto = st.text_input("Asunto")
    mensaje = st.text_area("Mensaje")
    enviar = st.form_submit_button("Enviar")

if enviar:
    if mensaje:
        st.json({
            "asunto": asunto, 
            "mensaje": mensaje
            })
    else:
        st.error("El mensaje no puede estar vacío.")

st.divider()

# Ejercicio 6: Login simulado

st.subheader("6. Login Simulado")

if "logueado" not in st.session_state:
    st.session_state.logueado = False

if not st.session_state.logueado:
    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        if usuario == "admin" and password == "1234":
            st.session_state.logueado = True
            st.success("Ingreso exitoso")
        else:
            st.error("Credenciales incorrectas.")
else:
    st.success("Ya estas logueado.")
    if st.button("Cerrar sesión"):
        st.session_state.logueado = False

st.divider()

# Ejercicio 7: Lista de compras

st.subheader("7. Lista de Compras")

if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

producto = st.text_input("Producto")

col1, col2 = st.columns(2)

with col1:
    if st.button("Agregar"):
        if producto:
            st.session_state.lista_compras.append(producto)
            
with col2:
    if st.button("Limpiar"):
        st.session_state.lista_compras = []

st.write("Lista actual: ")
st.write(st.session_state.lista_compras)

st.divider()

# Ejercicio 8: Grafico Interactivo

st.subheader("8. Gráfico Interactivo")

N = st.slider("Selecciona N", 10, 100, 20)
datos = [random.randint(0, 100) for _ in range(N)]
st.line_chart(datos)

if st.button("Regenerar"):
    st.rerun()