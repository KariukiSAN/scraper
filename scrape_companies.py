from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from companies import Company


def scrape_companies():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("table")[1]
    rows = table.find_all('tr')[1:]  # Exclude header row

    engine = create_engine('sqlite:///companies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    companies = []
    for row in rows:
        data = row.find_all('td')
        rank = int(data[0].text.strip())
        name = data[1].text.strip()
        industry = data[2].text.strip()
        revenue = data[3].text.strip()
        revenue_growth = data[4].text.strip()
        employees = data[5].text.strip()
        headquarters = data[6].text.strip()

        company = Company(rank=rank, name=name, industry=industry, revenue=revenue,
                          revenue_growth=revenue_growth, employees=employees, headquarters=headquarters)
        session.merge(company)
        companies.append(company)

    session.commit()
    session.close()

    return companies