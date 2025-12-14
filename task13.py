from ipaddress import ip_network

net = ip_network("23.140.159.160/255.255.252.0", 0)

cnt = 0
for ip in net:
    ipb = f"{ip:b}"
    if ipb[:16].count("1") >= ipb[16:].count("1"):
        cnt += 1

print(cnt)
# Ответ: 176
