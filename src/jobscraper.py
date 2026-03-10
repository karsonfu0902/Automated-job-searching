import csv
from jobspy import scrape_jobs
import pandas as pd


class JobScraper:
    def __init__(self, search_term, location, results_wanted=10, job_type="fulltime", hours_old=168):
        self.search_term = search_term
        self.location = location
        self.results_wanted = results_wanted
        self.job_type = job_type
        self.hours_old = hours_old
        self.jobs = None

    def scrape(self):
        jobs = scrape_jobs(
            site_name=["linkedin", "indeed", "glassdoor"],
            search_term=self.search_term,
            location=self.location,
            results_wanted=self.results_wanted,
            job_type=self.job_type,
            hours_old=self.hours_old,
            linkedin_fetch_description=True
        )

        self.jobs = jobs
        return

    def col_filter(self):
        self.jobs = self.jobs[[
            'id', 
            'job_url', 
            'title', 
            'company',
            'location', 
            'job_level', 
            'description', 
            'company_url'
            ]]


