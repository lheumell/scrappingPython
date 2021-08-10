import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    return (soup)


def job_data(soup):
    res = []
    for item in soup.findAll('h2', {'class': lambda x: x and 'jobTitle' in x.split()}):
        if item.get_text()[0:7] == 'nouveau':
            res.append(item.get_text()[7:])
        else:
            res.append(item.get_text())
    return (res)


def company_data(soup):
    res = []
    for item in soup.find_all("span", class_="companyName"):
        res.append(item.get_text())
    return (res)


def all_data(soup):
    res = []
    for item in soup.findAll('a', {'class': lambda x: x and 'fs-unmask' in x.split()}):
        res.append(item.get_text())
    return (res)


def url_data(soup):
    res = []
    for item in soup.findAll('a', {'class': lambda x: x and 'tapItem' in x.split()}):
        res.append(item['href'])
    return (res)


if __name__ == "__main__":


    url = "https://www.voyagespirates.fr/vols"

    soup = html_code(url)

    #job_res = job_data(soup)
    #com_res = company_data(soup)
    #all_res = all_data(soup)
    url_res = url_data(soup)

    temp = 0

    for i in range(0, len(url_res)):

        print("Url : " + url_res[i])

        print("-----------------------------")

    print("Nombre de resultats : " + str(len(url_res)))
