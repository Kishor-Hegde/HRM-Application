import urllib.request,json,threading

def fetch(link):
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        return data
    


def AuthenticateUser(username,password,callback=None):
    def get():
        data=fetch(f"https://cakehouse.co.in/hr-management/apis/main.php?username={username}&password={password}")
        if(callback):callback('status' in data.keys() and data['status'])
        print("hello")
    threading.Thread(target=get).start()
    