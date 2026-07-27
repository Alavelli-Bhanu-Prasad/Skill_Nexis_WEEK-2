import json
fname = input("Enter JSON file name (with .json extension): ")
fname = fname.strip().strip('"').strip("'")
try:
    f = open(fname, "r")
    content = f.read() 
    f.close()
    data = json.loads(content) 
    print("\n----- Formatted JSON Output -----")
    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("\nError: File not found. Please check the file name/path.")

except json.JSONDecodeError as e:
    print("\nError: Invalid JSON format.")
    print("Details:", e)