from bs4 import BeautifulSoup
import requests
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('sheet 1')
sheet1.write(0,0,'NAMES')
sheet1.write(0,1,'LINKS')
sheet1.col(0).width = 10000
sheet1.col(1).width = 25000

page=requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')  #creating BeautifulSoup object

# avoiding extra links
last_links = soup.find(class_='AlphaNav')  # we got this class from the html code of the site that was at last of BodyText
last_links.decompose()

table = soup.find(class_='BodyText')   # getting text from the BodyText div



name = table.find_all('a')    # Pull text from all instances of <a> tag within BodyText div
count =0
for artist in name:
    count=count+1      #getting count of number of url
    #print(artist.prettify)  # pritning names of all artists along with links
    names = artist.contents[0]
    #print(names)            # printing only names of artists
    links='https://web.archive.org' + artist.get('href')     # getting all the links related to particular artists (we can't use find here as it's not BeautifulSoup)
    #print(links)
    sheet1.write(count,0,names)
    sheet1.write(count,1,links)

wb.save('artists names.xls')










