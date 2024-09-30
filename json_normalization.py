import json
from datetime import datetime
import os

def json_loader(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data
def time_parser(date_data, time_data):
    DateTimeData = date_data + " " + time_data
    DateTimeData = DateTimeData.replace('a.m.', 'AM').replace('p.m.', 'PM')
    date_format = "%d/%m/%Y %H:%M:%S %p"
    parsed_date = datetime.strptime(DateTimeData, date_format)
    unix_time = parsed_date.timestamp()
    return unix_time
def update_json_with_unix_time(data):
    for key, entry in data.items():
        unix_time = time_parser(entry["date"], entry["time"])
        entry["unix_time"] = unix_time
def json_updater(file_path):
    data = json_loader(file_path)
    update_json_with_unix_time(data)
    output_dir = os.path.dirname(file_path)
    output_file = os.path.join(output_dir, 'updated_log.json')
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
def process_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
    # Exclude root folder file
        if not root == folder_path:
            for filename in files:
                if filename.endswith(".json"):
                    file_path = os.path.join(root, filename)
                    json_updater(file_path)
if __name__ == "__main__":
    folder_path = "/home/rudito/Code/WUIL Logs/WUIL Logs/"
    process_files_in_folder(folder_path)