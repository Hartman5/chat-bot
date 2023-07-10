import re
from curl_cffi import requests

session = requests.Session(impersonate="chrome101")

def host_session():
    headers = {
        'authority': 'heypi.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '__cf_bm=bswy1thrM_whuFa0AcysL12so86_WQ5D_5yjWxAthwc-1688943640-0-AYMjUJelRYzyK/LnrScQdDRGc5Y9sXDglB+2AO9g7zZneWzBzvl/qF40ZPz2e1eWLfXHdlkab60jMozHZeIeJ3U=; ai_user=N3SltgfkkRZwVLvOfj5PN5|2023-07-09T23:00:41.612Z',
        'origin': 'https://heypi.com',
        'referer': 'https://heypi.com/talk',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-api-version': '3',
    }

    session.post('https://heypi.com/api/chat/start', headers=headers)

    return;

def events():
    headers = {
        'authority': 'heypi.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'text/plain',
        # 'cookie': 'ai_user=DVdr1vBPXCrmH0FGFB5pdo|2023-07-09T19:45:57.257Z; __Host-session=87sKN1uvf4m7BgnWybqMj; __cf_bm=ReWiNzu0ZzAE2QIGiI2GAqssKStpWrMVolBAK.we05I-1688934229-0-Aa/YEBUcIqgPm+FRFW164g6gHwv2RLmFV4NjYiHDsjZy+Ni50mu+X7V0fL+1L3rveLBFdItXA3uis/cp3vEfSFY=',
        'origin': 'https://heypi.com',
        'referer': 'https://heypi.com/talk',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    data = '{"n":"curtain-raiser:started","u":"https://heypi.com/talk","d":"pi.ai","r":null}'

    session.post('https://heypi.com/proxy/api/event', headers=headers, data=data)

    data = '{"n":"pageview","u":"https://heypi.com/talk","d":"pi.ai","r":null}'

    session.post('https://heypi.com/proxy/api/event', headers=headers, data=data)

    data = '{"n":"curtain-raiser:completed","u":"https://heypi.com/talk","d":"pi.ai","r":null}'

    session.post('https://heypi.com/proxy/api/event', headers=headers, data=data)

    return;

def history():
    headers = {
        'authority': 'heypi.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': '__cf_bm=A3ZB8pncOOxAMp.F9ZI3gkFSWJF6AkV2PFi8ICfAJh8-1688931955-0-AQNEdLELAjUsJ20j0t8qOaYo0pC3tb+YtVXT7c6nuVBJAjneeTkoyHrMzgNXCVXVuPhdFFlilY+N3A+caCl9x8A=; ai_user=DVdr1vBPXCrmH0FGFB5pdo|2023-07-09T19:45:57.257Z; __Host-session=87sKN1uvf4m7BgnWybqMj',
        'if-none-match': '"6t5dqxvv2jt"',
        'referer': 'https://heypi.com/talk',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = session.get('https://heypi.com/api/chat/history', headers=headers).json()

    return response['messages'][0]['text']

def send_chat(message):
    headers = {
        'authority': 'heypi.com',
        'accept': 'text/event-stream',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '__cf_bm=A3ZB8pncOOxAMp.F9ZI3gkFSWJF6AkV2PFi8ICfAJh8-1688931955-0-AQNEdLELAjUsJ20j0t8qOaYo0pC3tb+YtVXT7c6nuVBJAjneeTkoyHrMzgNXCVXVuPhdFFlilY+N3A+caCl9x8A=; ai_user=DVdr1vBPXCrmH0FGFB5pdo|2023-07-09T19:45:57.257Z; __Host-session=87sKN1uvf4m7BgnWybqMj',
        'origin': 'https://heypi.com',
        'referer': 'https://heypi.com/talk',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-api-version': '3',
    }

    json_data = {
        'text': message,
    }

    response = session.post('https://heypi.com/api/chat', headers=headers, json=json_data).text

    partials = re.findall('data: {"text":"(.*?)"}', response)

    message = ''

    for partial in partials:
        message += partial

    return message

def main():
    host_session()
    events()
    message = history()
    print(message)
    while True:
        message = input('>>> ')
        if message == 'exit':
            break
        response = send_chat(message)
        print(response)

main()