import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import logging
import socket

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()  # Print to console
    ]
)

def export(results):
    df = pd.DataFrame(results)
    df.to_csv("Multi_Country_Job_results.csv", mode="a", index=False, header=True)

def internet_on():
    try:
        # Try to connect to a well-known site
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def scrape_job(base_url, job_search):
    url = f"{base_url}jobs?q={job_search.replace(' ', '+')}&l="
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(url)
        bs = BeautifulSoup(response.text, "html.parser")
        job_list = bs.find('ul', {'class': 'css-zu9cdh'})
        
        if not job_list:
            logging.warning(f"No job list found for {job_search} at {base_url}")
            return []

        jobs = job_list.find_all('div', {'class': 'job_seen_beacon'})
        info = []

        for job in jobs:
            TITLE = job.find('h2', {'class': 'jobTitle'})
            if not TITLE:
                continue
            
            title = TITLE.text.strip()
            link = TITLE.find('a')
            if not link or 'data-jk' not in link.attrs:
                continue
            
            job_key = link.attrs['data-jk']
            job_url = f"{base_url}viewjob?jk={job_key}"
            
            company_name_elem = job.find('span', {'class': 'css-63koeb'})
            company_name = company_name_elem.text.strip() if company_name_elem else "N/A"
            
            company_location_elem = job.find('div', {'class': "company_location"})
            company_location = company_location_elem.text.strip() if company_location_elem else "N/A"
            
            data = {
                'title': title,
                'company name': company_name,
                'company location': company_location,
                'job url': job_url
            }
            info.append(data)
        
        logging.info(f"Scraped {len(info)} jobs for {job_search} at {base_url}")
        return info

    except Exception as e:
        logging.error(f"Error while scraping {url}: {e}")
        return []

def main():
    domains = {
        "United Kingdom": "https://www.indeed.co.uk/",
        "Pakistan": "https://pk.indeed.com/"
    }

    job_professions = [
        "DevOps developer",
        "Python developer"
    ]

    all_results = []

    for country, base_url in domains.items():
        for job in job_professions:
            if not internet_on():
                logging.error("Internet connection lost. Exiting.")
                return
            
            logging.info(f"Scraping {job} in {country}...")
            results = scrape_job(base_url, job)
            for result in results:
                result['country'] = country
                result['search_term'] = job
            all_results.extend(results)
            
            # Add a delay to avoid overloading the server
            time.sleep(random.uniform(3, 5))

    export(all_results)
    logging.info("Scraping completed. Results saved to Multi_Country_Job_results.csv")
    print("Scraping completed. Results saved to Multi_Country_Job_results.csv")

if __name__ == "__main__":
    main()
