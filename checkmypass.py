import requests
import hashlib
import sys

def requests_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f'Error fetching: {res.status_code}, check API and try again')
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

def pwn_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = requests_api_data(first5_char)
	return get_password_leaks_count(response, tail)

def main(file_path):
	with open(file_path, 'r') as file:
		passwords = file.read().splitlines()

	for password in passwords:
		count = pwn_api_check(password)
		if count:
			print(f'{password} was found the {count} times... change password')
		else:
			print(f'{password} was not found, carry on')

	return 'done!'

if __name__ == '__main__':
	file_path = sys.argv[1]
	main(file_path)