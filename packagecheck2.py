import sys
import requests

def check_package_existence(package_name):
    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    
    if response.status_code != 200:
        # Package does not exist
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py package_name")
        sys.exit(1)

    package_name = sys.argv[1]

    if check_package_existence(package_name):
        print(f"The package '{package_name}' exists on PyPI.")
    else:
        print(f"The package '{package_name}' does not exist on PyPI.")
        with open('non_existent_packages.txt', 'a') as file:
            file.write(f'{package_name}\n')
