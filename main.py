import requests
from bs4 import BeautifulSoup
import csv

def exportToCSV(tab) :
    # field names
    fields = ['Name', 'Branch', 'Year', 'CGPA']

    # data rows of csv file
    rows = tab
    # name of csv file
    filename = "university_records.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)


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

    # Data for URL
    print("Enter your job:")
    job = input()
    lookAllJob = job.split(', ')
    print("Enter your location:")
    location = input()
    for job in lookAllJob:
        url = "https://fr.indeed.com/emplois?q=" + job + "&l=" + location + "&jt=apprenticeship"

        soup = html_code(url)

        job_res = job_data(soup)
        com_res = company_data(soup)
        all_res = all_data(soup)
        url_res = url_data(soup)

        temp = 0

        for i in range(0, len(job_res)):
            tabl = [job_res] + [com_res] + [url_res]
            exportToCSV(tabl)
            print(tabl)
            print("Company Name and Address : " + com_res[i])
            print("Job : " + job_res[i])
            print("Url : " + "https://fr.indeed.com" + url_res[i])
            print("All : " + all_res[i])
            print("-----------------------------")

        print("Nombre de resultats : " + str(len(job_res)))
