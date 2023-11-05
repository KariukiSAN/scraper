# Project-Scraper
The following project is related to web scraping and storing information about the largest companies in the United States by revenue. This project provides a way to gather and store information about the companies. It is useful in the following areas:
-It allows market researchers to gather up to date data on the largest companies.
-It allowed businesses and investors to gain insight into market dynamics which is beneficial for identification of potential partnership opportunities.


# Main features of the project
-Web Scraping: The project utilizes the BeautifulSoup library to scrape data from a Wikipedia page. 

-Database Storage: The SQLAlchemy ORM is used to store the scraped data in a SQLite database. 

-Composite Key: The project demonstrates the use of a composite primary key in the Company model. 

-Data Retrieval and Display: The main.py module allows for the retrieval of the stored company data from the database. It calls the scraping function, fetches the company information, and displays it by printing the details of each company object.

# Libraries used for this project
BeautifulSoup: Used the BeautifulSoup library, specifically BeautifulSoup4 (bs4), for web scraping. 

SQLAlchemy: SQLAlchemy for Object-Relational Mapping (ORM) library allowing for interaction with databases using Python objects.

# Project Deliverables
Use OOP
Defined a company class to represent each company that is in the table. The class is essentially used to store the company data retrieved from the website. The scrape_companies function scrapes the data and creates company objects based on the scraped data.
Using OOP allows for the encapsulation of the data and logic making the code more organized.

Use of dicts, tuples and lists
LIsts: In the code, lists are used to store multiple company dictionaries therefore enabling storage and organization of multiple companies in a single data structure.
The code has an empty list called companies at the beginning of the scrape_companies function. 
Tuples: In this code, tuples represent each company as an ordered collection of attributes. The company_tuple tuple holds the attributes of the company in a specific order. The tuples are used to store the company attributes in a fixed and ordered manner.
Dictionaries: In this code, dictionaries are used to associate attribute names with their respective values for each company. The dictionary created is company_dict where the keys are the attribute names and the values are the corresponding attribute values.

One to many relationships
The one-to-many relationship is demonstrated using two entities ie the company entity and the scrape_companies function. 
The “company: entity represents the “one” side of the relationship because it represents a single company.
The scrape_companies function represents the “many” side of the relationship because it can create multiple instances of the company function.

Use ORM to interact with a database
Allows for a more convenient and intuitive way to interact with databases.
Using SQLAlchemy necessitates the need to define a model class that represents the database table. For this project, the company class is created in the companies.py file. This class inherits from the base class provided by SQLAlchemy’s declarative_base()function.
Defining the company class in this way allows SQLAlchemy to automatically create a mapping between the class and the corresponding database table.

Create a table with a composite key.
The composite key is added to our company model. The primary key is composed of multiple columns. The composite primary key in this case is using the rank and name columns. Meaning that the combinations of the rank and name values must be unique for each row in the table.

