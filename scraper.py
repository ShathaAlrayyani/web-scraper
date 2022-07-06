import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    citation = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    count = 0
    for citation in citation:
        count += 1
    # print(f'The number of citations needed in this page is {count}')
    return f'The number of citations needed for this page is {count}'



def get_citations_needed_report(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('a', text='citation needed')

    output = []
    for citation in citations:
        text = citation.find_parents('p')[0].text
        output.append(text)
    rep = '\n'.join(output)
    return rep.strip()



if __name__ == "__main__":
    print(get_citations_needed_report(url))
    print(get_citations_needed_count(url))
