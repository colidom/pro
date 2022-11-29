org_date = "12/31/20"

splitted_date = org_date.split("/")
day = splitted_date[0]
month = splitted_date[1]
year = "20" + splitted_date[2]

new_format = "-".join([day, month, year])
print(new_format)
