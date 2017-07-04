# Author - Shivam Kapoor (ConanKapoor)

# Importing Essentials
from multiprocessing import Pool
from pyfiglet import Figlet
import os

# Opening onions directory. To scrape links add the same in onions.txt
with open("onions.txt", "r") as onion:
    content = onion.read().splitlines()

# Terminal Process to edit Onions.txt using nano.(Only for Gnome at the moment).
def ExecuteEditor():
    execute = "nano onions.txt"
    os.system(execute)

# Terminal Process for Crawler (Only for Gnome at the moment).
def ExecuteCrawler(url):
    execute = str('gnome-terminal -e \' python3 Modules/Crawler/crawl.py ' + url + '\'')
    os.system(execute)

# Terminal Process for Scraper (Only for Gnome at the moment).
def ExecuteScraper(url):
    execute = str('gnome-terminal -e \'python3 Modules/Scraper/Scrape.py ' + url + '\'')
    print (execute)
    os.system(execute)

# Terminal Process for Scraping latest links. (Under Construction)
def ExecuteDiff():
    print ("\n------------> Work in progress. The developer is lazy af. <------------\n")

# MultiPrcessing Implementation (Limit - 5 processes at a time).
def Multiprocessing(task):
    if (os.path.exists("Output")):
        delete = str('rm -r Output')
        os.system(delete)
        os.makedirs("Output")
    else:
        os.makedirs("Output")

    with Pool(processes=5) as pool:
        for onion in range(0, len(content)):
            pool.apply(task, args=(content[onion],))

# Banner for the program.
def Banner():
    banner = Figlet(font='slant')
    print (banner.renderText('TorScraper'))
    print ("<---------WELCOME TO TORSCRAPER PROGRAM--------->")
    print ("<---------v1.0 - Author - Conan Kapoor--------->")
    print ("\n")

# Menu given to users. Eat away!
def Menu():
    print ("Please Select the mode of operation:- \n")
    print ("----> 1) Edit Onions.txt to add links.")
    print ("----> 2) Crawl given links :].")
    print ("----> 3) Scrape given links :].")
    print ("----> 4) Compare latest crawl and scrape the latest links.\n")

if __name__ == '__main__':
    try:
        Banner()
        Menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ExecuteEditor()
        elif choice == 2:
            Multiprocessing(ExecuteCrawler)
        elif choice == 3:
            Multiprocessing(ExecuteScraper)
        else:
            ExecuteDiff()

    except KeyboardInterrupt:
        print("Interrupt received! Exiting cleanly...")


