#Author - Shivam Kapoor (ConanKapoor)

#Importing Essentials
from multiprocessing import Pool
import os

#Opening onions directory. To scrape links add the same in onions.txt
with open("onions.txt", "r") as onion:
    content = onion.read().splitlines()

#Terminal Process (Only for Gnome at the moment).
def Execute(url):
    execute = str('gnome-terminal -e \' python3 Modules/Scraper/Scrape.py ' + url + '\'')
    os.system(execute)

#MultiPrcessing Implementation (Limit - 5 processes at a time).
if __name__ == '__main__':
    if (os.path.exists("Output")):
        delete = str('rm -r Output')
        os.system(delete)
        os.makedirs("Output")
    else:
        os.makedirs("Output")

    with Pool(processes=5) as pool:
        for onion in range(0, len(content)):
            pool.apply(Execute, args=(content[onion],))

