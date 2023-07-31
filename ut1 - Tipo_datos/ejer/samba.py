samba_url = '//1.1.1.1/eoi/python'
samba_url = samba_url[2:]

slash_index = samba_url.index('/')
host = samba_url[:slash_index]
path = samba_url[slash_index:]

print(f"host={host}; path={path}")
