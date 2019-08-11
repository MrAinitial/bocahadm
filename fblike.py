# Name: Instan Like 4 FB
# 22-06-2019
# Coded by: A'Initial

def notice():
	h = '\033[92m'
	k = '\033[93m'
	m = '\033[91m'
	p = '\033[0m'
	from getpass import getpass as oh
	import os
	os.system('clear')
	print m + "		[Warning]\n" + p
	print "Memakai tool bisa membuat akun anda\ncheckpoint atau yg paling parah dibanned.\n"
	print "Silahkan konfirmasi indentitas dahulu\nsebelum memakai tool ini. Segala risiko\nditanggung user. Hiya Hiya Hiya :v\n"
	oh('[Tekan Enter Untuk Lanjut]')
	main()
	
def login():
	import requests as r, json, time, os
	from bs4 import BeautifulSoup as parser
	os.system('clear')
	h = '\033[92m'
	k = '\033[93m'
	m = '\033[91m'
	p = '\033[0m'
	print h + "Instan Like For FB\nCoded by: A'Initial\n" + p
	print "[+] Login To Your Account\n[+] Gw ga masang logger ya qmak"
	u = raw_input('[?] Username: ')
	pw = raw_input('[?] Password: ')
	print "[+] Sedang Login ...."
	get = r.post('https://yolikers.com:443/tokenmess.php', data={'u':u, 'p':pw}).text
	soup = parser(get, 'html.parser')
	link = soup.find('iframe').get('src')
	get_token = r.get(link).text
	if "session_key" in get_token:
		tuken = json.loads(get_token)
		open('token.txt', 'w').write(tuken['access_token'])
		print "[+] Login Sukses"
		time.sleep(2)
		main()
	elif "unavailable" in get_token:
		print "[+] Generate Failed! Your Account Checkpoint"
		exit()
	else:
		print "[+] Wrong Username/Password"
		exit()

def main():
	try:
		import requests as r, json, time, os
		from bs4 import BeautifulSoup as parser
		os.system('clear')
		h = '\033[92m'
		k = '\033[93m'
		m = '\033[91m'
		p = '\033[0m'
		print h + "Instan Like For FB\nCoded by: A'Initial\n" + p
		token = open('token.txt').read()
		cek = r.get('https://graph.facebook.com/me?access_token='+token).text
		if "error" in cek:
			login()
		else:
			pass
		print "[+] Login as " + h + json.loads(cek)['name'] + p
		id = raw_input('[?] Target Id: ')
		like_id = []
		data = r.get('https://graph.facebook.com/'+id+'/feed?access_token='+token+'&fields=id&limit=5000').text
		target = r.get('https://graph.facebook.com/'+id+'/?access_token='+token).json()['name']
		print "[+] Spam Like To " + h + target + p
		if "error" in data:
			print "[+] Invalid Id"
			exit()
		else:
			pass
		a = json.loads(data)
		for a1 in a['data']:
			like_id.append(a1['id'])
		next_id = a['paging']['next']
		try:
			while True:
				m1 = r.get(next_id).json()
				for m2 in m1['data']:
					like_id.append(m2['id'])
				next_id = m1['paging']['next']
		except KeyError:
			pass
			
				
		print ""
		for s in like_id:
			b = r.post('https://graph.facebook.com/'+s+'/likes?access_token='+token).text
			time.sleep(1)
			if "true" in b:
				print h + "[OK] " + p + s
			else:
				print m + "[FL] " + p + s
		print "\nDone!"
		exit()
		
	except ImportError:
		print "[+] need module requests and bs4"
	except IOError:
		login()
	except r.exceptions.ConnectionError:
		print "[+] Koneksi Error"
	except KeyboardInterrupt:
		print "[+] Exit: Ok"
	except NameError:
		main()
	except ImportError:
		print "[+] need module requests and bs4"
	

notice()