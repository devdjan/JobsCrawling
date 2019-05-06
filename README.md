# JobsCrawling
The project was create to parse data related to job (title, description, etc.) from sites:
* `https://www.hrforecast.de/company/career/` and  `https://www.gazpromvacancy.ru/jobs/`
And saving data to the Postgres database.

# Prerequisites
1. Installing `python3`
* Follow this [link](https://www.python.org/) and download the latest python3 OS X package
* Run the package and follow the steps to install `python3` on your computer.
* Once the installation is done, on your Terminal, run
`python3 --version`

2. Istall `pip` package
Securely download the `get-pip.py` file from this [link](https://pip.pypa.io/en/stable/installing/)
From the directory where the file was downloaded to, run the following command in the `Terminal`
`python3 get-pip.py`

3. Install `virtualenv` using pip
`pip3 install virtualenv`

4. Install DB. Follow this [link](https://postgresapp.com/) OR
`pip install postgres`

5. Setup the VirualEnviroment for the project
```virtualenv CrawlEnv
source crawlenv/bin/activate
```

# Dependencies
* Download Scrapy framework `pip install scrapy`
* Download the psycorp2 `pip install psycopg2-binary` 

# Running Spiders
To run spiders, just execute following commands in project directory:
```scrapy runspider hr_spider.py
scrapy runspider gazprom_spider.py
```
Or run bash script `crawling.sh`


# The Output data
Data you can find in database. Connect to db as manager:
`psql jobs_hrforecast manager`
Then check for tables:
`\dt`
Select all data from the table:
`SELECT * FROM jobs_data`






