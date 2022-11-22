import re
link = "https://www.bls.gov/regions/west/arizona.htm"
if "_msa" not in link:
  type = "state"
  pattern = "(regions\/.*\/)(.*)(.htm)"
  location = re.split(pattern=pattern, string=link)[2]
print(type, location)