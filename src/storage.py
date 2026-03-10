import sqlite3

class Storage:
    def __init__(self, path = "jobs.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
    

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            job_url TEXT,
            title TEXT,
            company TEXT,
            location TEXT,
            job_level TEXT,
            description TEXT,
            company_url TEXT
        )
        ''')
        self.conn.commit()

    def save_jobs(self, jobs):
        self.cursor.executemany("""
            INSERT INTO jobs (id, job_url, title, company, location, job_level, description, company_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, jobs)
        self.conn.commit()
