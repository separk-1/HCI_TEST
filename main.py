from http.server import SimpleHTTPRequestHandler
import socketserver
import urllib.parse
import json
import os
import csv
from create_google_doc import create_google_doc
from datetime import datetime

PORT = 8000
DIRECTORY = "static"

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/create_doc':
            # Get the length of the data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            # Extract user details from the form data
            user_name = data.get('name', [''])[0]
            user_email = data.get('email', [''])[0]
            
            # Create a Google Doc for the user
            doc_url = create_google_doc(user_name, user_email)

            # Send a JSON response with the URL of the newly created Google Doc
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'doc_url': doc_url}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == '/save_results':
            # Get the length of the data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            # Check if 'timeline' and 'browsingHistory' are present in the data
            timeline_data = data.get('timeline', [''])[0]
            browsing_history_data = data.get('browsingHistory', [''])[0]

            # Verify if the data is not empty
            if not timeline_data or not browsing_history_data:
                # Send an error response if the data is missing
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'success': False, 'error': 'Invalid or missing data'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return

            try:
                # Parse the JSON data
                timeline = json.loads(timeline_data)
                browsing_history = json.loads(browsing_history_data)
            except json.JSONDecodeError:
                # Send an error response if JSON decoding fails
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'success': False, 'error': 'Failed to decode JSON'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return

            # Extract user details
            user_name = data.get('userName', [''])[0]
            user_email = data.get('userEmail', [''])[0]

            # Create a folder for the results if it doesn't exist
            results_dir = 'results'
            if not os.path.exists(results_dir):
                os.makedirs(results_dir)

            # Create a unique folder for each user
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            user_folder_name = f"{timestamp}_{user_name}"
            user_folder_path = os.path.join(results_dir, user_folder_name)
            os.makedirs(user_folder_path, exist_ok=True)

            # Save the timeline to a CSV file
            timeline_csv_path = os.path.join(user_folder_path, 'timeline.csv')
            with open(timeline_csv_path, 'w', newline='') as csvfile:
                fieldnames = ['task', 'startTime', 'endTime']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for entry in timeline:
                    writer.writerow(entry)

            # Save the browsing history to a CSV file
            browsing_csv_path = os.path.join(user_folder_path, 'browsing_history.csv')
            with open(browsing_csv_path, 'w', newline='') as csvfile:
                fieldnames = ['site', 'startTime', 'endTime']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for entry in browsing_history:
                    writer.writerow(entry)

            # Send a success response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'success': True}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        else:
            # For unsupported paths, send a 404 error response
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'error': 'Path not supported'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

# Change working directory to the project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Setup the HTTP server
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Open your browser and go to http://localhost:{PORT}/index.html")
    httpd.serve_forever()
