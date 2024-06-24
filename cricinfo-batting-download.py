import requests
import time
import csv
from bs4 import BeautifulSoup

base_url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;orderby=start;page={};size=200;template=results;type=batting;view=innings'

# Function to scrape data from single page
def scrape_cricinfo(page_number):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
           'Connection': 'keep-alive'}

    url = base_url.format(page_number)

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Failed to retrieve page {page_number}')
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the specific caption
    table = None
    for tbl in soup.find_all('table', class_='engineTable'):
        caption = tbl.find('caption')
        if caption and caption.text.strip() == "Innings by innings list":
            table = tbl
            break

    if not table:
        print(f'No table with the correct caption found on page {page_number}')
        return None
    
    # Extract headers
    header_row = table.find('thead')
    if not header_row:
        print(f"No header row found on page {page_number}")
        return None
    
    csv_headers = [th.text.strip() for th in header_row.find_all('th') if th.text.strip()]

    rows = []
    body = table.find('tbody')
    if not body:
        print(f"No table body found on page {page_number}")
        return None
    
    for tr in body.find_all('tr'):
        cells = tr.find_all('td')
        row = [cell.text.strip() for cell in cells if cell.text.strip()]
        if row:  # Ensure not to include empty rows
            rows.append(row)
        
    return csv_headers, rows

def main():

    all_data = []
    headers = None

    for page in range(1, 300):

        print(f'Scraping Page {page}')

        result = scrape_cricinfo(page)

        if result:
            page_headers, page_data = result
            if headers is None:
                headers = page_headers
            all_data.extend(page_data)

        time.sleep(1)

    if headers:

        with open('cricinfo-batting-stats.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            writer.writerows(all_data)

        print('Scraping completed and data saved to cricinfo-batting-stats.csv')

if __name__ == "__main__":
    main()
