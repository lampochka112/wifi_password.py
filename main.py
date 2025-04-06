import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

profile = []
for i in data:
    if "All User Profile" in i:  
        profile.append(i.split(":")[1].strip())

for i in profile:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, "key=clear"]).decode('utf-8', errors="backslashreplace").split('\n')
        result = []

        for b in results:
            if "Key Content" in b:  
                result.append(b.split(":")[1].strip())  

        if result:
            print("{:<30} | {:<}".format(i, result[0]))
        else:
            print("{:<30} | {:<}".format(i, "No password set"))

    except subprocess.CalledProcessError:
        print("{:<30} | {:<}".format(i, "ERROR OCCURRED"))
     