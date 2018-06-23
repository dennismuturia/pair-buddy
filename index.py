import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Using the credentilas to enable user to interact with the Google API
scope = ['https://spreadsheets.google.com/feeds']
credds = ServiceAccountCredentials.from_json_keyfile_name('Pair buddy-06f8df1913fe.json', scope)
client = gspread.authorize(credds)

#Looking for the sheetfile and open it here
sheet = client.open("Peoples Name").sheet1
