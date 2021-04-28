from random import sample
import wifi_qrcode_generator as qr
import time
import os

html = '''
<html>
	<head>
		<meta http-equiv="refresh" content="5">
		<title>WiFi Login</title>
	</head>
	<body>
		<table width="100%" height="100%"><tbody><tr><td><center><span style="font-size:100px;">
		<img src="passphrase.png" style="width: 50vh;"><br>
        {}
		</span></center></td></tr></tbody></table>
	</body>
</html>
'''

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "words.txt")) as f:
	words = f.read().splitlines()
	while True:		
		n = 4
		passphrase = '-'.join(sample(words,n))
		with open(os.path.join(dir_path, "../passphrase"),"w") as f, open(os.path.join(dir_path, "../index.html"),"w") as f1:
			f.write(passphrase)
			f1.write(html.format(passphrase))
		q = qr.wifi_qrcode('cs528',False,'WPA',passphrase)
		q.save(os.path.join(dir_path, "../passphrase.png"))
		time.sleep(30)
