import json
import os


def parse_record(line):
    record = line.strip().split("|")
    entry_id = int(record[0])
    date = record[1]
    time = record[2]
    elapsed_time = record[3]
    object = record[4]
    path = record[5]

    return {
        "entry_id": entry_id,
        "date": date,
        "time": time,
        "elapsed_time": elapsed_time,
        "object": object,
        "path": path,
    }

def convert_to_json(file_path):
    records = {}
    with open(file_path, 'r') as file:
        for line in file:
            record = parse_record(line)
            entry_id = record.pop('entry_id', None)  # Remove entry_id from the record
            records[entry_id] = record  # Use entry_id as key
    return records



def process_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
    # Exclude root folder file
        if not root == folder_path:
            for filename in files:
                if filename.endswith(".txt"):
                    file_path = os.path.join(root, filename)
                    print(f"Processing file: {file_path}")
                    json_data = convert_to_json(file_path)
                    json_output_path = os.path.splitext(file_path)[0] + ".json"
                    with open(json_output_path, "w") as json_file:
                        json.dump(json_data, json_file, indent=2)
                    print(f"Conversion successful for {filename}. JSON file created.")


if __name__ == "__main__":
    folder_path = "/home/rudito/Code/WUIL Logs/WUIL Logs/"
    process_files_in_folder(folder_path)

