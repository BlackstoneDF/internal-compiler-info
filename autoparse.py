import requests

a: dict = requests.get("https://raw.githubusercontent.com/BlackstoneDF/internal-compiler-info/main/backend/action_dump.json").json()
t = ""
for b in a['actions']:
    c = "".join(b['codeblockName'].split())
    n = "".join(b['name'].split())
    s = f"{c}|{n}"
    if "arguments" in b['icon']:
        for r in b['icon']['arguments']:
            if "type" in list(r.keys()):
                q = "".join(r['type'].strip().replace("[","(").replace("]",")"))
                s = f"{s}|{q}"
    
    t = f"{t}{s.strip()}\n"

f = open("target.txt", "a")
f.write(t)
f.close()


