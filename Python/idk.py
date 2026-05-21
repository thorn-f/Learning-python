import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    print("Checking internet speed...")
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    return {
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),
        "ping": round(ping, 2)
    }

speed = check_internet_speed()
print(f"Download Speed: {speed['download']} Mbps")
print(f"Upload Speed: {speed['upload']} Mbps")
print(f"Ping: {speed['ping']} ms")
