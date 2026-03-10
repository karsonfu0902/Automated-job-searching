from jobscraper import JobScraper
from storage import Storage


if __name__ == "__main__":
    scraper = JobScraper("data analyst", "Toronto", 20, "fulltime", 168)
    scraper.scrape()
    scraper.col_filter()
    db = Storage()
    db.create_table()
    scraper.jobs.to_sql("jobs", db.conn, if_exists="replace", index=False)
