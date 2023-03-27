import subprocess

file_name = "latest_id"
with open(file_name, 'r') as f:
    # Read the contents of the file
    latest_id = f.read()

# Open the output file in write mode
with open(file_name, 'w') as f:
    # Write the contents to the output file
    latest_id = int(latest_id)
    latest_id += 1
    subprocess.run("hexo new {file_name}".format(file_name=latest_id), shell=True)
    f.write(str(latest_id))
    print(latest_id)
