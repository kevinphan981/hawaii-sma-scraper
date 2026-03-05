import requests
import pandas as pd
import json
import os

url = "https://hawaiicountyhi-energovpub.tylerhost.net/apps/selfservice/api/energov/search/search"

# huge shoutout to https://curlconverter.com/python/ for making my life easier
# Copy search response as cURL
cookies = {
    'Tyler-Tenant-Culture': 'en-US',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://hawaiicountyhi-energovpub.tylerhost.net',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://hawaiicountyhi-energovpub.tylerhost.net/Apps/SelfService',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'tenantid': '1',
    'tenantname': 'HawaiiCountyHIProd',
    'tyler-tenant-culture': 'en-US',
    'tyler-tenanturl': 'HawaiiCountyHIProd',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': 'Tyler-Tenant-Culture=en-US',
}

payload = {
    'Keyword': '',
    'ExactMatch': True,
    'SearchModule': 3,
    'FilterModule': 1,
    'SearchMainAddress': False,
    'PlanCriteria': {
        'PlanNumber': None,
        'PlanTypeId': '60514700-ce16-45a4-8c8a-bb7e6e46e33d_8c4a33c7-2e5d-4a30-b8a5-59459d349108',
        'PlanWorkclassId': None,
        'PlanStatusId': 'none',
        'ProjectName': None,
        'ApplyDateFrom': None,
        'ApplyDateTo': None,
        'ExpireDateFrom': None,
        'ExpireDateTo': None,
        'CompleteDateFrom': None,
        'CompleteDateTo': None,
        'Address': None,
        'Description': None,
        'SearchMainAddress': False,
        'ContactId': None,
        'ParcelNumber': None,
        'TypeId': None,
        'WorkClassIds': None,
        'ExcludeCases': None,
        'EnableDescriptionSearch': False,
        'PageNumber': 1,
        'PageSize': 10,
        'SortBy': 'relevance',
        'SortAscending': False,
    },
    'PermitCriteria': {
        'PermitNumber': None,
        'PermitTypeId': None,
        'PermitWorkclassId': None,
        'PermitStatusId': None,
        'ProjectName': None,
        'IssueDateFrom': None,
        'IssueDateTo': None,
        'Address': None,
        'Description': None,
        'ExpireDateFrom': None,
        'ExpireDateTo': None,
        'FinalDateFrom': None,
        'FinalDateTo': None,
        'ApplyDateFrom': None,
        'ApplyDateTo': None,
        'SearchMainAddress': False,
        'ContactId': None,
        'TypeId': None,
        'WorkClassIds': None,
        'ParcelNumber': None,
        'ExcludeCases': None,
        'EnableDescriptionSearch': False,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'InspectionCriteria': {
        'Keyword': None,
        'ExactMatch': False,
        'Complete': None,
        'InspectionNumber': None,
        'InspectionTypeId': None,
        'InspectionStatusId': None,
        'RequestDateFrom': None,
        'RequestDateTo': None,
        'ScheduleDateFrom': None,
        'ScheduleDateTo': None,
        'Address': None,
        'SearchMainAddress': False,
        'ContactId': None,
        'TypeId': [],
        'WorkClassIds': [],
        'ParcelNumber': None,
        'DisplayCodeInspections': False,
        'ExcludeCases': [],
        'ExcludeFilterModules': [],
        'HiddenInspectionTypeIDs': None,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'CodeCaseCriteria': {
        'CodeCaseNumber': None,
        'CodeCaseTypeId': None,
        'CodeCaseStatusId': None,
        'ProjectName': None,
        'OpenedDateFrom': None,
        'OpenedDateTo': None,
        'ClosedDateFrom': None,
        'ClosedDateTo': None,
        'Address': None,
        'ParcelNumber': None,
        'Description': None,
        'SearchMainAddress': False,
        'RequestId': None,
        'ExcludeCases': None,
        'ContactId': None,
        'EnableDescriptionSearch': False,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'RequestCriteria': {
        'RequestNumber': None,
        'RequestTypeId': None,
        'RequestStatusId': None,
        'ProjectName': None,
        'EnteredDateFrom': None,
        'EnteredDateTo': None,
        'DeadlineDateFrom': None,
        'DeadlineDateTo': None,
        'CompleteDateFrom': None,
        'CompleteDateTo': None,
        'Address': None,
        'ParcelNumber': None,
        'SearchMainAddress': False,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'BusinessLicenseCriteria': {
        'LicenseNumber': None,
        'LicenseTypeId': None,
        'LicenseClassId': None,
        'LicenseStatusId': None,
        'BusinessStatusId': None,
        'LicenseYear': None,
        'ApplicationDateFrom': None,
        'ApplicationDateTo': None,
        'IssueDateFrom': None,
        'IssueDateTo': None,
        'ExpirationDateFrom': None,
        'ExpirationDateTo': None,
        'SearchMainAddress': False,
        'CompanyTypeId': None,
        'CompanyName': None,
        'BusinessTypeId': None,
        'Description': None,
        'CompanyOpenedDateFrom': None,
        'CompanyOpenedDateTo': None,
        'CompanyClosedDateFrom': None,
        'CompanyClosedDateTo': None,
        'LastAuditDateFrom': None,
        'LastAuditDateTo': None,
        'ParcelNumber': None,
        'Address': None,
        'TaxID': None,
        'DBA': None,
        'ExcludeCases': None,
        'TypeId': None,
        'WorkClassIds': None,
        'ContactId': None,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'ProfessionalLicenseCriteria': {
        'LicenseNumber': None,
        'HolderFirstName': None,
        'HolderMiddleName': None,
        'HolderLastName': None,
        'HolderCompanyName': None,
        'LicenseTypeId': None,
        'LicenseClassId': None,
        'LicenseStatusId': None,
        'IssueDateFrom': None,
        'IssueDateTo': None,
        'ExpirationDateFrom': None,
        'ExpirationDateTo': None,
        'ApplicationDateFrom': None,
        'ApplicationDateTo': None,
        'Address': None,
        'MainParcel': None,
        'SearchMainAddress': False,
        'ExcludeCases': None,
        'TypeId': None,
        'WorkClassIds': None,
        'ContactId': None,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'LicenseCriteria': {
        'LicenseNumber': None,
        'LicenseTypeId': None,
        'LicenseClassId': None,
        'LicenseStatusId': None,
        'BusinessStatusId': None,
        'ApplicationDateFrom': None,
        'ApplicationDateTo': None,
        'IssueDateFrom': None,
        'IssueDateTo': None,
        'ExpirationDateFrom': None,
        'ExpirationDateTo': None,
        'SearchMainAddress': False,
        'CompanyTypeId': None,
        'CompanyName': None,
        'BusinessTypeId': None,
        'Description': None,
        'CompanyOpenedDateFrom': None,
        'CompanyOpenedDateTo': None,
        'CompanyClosedDateFrom': None,
        'CompanyClosedDateTo': None,
        'LastAuditDateFrom': None,
        'LastAuditDateTo': None,
        'ParcelNumber': None,
        'Address': None,
        'TaxID': None,
        'DBA': None,
        'ExcludeCases': None,
        'TypeId': None,
        'WorkClassIds': None,
        'ContactId': None,
        'HolderFirstName': None,
        'HolderMiddleName': None,
        'HolderLastName': None,
        'MainParcel': None,
        'EnableDescriptionSearchForBLicense': False,
        'EnableDescriptionSearchForPLicense': False,
        'EnableDescriptionSearchForOperationalPermit': False,
        'IsOperationalPermit': False,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'ProjectCriteria': {
        'ProjectNumber': None,
        'ProjectName': None,
        'Address': None,
        'ParcelNumber': None,
        'StartDateFrom': None,
        'StartDateTo': None,
        'ExpectedEndDateFrom': None,
        'ExpectedEndDateTo': None,
        'CompleteDateFrom': None,
        'CompleteDateTo': None,
        'Description': None,
        'SearchMainAddress': False,
        'ContactId': None,
        'TypeId': None,
        'ExcludeCases': None,
        'EnableDescriptionSearch': False,
        'PageNumber': 0,
        'PageSize': 0,
        'SortBy': None,
        'SortAscending': False,
    },
    'PlanSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'PlanNumber.keyword',
            'Value': 'Plan Number',
        },
        {
            'Key': 'ProjectName.keyword',
            'Value': 'Project',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
        {
            'Key': 'ApplyDate',
            'Value': 'Apply Date',
        },
    ],
    'PermitSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'PermitNumber.keyword',
            'Value': 'Permit Number',
        },
        {
            'Key': 'ProjectName.keyword',
            'Value': 'Project',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
        {
            'Key': 'IssueDate',
            'Value': 'Issued Date',
        },
        {
            'Key': 'FinalDate',
            'Value': 'Finalized Date',
        },
    ],
    'InspectionSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'InspectionNumber.keyword',
            'Value': 'Inspection Number',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
        {
            'Key': 'ScheduledDate',
            'Value': 'Schedule Date',
        },
        {
            'Key': 'RequestDate',
            'Value': 'Request Date',
        },
    ],
    'CodeCaseSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'CaseNumber.keyword',
            'Value': 'Code Case Number',
        },
        {
            'Key': 'ProjectName.keyword',
            'Value': 'Project',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
        {
            'Key': 'OpenedDate',
            'Value': 'Opened Date',
        },
        {
            'Key': 'ClosedDate',
            'Value': 'Closed Date',
        },
    ],
    'RequestSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'RequestNumber.keyword',
            'Value': 'Request Number',
        },
        {
            'Key': 'ProjectName.keyword',
            'Value': 'Project Name',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
        {
            'Key': 'EnteredDate',
            'Value': 'Date Entered',
        },
        {
            'Key': 'CompleteDate',
            'Value': 'Completion Date',
        },
    ],
    'LicenseSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'LicenseNumber.keyword',
            'Value': 'License Number',
        },
        {
            'Key': 'LicenseNumber.keyword',
            'Value': 'Operational Permit Number',
        },
        {
            'Key': 'CompanyName.keyword',
            'Value': 'Company Name',
        },
        {
            'Key': 'AppliedDate',
            'Value': 'Applied Date',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
    ],
    'ProjectSortList': [
        {
            'Key': 'relevance',
            'Value': 'Relevance',
        },
        {
            'Key': 'ProjectNumber.keyword',
            'Value': 'Project Number',
        },
        {
            'Key': 'ProjectName.keyword',
            'Value': 'Project Name',
        },
        {
            'Key': 'StartDate',
            'Value': 'Start Date',
        },
        {
            'Key': 'CompleteDate',
            'Value': 'Completed Date',
        },
        {
            'Key': 'ExpectedEndDate',
            'Value': 'Expected End Date',
        },
        {
            'Key': 'MainAddress',
            'Value': 'Address',
        },
    ],
    'ExcludeCases': None,
    'SortOrderList': [
        {
            'Key': True,
            'Value': 'Ascending',
        },
        {
            'Key': False,
            'Value': 'Descending',
        },
    ],
    'HiddenInspectionTypeIDs': None,
    "IsCitizenAccessCustomFieldSearch": False, # Add
    'PageNumber': 1,
    'PageSize': 10,
    'SortBy': 'relevance',
    'SortAscending': True,
}

all_results = []

# Arbitary time criteria
payload["PlanCriteria"]["ApplyDateFrom"] = "2020-01-01T00:00:00.000Z"
payload["PlanCriteria"]["ApplyDateTo"] = "2024-12-31T23:59:59.999Z"

#test for first five pages
for page in range(1,10):
    payload["PlanCriteria"]["PageNumber"] = page
    payload["PageNumber"] = page #global update
    response = requests.post(url, json = payload, headers = headers, cookies = cookies)

    if response.status_code == 200:
        print("wow!")
        data = response.json()
        print(data)
        
        if page == 0:
            print("Response keys: ", data.keys())
            print("Total results reported: ", data.get('TotalRows', 'Unknown'))


        results = data['Result'] # EnerGov usually puts results here
        if not results:
            print(f"Page {page} was empty, stopping")
            break # Stop if we hit an empty page
        all_results.extend(results)
        print(f"Grabbed page {page}")   
    else: 
        print(f"Failed with Status Code: {response.status_code}")
        print(f"Server message: {response.text[:5000]}") # Show first 500 chars of error
        break
        
    
print(f"Total records found: {len(all_results)}")   