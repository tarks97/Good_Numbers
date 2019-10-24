from time import sleep
from file_manipulation import Reader
from mobileLebra import mobileLebara
from prekoUrl import getOister
from telmorePrekoUrl import getTelmore


def main():
    
    
    getOister()
    getTelmore()
    URLS = Reader("urls.txt")
    for url in URLS:
        if "mobile.lebara" in str(url):
             mobileLebara(url)
        
            
if __name__ == "__main__":
    while True:
        main()
        sleep(5)


    
