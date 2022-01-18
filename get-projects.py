import subprocess
import csv

# name of the output file
OUTPUT_FILE_NAME = 'projects.csv'

# bash command fetch all projects in GCP org and store into output variable
bashCommand = "gcloud projects list"# --format='csv(projectId, name, labels)'"
print(bashCommand)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

if type(output) == type(b''): output = output.decode('ascii')
output = output.split('\n')

with open(OUTPUT_FILE_NAME, 'w') as file:

    writer = csv.writer(file)

    for i in range(len(output)):
        writer.writerow([output[i]])
