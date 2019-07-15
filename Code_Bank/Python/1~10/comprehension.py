height = [158, 157, 163, 157, 145]

total = sum(height)
length = len(height)
ave = total / length

# for h in height:
#    variance += (ave - h)**2
#
# variance/=length

variance = sum([(h - ave) ** 2 for h in height]) / length
print(variance)
print([(h - ave) ** 2 for h in height])


#####################################
str_speeds = "38 42 20 49 39"
speeds = [int(s) for s in str_speeds.split(' ')]
print(speeds)

#####################################
speeds2 = "38 42 23 char 25 111"
speeds_ = [int(s) for s in speeds2.split(' ') if s.isdigit()]
print(speeds_)

######################################
tz = {"GMT": "+000", "BST": "+100",
      "EET": "+200", "JST": "+900"}

rev_tz = {sec: fir for fir, sec in tz.items()}
print(rev_tz)

######################################
names = {"BOB", "burton", "dave", "bob"}
unames = {s.lower() for s in names}

print(names)
print(unames)
