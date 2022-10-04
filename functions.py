def upperName(name):
  nameArray = name.split()
  fullname = ""
  for x in nameArray:
    fullname += x[:1].upper() + x[1:] + " "
  return fullname.strip()

def refundName(name):
  nameArray = name.split()
  fullname = ""
  for x in nameArray:
    if not x.isdigit():
     fullname += x[:1].upper() + x[1:] + " "
  return fullname.strip()