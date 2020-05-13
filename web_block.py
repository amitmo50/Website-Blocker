import time
from datetime import datetime
global host_path
host_path = "/etc/hosts"

class WebsiteBlocker:
    def __init__(self):
        self.redirect = "127.0.0.1"
        self.website_block_list = []

    def blocking(self):

        while True:
            # time of your work
            if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8)< datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16):
                print("Working hours...")
                with open(host_path, 'r+') as file:
                    content = file.read()
                    for website in self.website_block_list:
                        if website in content:
                            pass
                        else:
                            # mapping hostnames to your localhost IP address
                            file.write(self.redirect + " " + website + "\n")
            else:
                with open(host_path, 'r+') as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                            # removing hostnmes from host file
                    file.truncate()

                print("Fun hours...")
            time.sleep(5)




