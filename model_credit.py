import urllib3, requests, json

apikey = "0PbEP-YxORfrEEXNReBwsW4ZTI2z-VEKYMOZbsB3V9bU"

url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]
#print(iam_token)
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': 'fb3bd6c8-67cb-470c-9bd9-ae990ae717c6'}

payload_scoring = {"input_data": [{"fields": ["account_check_status", "duration_in_month", "credit_history", "purpose", "credit_amount", "savings", "present_emp_since", "installment_as_income_perc", "personal_status_sex", "other_debtors", "present_res_since", "property", "age", "other_installment_plans", "housing", "credits_this_bank", "job", "people_under_maintenance", "telephone", "foreign_worker"], "values": [["0_to_200",31,"credits_paid_to_date","other",1889 ,"100_to_500","less_1",3,"female","none",3,"savings_insurance",32,"none" ,"own",1,"skilled",1,"none","yes"]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/52e3f0a9-f95a-44fa-9af8-b5a589085321/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))