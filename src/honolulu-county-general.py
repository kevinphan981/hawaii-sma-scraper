'''
    I was dumb and forgot that we're looking for SMAs and not just regular permit data
'''

import requests
from bs4 import BeautifulSoup

cookies = {
    'SessionId': 'VISpbUkMTGFLNNmeBEYbnktEBJJrvlmldjSOpnyT',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://dppweb.honolulu.gov',
    'Pragma': 'no-cache',
    'Referer': 'https://dppweb.honolulu.gov/DPPWeb/Default.aspx?PossePresentation=BuildingPermitSearch',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'SessionId=VISpbUkMTGFLNNmeBEYbnktEBJJrvlmldjSOpnyT',
}

params = {
    'PossePresentation': 'BuildingPermitSearch',
}

# data = {
#     'currentpaneid': '713870',
#     'paneid': '713869',
#     'functiondef': '5',
#     'sortcolumns': '{}',
#     'datachanges': "'j0BIYqkh1gWN8XD8bXTt%2BZ5L89tAj189n2CWIhV2rF1sCc17mFeV2NTyApwSGtGXcShQR1a6JywjlQaiSWzudN%2B50q8RDSrq13fb9IYCPCEqWLjvRs%2Bywc0bpXkBQlXMNJ/ewZ4AnMfcFq/2uVm%2BORGeyVFBsBrQuLUm7nVh3v4uApNDrWxXQaRMZMx/1/ruUCKidaF701fVAclGgmBbXV%2BrnmkUCzpdWAOk5AYSHUu/5OPm1Vv4IWbYwaux%2B921S217I0V%2BImo8bjczSGo%2BWA%3D%3D',('C','S0',664452,'2023-01-01 00:00:00'),('C','S0',664453,'2023-01-10 00:00:00'),('F','ext-gen1009',0,460),('F','ext-gen1009',0,460)",
#     'comesfrom': 'posse',
#     'changesxml': '',
# }

#date formatting: 2023-01-10

def create_data(start_date, end_date):
    data = {
        'currentpaneid': '713870',
        'paneid': '713869',
        'functiondef': '5',
        'sortcolumns': '{}',
        'datachanges': (
            "'j0BIYqkh1gWN8XD8bXTt%2BZ5L89tAj189n2CWIhV2rF1sCc17mFeV2NTyApwSGtGXcShQR1a6JywjlQaiSWzudN%2B50q8RDSrq13fb9IYCPCEqWLjvRs%2Bywc0bpXkBQlXMNJ/"
            "ewZ4AnMfcFq/2uVm%2BORGeyVFBsBrQuLUm7nVh3v4uApNDrWxXQaRMZMx/1/ruUCKidaF701fVAclGgmBbXV%2BrnmkUCzpdWAOk5AYSHUu/5OPm1Vv4IWbYwaux%2B921S217I0V%2B"
            "Imo8bjczSGo%2BWA%3D%3D',"
            f"('C','S0',664452,'{start_date} 00:00:00'),"
            f"('C','S0',664453,'{end_date} 00:00:00'),"
            "('F','ext-gen1009',0,460),('F','ext-gen1009',0,460)"
        ),
        'comesfrom': 'posse',
        'changesxml': '',
    }
    return data

# declare some vars
start_date = '2023-01-10'
end_date = '2023-01-11'
response = requests.get(
    'https://dppweb.honolulu.gov/DPPWeb/Default.aspx',
    params=params,
    cookies=cookies,
    headers=headers,
    data=create_data(start_date = start_date, end_date = end_date),
)

import pandas as pd
# global vars
full_data = []

if response.status_code == 200:
    print("Success!")

    # Check what type of content we got
    print(f"Content-Type: {response.headers.get('content-type', 'unknown')}")
    print(f"Content length: {len(response.content)} bytes")

    # Output is a bunch of html, must use bs4
    data = response.text 

    # parse html with beautifulsoup
    soup = BeautifulSoup(data, 'html.parser')
    
    #test print first 6k chars to see
    # print(soup.prettify()[:6000]) 

    # we look for tables
    tables = soup.find_all('table')
    print(f"Found {len(tables)} tables")

    for i, table in enumerate(tables):
        rows = table.find_all('tr')
        print(f"\nTable {i+1} has {len(rows)} rows")
        if rows:
            print("First row:", rows[0].get_text(strip=True)[:200])


    # based on the data, it is the second table that has the data we want.
    main_table = soup.find_all('table')[1]  # Adjust index as needed

    #retrieves all rows
    rows = main_table.find_all('tr')
    # for row in rows[1:]:  # Skip header
    #     cols = row.find_all(['td', 'th'])
    #     row_data = [col.get_text(strip=True) for col in cols]
    #     if row_data:  # Only non-empty rows
    #         data.append(row_data)
    # print("Extracted data:", data[:3])  # First 3 rows

    for i, row in enumerate(rows):
        print(f"Row {i}: {row.get_text(strip=True)}")
        cols = row.find_all(['td', 'th'])
        row_data = [col.get_text(strip=True) for col in cols]
        if row_data:  # Only non-empty rows
            full_data.append(row_data)
    print("Extracted data:", full_data[:3])  # First 3 rows

else: 
    print(f"Failed with Status Code: {response.status_code}")
    print(f"Server message: {response.text[:500]}") # Show first 500 chars of error

df = pd.DataFrame(full_data)
print(df.head())

import os
path = 'data'
if not os.path.exists(path):
    os.makedirs(path)

filename = f"honolulu-county-{start_date}-{end_date}"
df.to_csv(f"{path}/{filename}.csv", index = False)
