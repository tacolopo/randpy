import os
import requests

# Create a folder called "sn" on the desktop if it doesn't exist
folder_path = os.path.expanduser("~/Desktop/sn")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loop through PDFs from 967 to 1 in descending order
for i in range(967, 0, -1):
    if i > 99:
    
        url = f"https://www.grc.com/sn/sn-{i}.pdf"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(os.path.join(folder_path, f"sn-{i}.pdf"), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded sn-{i}.pdf")
        else:
            print(f"Failed to download sn-{i}.pdf")

    elif i > 9: 
        url = f"https://www.grc.com/sn/sn-0{i}.pdf"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(os.path.join(folder_path, f"sn-{i}.pdf"), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded sn-{i}.pdf")
        else:
            print(f"Failed to download sn-{i}.pdf")
    else: 
        url = f"https://www.grc.com/sn/sn-00{i}.pdf"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(os.path.join(folder_path, f"sn-{i}.pdf"), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded sn-{i}.pdf")
        else:
            print(f"Failed to download sn-{i}.pdf")
    
