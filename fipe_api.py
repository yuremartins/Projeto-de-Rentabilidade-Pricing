import requests

def fipe_json(resource, data=None):
    url = "http://veiculos.fipe.org.br/api/veiculos"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Host": "veiculos.fipe.org.br",
        "Referer": "http://veiculos.fipe.org.br"
    }

    response = requests.post(f"{url}/{resource}", json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


