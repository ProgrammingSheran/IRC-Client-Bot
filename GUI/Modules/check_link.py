import link_parser

f = open("domains.txt")
file = open("Data.txt", mode="w")

l = []
res = link_parser.parse_utype(f, l)
counter = 0
for value, threat in res:
    file.write("%s --> %s : %s\n" % (counter, value, threat))
    counter += 1

file.close()
