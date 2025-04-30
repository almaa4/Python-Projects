import socket
import datetime

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("127.0.0.1", 9999))

print("UDP server listening on port number 9999.....")
try:
	while True:
		data, addr = udp_server.recvfrom(1024)
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S" )
		print(f"[{timestamp}] Received from {addr}:{data.decode(errors = 'ignore')}")
		udp_server.sendto(data,addr)

except KeyboardInterrupt:
	print("\n🛑 Server stopped by user...")
finally:
	udp_server.close()
