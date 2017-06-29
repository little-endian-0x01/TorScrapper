#Author - Shivam Kapoor (ConanKapoor)

#Importing Essentials
from multiprocessing import Pool
import os

#Opening onions directory. To scrape links add the same in onions.txt
with open("onions.txt", "r") as onion:
    content = onion.read().splitlines()

#Terminal Process (Only for Gnome at the moment).
def Execute(url):
    execute = str('gnome-terminal -e \' python3 Scrape.py ' + url + '\'')
    os.system(execute)

#MultiPrcessing Implementation (Limit - 5 proesses at a time).
if __name__ == '__main__':
    with Pool(processes=5) as pool:
        for onion in range(0, len(content)):
            pool.apply(Execute, args=(content[onion],))