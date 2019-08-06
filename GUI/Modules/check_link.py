import link_parser

f = open("C:\\Users\\Simon\\Desktop\\domains.txt")
file = open("Data.txt", mode="w")

l = []
res = link_parser.parse_utype(f, l)
for value, threat in res:
    file.write("%s : %s\n" % (value, threat))

file.close()