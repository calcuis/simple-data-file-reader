import os, json, csv

def list_files():
    return [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(('.txt', '.csv', '.json'))]

def read_file(file_name):
    if file_name.endswith('.txt'):
        with open(file_name, 'r', encoding='utf-8') as f:
            print(f.read())
    elif file_name.endswith('.csv'):
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    elif file_name.endswith('.json'):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(json.dumps(data, indent=4))
    else:
        print("Unsupported file format.")

def main():
    files = list_files()
    if not files:
        print("No .txt, .csv, or .json files found in the current directory.")
        return
    
    print("Available files:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    try:
        choice = int(input("Select a file by number: ")) - 1
        if 0 <= choice < len(files):
            read_file(files[choice])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
