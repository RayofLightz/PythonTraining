import requests as r

def getEndpoint(endpoint):
    url = "http://127.0.0.1:5000" + endpoint
    res = r.get(url)
    print(res.text)

def main():
    getEndpoint("/")
    getEndpoint("/sayHi")
    getEndpoint("/goodbye")

if __name__ == "__main__":
    main()
