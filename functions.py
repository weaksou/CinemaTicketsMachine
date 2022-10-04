def upperName(name):
  nameArray = name.split()
  fullname = ""
  for x in nameArray:
    fullname += x[:1].upper() + x[1:] + " "
  return fullname.strip()