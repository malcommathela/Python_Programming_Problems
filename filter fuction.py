friends = [("jreher",20),
           ("hfbefje",19),
           ("fecejrk",17),
           ("khffue",18),
           ("vfgdhdu",21),
           ("asurtbf",16)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)