import subprocess
from datetime import date
with open("links.txt", "r") as fd:
    lines = fd.read().splitlines()
todays_date = str(date.today())

subprocess.run("mkdir " + todays_date)
print('Downloading redump...')
for link in lines:
    linkr = link.replace('http://www.redump.org/', '')
    linkr = linkr.replace('/', '-')
    linkr += todays_date
    print(linkr)
    subprocess.run("wget -r -O ./" + todays_date + "/"+ linkr + ".zip " + link)
print('Zipping...')
subprocess.run("zip redump-" + todays_date + ".zip -r " + todays_date)
print('Zipping complete.')
print('Removing files...')
subprocess.run("rm -r " + todays_date)
print('Process complete.')