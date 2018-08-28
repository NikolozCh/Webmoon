import webbrowser
import urllib3
import colorama
from colorama import *
import socket
import argparse
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()


class SubDomain:

    def __init__(self, url, wordlist, ignored):
        self.url = url
        self.wordlist = wordlist
        self.ignored = ignored
        if ignored:
            self.ignored = ignored
        else:
            self.ignored = 0


    def main(self):
        if self.ignored != 0:
            print("Ignoring Response Code:", self.ignored, '\n')
        # exit()
        if len(self.url.split('://')[0]) > 5 or str(self.url.split('://')[0])[:4] != "http":
            print("\nCouldn't Resolve DNS")
            sys.exit(0)
        try:
            socket.gethostbyname(self.url.split('://')[1])
        except socket.gaierror:
            print("\nCouldn't Resolve DNS")
            sys.exit(0)
        http = urllib3.PoolManager()

        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'identity',
            'Keep-Alive': '300',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }

        black_list = list()
        for i in open(self.wordlist, 'r'):
            try:
                new_url = self.url.split("://")[0] + "://" + i.rstrip() + '.' + self.url.split("://")[1]
                r = http.request('GET', new_url, headers=headers)
                if r.status >= 200 and r.status < 300:
                    color_status = Fore.GREEN
                else:
                    color_status = Fore.RED
                # print(new_url, r.status)
                # print(r.status != int(self.ignored))
                # exit()
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(new_url)
                if r.status != int(self.ignored):
                    if new_url not in black_list:
                        print(Fore.BLUE + "URL: " + Fore.RED + new_url + Fore.BLUE + " | IP: " + Fore.RED + socket.gethostbyname(new_url.split("://")[1]) + Fore.BLUE + " | Response: " + color_status + str(r.status))
                        black_list.append(new_url)
            except urllib3.exceptions.MaxRetryError:
                pass
            except UnicodeError:
                pass
            except KeyboardInterrupt:
                print(Fore.RED + "\nQuiting...")
                sys.exit(0)
            except urllib3.exceptions.ProtocolError:
                pass
            except socket.gaierror:
                pass
            except FileNotFoundError:
                print("File Can Not Be Linked!")
                sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNS Scanner To Get Subdomains of Website')
    parser.add_argument('-u', '--url', help="URL To Scan")
    parser.add_argument('-w', '--wordlist', help="Select Wordlist")
    parser.add_argument('-i', '--ignore', help='Ignore The Responses By Statuscode')
    args = parser.parse_args()
    if not args.url:
        print("\nURL Input Error")
        sys.exit(0)
    if not args.wordlist or not args.wordlist.endswith(".txt"):
        print("\nWordlist Input Error")
        sys.exit(0)
    print(Fore.BLUE + '''
 ▄█     █▄     ▄████████ ▀█████████▄    ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄██████▄  ███▄▄▄▄
███     ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███    ███ ███▀▀▀██▄
███     ███   ███    █▀    ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███
███     ███  ▄███▄▄▄      ▄███▄▄▄██▀  ███   ███   ███ ███    ███ ███    ███ ███   ███
███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ███   ███   ███ ███    ███ ███    ███ ███   ███
███     ███   ███    █▄    ███    ██▄ ███   ███   ███ ███    ███ ███    ███ ███   ███
███ ▄█▄ ███   ███    ███   ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███
 ▀███▀███▀    ██████████ ▄█████████▀   ▀█   ███   █▀   ▀██████▀   ▀██████▀   ▀█   █▀

    ╔╗ ┬ ┬  ╔╗╔┬┌─┐┬┌─  ╔═╗┬ ┬┬┌┬┐┌─┐┌─┐┬ ┬┬  ┬┬┬  ┬
    ╠╩╗└┬┘  ║║║││  ├┴┐  ║  ├─┤│ │ ├─┤└─┐├─┤└┐┌┘││  │
    ╚═╝ ┴   ╝╚╝┴└─┘┴ ┴  ╚═╝┴ ┴┴ ┴ ┴ ┴└─┘┴ ┴ └┘ ┴┴─┘┴
    ''')
    lets_do_this = SubDomain(url=args.url, wordlist=args.wordlist, ignored=args.ignore)
    lets_do_this.main()