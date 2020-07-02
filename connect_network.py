import requests
import time

def is_connected():
    url = 'https://www.baidu.com/'
    try:
        requests.get(url)
        return True
    except:
        return False
    

def log_in(username, password, output_file):
    url = 'http://210.34.48.49/eportal/InterFace.do'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    params = (
        ('method', 'login'),
    )
    data = {
        'userId': username,
        'password': password,
        'service': '',
        'queryString': 'wlanuserip=4168a23cb81c0c54de7c6943fcdf479c&wlanacname=3d1cd94ffbf7e4197e8fbd46a5584e53&ssid=&nasip=39ac2c6e007df760ae8b3f7f3b919dfe&snmpagentip=&mac=4e322ca419aeaaa5523942da438b26de&t=wireless-v2&url=709db9dc9ce334aa6363270493a5e6a6b1748319c9795b5e&apmac=&nasid=3d1cd94ffbf7e4197e8fbd46a5584e53&vid=1b33d3067b548968&port=2b0765f54b94f6f7&nasportid=5b9da5b08a53a54010ce97b909267f4e49b8dcf9acf28fa02ad8591e2fe4335e',
        'operatorPwd': '',
        'operatorUserId': '',
        'validcode': ''
    }
    try:
        response = requests.post(url=url, headers=headers, params=params, data=data)
        print(response.text, file=output_file)
    except requests.exceptions.RequestException as e:
        print(e)
    

if __name__ == '__main__':
    output_file = open('result.txt', 'w', encoding='utf-8')
    if not is_connected():
        output_file.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
        log_in('', '', output_file)
        output_file.close()
    else:
        output_file.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
        output_file.write('Everything is OK.\n')
        output_file.close()