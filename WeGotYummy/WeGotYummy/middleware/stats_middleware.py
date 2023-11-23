import os
import csv
from datetime import *

class StatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file_path = os.path.join(os.path.dirname(__file__), 'stats/request_logs.csv')

    def __call__(self, request):
        response = self.get_response(request)
        self.process_request(request)
        return response

    def process_request(self, request):
        # Log request statistics here
        # Extract information from the request like URL, IP, User-Agent, etc.
        url = request.path
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        # Log this information to a CSV file
        self.log_statistics(url, ip_address, user_agent)

    def log_statistics(self, url, ip_address, user_agent):
        # Write log to a CSV file
        fieldnames = ['URL', 'IP', 'User-Agent', 'Datetime']

        # Write to the CSV file
        with open(self.log_file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Check if the file is empty and write the header only if it's a new file
            if file.tell() == 0:
                writer.writeheader()
            
            writer.writerow({'URL': url, 'IP': ip_address, 'User-Agent': user_agent, 'Datetime': datetime.now().strftime('%d.%m.%y %H:%M:%S')})

    def log_error(request, errors):

        log_file_path = os.path.join(os.path.dirname(__file__), 'stats/error_logs.csv')

        url = request.path
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        fieldnames = ['URL', 'IP', 'User-Agent', 'Datetime', 'Errors']

        with open(log_file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Check if the file is empty and write the header only if it's a new file
            if file.tell() == 0:
                writer.writeheader()
            
            writer.writerow({'URL': url,
                              'IP': ip_address,
                                'User-Agent': user_agent, 
                                'Datetime': datetime.now().strftime('%d.%m.%y %H:%M:%S'),
                                'Errors': errors})