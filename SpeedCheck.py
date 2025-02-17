import speedtest

def obtener_velocidad_wifi():
    st = speedtest.Speedtest()
    st.get_best_server()

    descarga = st.download() / 1_000_000 # Convertir de bits a megabits (Mbps)
    subida = st.upload() / 1_000_000 # Convertir de bits a megabits (Mbps)

    print(f"Velocidad de descarga: {descarga:.2f} Mbps")
    print(f"Velocidad de subida: {subida:.2f} Mbps")

if __name__ == "__main__":
    obtener_velocidad_wifi()
