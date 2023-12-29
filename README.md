# password-checker
'![Local Image](images/privacy.jpg)'

This script checks if passwords provided in a file have been compromised using the Pwned Passwords API. It hashes the passwords and queries the API to find if the hash exists in the list of compromised passwords.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/password-checker.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd password-checker
    ```

3. **Run the script by providing the path to a file containing passwords:**

    ```bash
    python script.py path/to/passwords.txt
    ```

    Replace `path/to/passwords.txt` with the actual path to your file containing passwords.

## Requirements

- Python 3.x
- Requests library (install using `pip install requests`)

## How it Works

1. The script reads passwords from the provided file.
2. It hashes each password using SHA-1.
3. The first five characters of the hash are sent to the Pwned Passwords API.
4. The API responds with a list of hash suffixes and their counts.
5. The script checks if the hash suffix of the given password is present in the response.
6. If found, it indicates that the password has been compromised.

## Example

Assuming the file `passwords.txt` contains:

password123
securepassword

## Running the script:

python script.py passwords.txt

## The output might be:

password123 was found 123456 times... change password
securepassword was not found, carry on

---

## Note

- Make sure to keep your password files secure.
- If a password is found in breaches, consider changing it to a more secure one.
