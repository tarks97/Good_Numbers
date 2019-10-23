from time import sleep
from file_manipulation import Reader
from mobileLebra import mobileLebara
from telmore import telmore
from oister import oister
from prekoUrl import getOister
from telmorePrekoUrl import getTelmore
from telenor import telenor
from apiCheck import func
from searchTelmore import telmoreSearch
def main():
    
    func()
    getOister()
    getTelmore()
    URLS = Reader("urls.txt")
    for url in URLS:
        if "mobile.lebara" in str(url):
            mobileLebara(url)
        elif "telmore" in str(url):
            telmoreSearch(url)
          
            
if __name__ == "__main__":
    while True:
        main()
        sleep(5)


    
