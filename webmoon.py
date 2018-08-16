import urllib3
import colorama
from colorama import *
import socket

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()

def parse_wordlist(path):
    wordlist = open(path, 'r+')
    word_list_py = []
    for i in wordlist:
        word_list_py.append(i.rstrip())
    return word_list_py

def main(url, wordlist_path = "N:\\Tools\\webmoon\\rockyou.txt"):
        fucker = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'identity',
            'Keep-Alive': '300',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }
        black_list = []
        listt = parse_wordlist(wordlist_path)
        print("Operation Starting Boss..............")
        for i in listt:
            try:
                new_url = "https://" + str(i).rstrip() + "." + url
                http = urllib3.PoolManager()
                # print('Sent:', new_url)
                r = http.request('POST', new_url, headers=fucker)
                if r.status >= 200 and r.status < 300:
                    color_status = Fore.GREEN
                else:
                    color_status = Fore.RED
                if new_url not in black_list:
                    print(Fore.BLUE + "URL: " + Fore.RED + new_url + Fore.BLUE + " | IP: " + Fore.RED+socket.gethostbyname(new_url.split("://")[1]) + Fore.BLUE +" | Response: " + color_status + str(r.status))
                    black_list.append(new_url)
            except urllib3.exceptions.MaxRetryError:
                # print(r.status)
                pass
            except UnicodeError:
                pass
            except urllib3.exceptions.ProtocolError:
            	pass
            except KeyboardInterrupt:
            	with open('report.txt', 'w') as file:
            		for i in black_list:
            			file.write(i+'\n')


def validateUrl(url):
    domain_extensions = ['com', 'ge', 'io', 'de', 'ru']
    try:
        if url.split(".")[1] not in domain_extensions:
            print("URL Extension Doesn't Seem To Be Valid")
            url = input("Please Enter Valid The URL: ")
            validateUrl(url)
    except IndexError:
        print("You Entered URL Without Extension")
        url = input("Please Enter Valid The URL: ")
        validateUrl(url)
    return url


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='DNS Scanner To Get Subdomains of Website')
    # parser.add_argument('-u', '--url', help="URL To Scan")
    # # parser.add_argument('-w', '--wordlist', help="Import Your Wordlist")
    # args = parser.parse_args()
    # # print(args)
    # # exit()
    # if not args.url:
    #     print("\nPlease Specify The Url And Start The Program Again!")
    #     print("Use -h for Help")
    #     sys.exit(-1)
    # # elif args.wordlist:
    # #     main(url=args.url, word_list=args.wordlist)
    # else:
    #     main(url=args.url)
    print(Fore.BLUE + '''
 ▄█     █▄     ▄████████ ▀█████████▄    ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄██████▄  ███▄▄▄▄   
███     ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███    ███ ███▀▀▀██▄ 
███     ███   ███    █▀    ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███ 
███     ███  ▄███▄▄▄      ▄███▄▄▄██▀  ███   ███   ███ ███    ███ ███    ███ ███   ███ 
███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ███   ███   ███ ███    ███ ███    ███ ███   ███ 
███     ███   ███    █▄    ███    ██▄ ███   ███   ███ ███    ███ ███    ███ ███   ███ 
███ ▄█▄ ███   ███    ███   ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███ 
 ▀███▀███▀    ██████████ ▄█████████▀   ▀█   ███   █▀   ▀██████▀   ▀██████▀   ▀█   █▀ 
    ''')
    url = input("Please Enter The URL: ")
    main(validateUrl(url))