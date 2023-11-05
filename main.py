from scrape_companies import scrape_companies

def main():
    companies = scrape_companies()

    for company in companies:
        print(company)

if __name__ == '__main__':
    main()


    