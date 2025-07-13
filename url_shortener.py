import random
import string

url_map = {}

def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def shorten_url(long_url):
    code = generate_code()
    url_map[code] = long_url
    return code

def expand_url(code):
    return url_map.get(code, "Short code not found.")

def main():
    while True:
        print("\n1. Shorten URL")
        print("2. Expand short code")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            long_url = input("Enter long URL: ")
            code = shorten_url(long_url)
            print("Short code:", code)
        elif choice == '2':
            code = input("Enter short code: ")
            print("Original URL:", expand_url(code))
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
