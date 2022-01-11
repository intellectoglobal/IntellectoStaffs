#INTERNET SPEED TEST
#Install it on your system by using the pip command
#pip install speedtest-cli
# import speedtest
# wifi  = speedtest.Speedtest()
# print("Wifi Download Speed is ", wifi.download())
# print("Wifi Upload Speed is ", wifi.upload())

import speedtest as st

s = st.Speedtest()

print("Testing ....")

downloadSpeed = s.download() / 1048576
uploadSpeed = s.upload() / 1048576
pingResult = round(s.results.ping)


print(f"Download speed : {downloadSpeed:.2f} Mbps")
print(f"Upload speed : {uploadSpeed:.2f} Mbps")
print(f"Ping : {pingResult} Ms")