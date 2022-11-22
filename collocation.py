import http.client

def get_callocation(word):
    html_text = "<html></html>"
    connection = http.client.HTTPSConnection("ozdic.com")
    connection.request("GET", f"/collocation/{word.replace(' ','%20')}.txt")
    response = connection.getresponse()
    if response.status == 200:
        html_text = response.read().decode()
    return html_text

if __name__ == '__main__':
    get_callocation("fish")