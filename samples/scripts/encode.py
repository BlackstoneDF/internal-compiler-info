import base64
import gzip

input_string = input("Data: \n")

input_bytes = bytes(input_string, 'utf-8')

compressed_bytes = gzip.compress(input_bytes)

out = base64.b64encode(compressed_bytes)

out = out.decode()

print()

print(out + "\n")

print("""Give Command: give @p minecraft:ender_chest{PublicBukkitValues:{"hypercube:codetemplatedata":'{"author":"Joe","name":"None","version":1,"code":\"""" + out + """"}'},display:{Name:'{"extra":[{"text":"None"}],"text":""}'}}""")


input("Enter to continue...\n")