import requests

def search_user(token, logon_name):
    url = f"http://brgsgt-manage.bumiresourcesgroup.com:8080/RestAPI/SearchUser?domainName=kpc.co.id&AuthToken={token}&range=1&startIndex=1&searchText={logon_name}"

    res = requests.get(url)
    print(res.text)