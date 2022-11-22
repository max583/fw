import requests

def_rapid_key = "3623bee911msh93ad8449311d407p18d408jsnd1c153180d0a"

def rapid_translate(word, rapid_key=def_rapid_key):

    if rapid_key == '':
        rapid_key = def_rapid_key
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to[0]":"ru","api-version":"3.0","from":"en","profanityAction":"NoAction","textType":"plain"}
    payload = [{"Text": f"{word}"}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": f"{rapid_key}",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }

    result = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    if result.status_code == 200:
        return result.json()[0]['translations'][0]['text']
    else:
        return f"You may need to specify a rapid access key. See readme.rst file. Access error: {result.reason} {result.status_code}"

if __name__ == '__main__':
    print(rapid_translate("Double trouble"))