import requests
import random
key, secret = "epMPhY33tN1i_TSS4ywFuhv62kHYKVgpNQi", "9HznJNRoQyCAYjWoqQivXE"

def check(domain):
	"""
	Function to make an API request given the proper authorization headers to check the domain validity.
	Information is printed to the terminal shell, and also appended to an text file.
	"""
	response = requests.request("GET", 
		f"https://api.godaddy.com/v1/domains/available?domain={domain}&checkType=FAST&forTransfer=false", 
		headers = {"Authorization": f"sso-key {key}:{secret}"}
		)
	if "\"available\":true" in response.text:
		print(response.text)
		with open("available.txt", 'a') as file:
			file.write(response.text)

def genNames(word, after=False, length=1, num=100, exten='.com'):
	"""
	Function that generates the randomized name combinations of a domain to be stored in a text file.
	word, defines the name or word you would like the domain to have.
	after, defines whether the randomized text will be after the word.
	length, defines the length of the generated random text,
	num, defines the number of domains to generate.
	exten, defines the extention of the domain.

	"""
	chrs = 'abcdefghjklmnopqrstuvwxyz'
	for x in range(1, num + 1):
		result = ''.join(random.choice(chrs) for _ in range(length))
		my_result = (word + result if after else result + word) + exten
		f = open("domains.txt", "a")
		f.write(my_result + "\n")
	f.close()
	
def genDomains():
	"""
	Function which will check the domains apart of the text file of domains, and return the API response.
	"""
	with open("domains.txt") as f:
		domains = [x.strip() for x in f.readlines()]
	for y in domains:
		check(y)	
genDomains()