import requests
import json
import socket

field = {
        "method": "login",
        "params": {
            "username": "admin",
            "encryptedPassword":"7838e6523d0e994138820bb0040ec87c865aaaeea9bf1d40980170f7044112e11a97353d38341f1859d6afc7c0bbb40947339616d9d42a676ebb252afa885136ea579b1d55dec8502fd335cec77078187064f52c744e09b12f71d6e76aa2530c75d76aa084d7a2f241124f307d74f80b5725e6bab0bed613ac0cf345e3d00969",
            "keyId": "A9_0654hRtmzGmuXZkKdqw|Ok6DpQzZ639UdoKQizBe5yKkEtF7HBQg"
        }
}

field = json.dumps(field)
# exit()
# http = urllib3.PoolManager()
url = 'https://data.unikrn.com'
print(url.split("://")[1])
# r = http.request('POST', url, fields=data)
r = requests.post(url, data=field)
# bla = r.raw._connection.sock.getpeername()
# print(bla)
print('IP:', socket.gethostbyname('localhost.mail.ru'))