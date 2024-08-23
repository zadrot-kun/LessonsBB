import requests

if __name__ == '__main__':
    r = requests.options('http://127.0.0.1:5007/')
    print(r.status_code, r.headers, r.text)

