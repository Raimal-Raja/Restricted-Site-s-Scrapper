# Restricted-Site-s-Scrapper

## Description

This Python script is designed to scrape job listings from Indeed.com for multiple countries and job professions. It utilizes web scraping techniques to extract job information such as job title, company name, location, and job URL. The scraped data is then exported to a CSV file for further analysis.

## Features

- Scrapes job listings from Indeed.com for multiple countries
- Supports multiple job professions
- Exports results to a CSV file
- Implements error handling and logging
- Includes internet connectivity check
- Uses random delays to avoid overloading the server

## Requirements

- Python 3.6+
- cloudscraper
- beautifulsoup4
- pandas

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```bash
pip install cloudscraper beautifulsoup4 pandas
```

## Usage

1. Modify the `domains` dictionary in the `main()` function to include the desired countries and their corresponding Indeed.com URLs.
2. Adjust the `job_professions` list to include the job titles you want to search for.
3. Run the script:

```bash
python job_scraper.py
```

4. The results will be saved in a file named `Multi_Country_Job_results.csv` in the same directory as the script.

## Code Explanation

### Imports

```python
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import logging
import socket
```

These libraries are used for web scraping (cloudscraper, BeautifulSoup), data manipulation (pandas), timing and randomization (time, random), logging, and network connectivity checks (socket).

### Logging Configuration

The script sets up logging to both a file (`scraper.log`) and the console, which helps in debugging and monitoring the scraping process.

### Functions

1. `export(results)`: Exports the scraped data to a CSV file.
2. `internet_on()`: Checks if there's an active internet connection.
3. `scrape_job(base_url, job_search)`: The main scraping function that extracts job information from a given Indeed.com URL.
4. `main()`: The main function that orchestrates the scraping process for multiple countries and job professions.

### Scraping Process

1. The script iterates through each country and job profession.
2. For each combination, it constructs the appropriate URL and sends a request using cloudscraper.
3. The HTML response is parsed using BeautifulSoup to extract job information.
4. Extracted data is stored in a list of dictionaries.
5. The process includes error handling and logging for robustness.

### Data Export

The scraped data is exported to a CSV file named `Multi_Country_Job_results.csv` using pandas.

## Ethical Considerations

When using this scraper, please be mindful of the following:

1. Respect the website's `robots.txt` file and terms of service.
2. Implement appropriate delays between requests to avoid overloading the server.
3. Use the data responsibly and in compliance with relevant laws and regulations.

## Related Links and Sources

- [Cloudscraper Documentation](https://github.com/VeNoMouS/cloudscraper)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Indeed.com](https://www.indeed.com/)
- [Web Scraping Best Practices](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)

## Disclaimer

This script is for educational purposes only. Make sure to comply with Indeed.com's terms of service and implement appropriate rate limiting to avoid potential IP bans.

## License

This project is open-source and available under the MIT License.
