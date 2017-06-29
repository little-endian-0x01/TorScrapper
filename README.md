# TorScrapper
A basic scrapper made in python with BeautifulSoup to - 

* Scrape Onion and normal links.
* Save the output in html format in Output folder.
* Filter the html output and strip out useful data only (Work in Progress).
* Striping out IOCs and other related data (On To-Do list).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python3 to run this project smoothly. Go to your terminal and execute the following command or visit [Python3](https://www.python.org/download/releases/3.0/) website.

```
[sudo] apt-get install python3 python3-dev
```

Furthermore install the requirements.txt using pip3 - 

```
[sudo] pip3 install -r requirements.txt
```

TL;DR: We recommend installing TorScrapper inside a virtual environment on all platforms.

Python packages can be installed either globally (a.k.a system wide), or in user-space. We do not recommend installing TorScrapper system wide.

Instead, we recommend that you install TorScrapper within a so-called “virtual environment” (virtualenv). Virtualenvs allow you to not conflict with already-installed Python system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).

To get started with virtual environments, see virtualenv installation instructions. To install it globally (having it globally installed actually helps here), it should be a matter of running:

```
[sudo] pip install virtualenv
```

### Deployment

A step by step series of examples that tells what you have to do to get this project running -

* Enter the project directory.
* Copy all the onion and normal links you want to scrape in _onions.txt_

```
[nano]/[vim]/[gedit]/[Your choice of editor] onions.txt
```

* Run TorScrapper.py using Python3

```
[sudo] python3 TorScrapper.py
```

* Check the scraped outputs in Output folder.


## Built With

* [Python](https://www.python.org/) - Python programming language.
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Beautiful Soup is a Python library for pulling data out of HTML and XML files.

## Contributing

If you want to contribute to this project, for some reason I won't understand, then you can create a pull request. Happy Coding!

## Versioning

Version 1.something Mehh...

## Authors

* **Shivam Kapoor** - An avid learner who likes to know every tiny detail in working of real life systems. Real enthusiast of cyber security and underlying networking concepts. (Email - kapoor.shivam88@gmail.com)

## License

Too lazy to decide on a License. zZzZ
