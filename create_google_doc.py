from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from datetime import datetime

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def create_google_doc(user_name, user_email):
    """Creates a Google Doc and returns the document URL."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # Here, we set the port to a fixed value (e.g., 8080)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Drive service
    service = build('drive', 'v3', credentials=creds)
    
    # Create a new Google Doc
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    doc_title = f"{now}_{user_name}_HCI_test_note"
    file_metadata = {
        'name': doc_title,
        'mimeType': 'application/vnd.google-apps.document'
    }
    doc = service.files().create(body=file_metadata).execute()
    
    # Get the document URL
    doc_url = f"https://docs.google.com/document/d/{doc['id']}/edit"
    
    return doc_url
