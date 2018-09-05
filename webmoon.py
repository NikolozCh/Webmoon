import webbrowser, urllib3, colorama, argparse, sys, socket
from colorama import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
colorama.init()


class SubDomain:

    def __init__(self, url, wordlist, ignored, browser):
        self.url = url
        self.browser = browser
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
                if r.status != int(self.ignored):
                    if new_url not in black_list:
                        print(Fore.BLUE + "URL: " + Fore.RED + new_url + Fore.BLUE + " | IP: " + Fore.RED + socket.gethostbyname(new_url.split("://")[1]) + Fore.BLUE + " | Response: " + color_status + str(r.status))
                        if self.browser:
                            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(new_url)
                        black_list.append(new_url)
            except urllib3.exceptions.MaxRetryError:
                pass
            except UnicodeError:
                pass
            except KeyboardInterrupt:
                print(Fore.RED + "\nUser Requested Exit, Quitting....s")
                sys.exit(0)
            except urllib3.exceptions.ProtocolError:
                pass
            except socket.gaierror:
                pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNS Scanner To Get Subdomains of Website')
    parser.add_argument('-u', '--url', required=True, help="URL To Scan")
    parser.add_argument('-w', '--wordlist', required=True, help="Select Wordlist")
    parser.add_argument('-i', '--ignore', help='Ignore The Responses By Statuscode')
    parser.add_argument('-b', '--browser', help='Pop Up Web Pages In Google Chrome (Working Only On Windows)', required=False, action='store_true')
    args = parser.parse_args()
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
    lets_do_this = SubDomain(url=args.url, wordlist=args.wordlist, ignored=args.ignore, browser=args.browser)
    try:
        lets_do_this.main()
    except FileNotFoundError:
        print("\nFile Input Error")
        sys.exit(0)