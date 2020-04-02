import sys, time, requests
from termcolor import colored

def getStatus(url):
	request = requests.get(url)
	return request.status_code

def splash():
	print(colored("""          _  __            
 _  _ _ _| |/ _|_  _ ______
| || | '_| |  _| || |_ /_ /
 \\_,_|_| |_|_|  \\_,_/__/__|""", "yellow"))

	print(colored("created by ", "green") + "https://github.com/kand0")

def scan(url, file):
	with open(file + '.txt') as fs:
		subs = fs.readlines()
		subs = [i.strip() for i in subs] 

		index = 0

		for i in subs:
			index += 1
			process = colored('\r[' + str(index) + '/' + str(len(subs)) + '] ')

			print(process + 'Checking: ' + i + ' ' * 20, end='')
			sys.stdout.flush()

			status = getStatus(url + i)
			if status == 200 or status == 403 or status == 401:
				print(colored('\n[Response:' + str(status) + '] ' + i, 'green'))

		print('')

def main():
	splash()

	URL = input(colored('[url: ] ', 'green'))
	TYPE = input(colored('[type(php, dir): ] ', 'green'))

	TYPE = TYPE.lower()

	if TYPE == 'php' or TYPE == 'dir': scan(URL, TYPE)
	else: print(colored('Invalid type', 'red'))

main()
