# import sys
#
# str1="PCPSCollege"
# print(str1)
# print(type(str1))
# print(id(str1))
# print(sys.getsizeof(str1))
# print(len(str1))
# print(min(str1))
# print(max(str1))
#
# print(str1[0])
# print(str1[5])
# print(str1[-3])#indexing
#
# print(str1[0:8])#slicing
#
# print(str1[1:9:2])
# print(str1)

# str2=str1[::-1]
# print(str2)
# print(id(str2))
# print(id(str1))
# print(str1.capitalize())
# print(id(str1.capitalize()))
# print(id(str1))
# # print(id(str2))
#
# print(str1.upper())
# print(id(str1.upper()))
# print(str1.lower())
# print(id(str1.upper()))

# str1="Admin"
# str2="ADMIN"
# if(str1==str2):
#     print("true")
# else:
#     print("false")
#
#
# if(str1.casefold()==str2.casefold()):
#     print("true")
# else:
#     print("false")
#
# print(str1.casefold())
# print(str2.casefold())
#


# str1="123456"
# str2=str1.ljust(20,"*")
# print(str2)
#
# str1="123456"
# str2=str1.center(20,"*")
# print(str2)
#
# str1="123456"
# str2=str1.rjust(20,"*")
# print(str2)


# str1="Kathmandu,Nepal"
# str2=str1.encode()
# print(str2)
#
# str2=str2.decode()
# print(str2)
# str1="How are you?"
# print(str1.endswith('?'))
#
# str1="SN\tNAME\tADDRESS"
# str2= str1.expandtabs(tabsize=20)
# print(str2)

# find
# str1="luffy is going to be pirates king"
# str2="o"
# result1=str1.find(str2,0,len(str1)-1)
# print(result1)
#
# result2=str1.find(str2,result1+1,len(str1)-1)
# print(result2)
#
# result3=str1.find(str2,result2+1,len(str1)-1)
# print(result3)
#
# # print(str1.count("o"))
# # result=-1
# # for i in range(str1.count("o")):
# #     result=str1.find(str2,result+1,len(str1)-1)
# #     print(result,ends=" ")
#
#
#
# strp='''essay, an analytic, interpretative, or critical literary composition usually much shorter and less systematic and formal than a dissertation or thesis and usually dealing with its subject from a limited and often personal point of view.
#
# Some early treatises—such as those of Cicero on the pleasantness of old age or on the art of “divination,” Seneca on anger or clemency, and Plutarch on the passing of oracles—presage to a certain degree the form and tone of the essay, but not until the late 16th century was the flexible and deliberately nonchalant and versatile form of the essay perfected by the French writer Michel de Montaigne. Choosing the name essai to emphasize that his compositions were attempts or endeavours, a groping toward the expression of his personal thoughts and experiences, Montaigne used the essay as a means of self-discovery. His Essais, published in their final form in 1588, are still considered among the finest of their kind. Later writers who most nearly recall the charm of Montaigne include, in England, Robert Burton, though his whimsicality is more erudite, Sir Thomas Browne, and Laurence Sterne, and in France, with more self-consciousness and pose, André Gide and Jean Cocteau.
#
# At the beginning of the 17th century, social manners, the cultivation of politeness, and the training of an accomplished gentleman became the theme of many essayists. This theme was first exploited by the Italian Baldassare Castiglione in his Il libro del cortegiano (1528; The Book of the Courtier). The influence of the essay and of genres allied to it, such as maxims, portraits, and sketches, proved second to none in molding the behavior of the cultured classes, first in Italy, then in France, and, through French influence, in most of Europe in the 17th century. Among those who pursued this theme was the 17th-century Spanish Jesuit Baltasar Gracián in his essays on the art of worldly wisdom.
#
# Keener political awareness in the 18th century, the age of Enlightenment, made the essay an all-important vehicle for the criticism of society and religion. Because of its flexibility, its brevity, and its potential both for ambiguity and for allusions to current events and conditions, it was an ideal tool for philosophical reformers. The Federalist Papers in America and the tracts of the French Revolutionaries are among the countless examples of attempts during this period to improve the human condition through the essay.
#
# The genre also became the favoured tool of traditionalists of the 18th and 19th centuries, such as Edmund Burke and Samuel Taylor Coleridge, who looked to the short, provocative essay as the most potent means of educating the masses. Essays such as Paul Elmer More’s long series of Shelburne Essays (published between 1904 and 1935), T.S. Eliot’s After Strange Gods (1934) and Notes Towards the Definition of Culture (1948), and others that attempted to reinterpret and redefine culture, established the genre as the most fitting to express the genteel tradition at odds with the democracy of the new world.
#
# Whereas in several countries the essay became the chosen vehicle of literary and social criticism, in other countries the genre became semipolitical, earnestly nationalistic, and often polemical, playful, or bitter. Essayists such as Robert Louis Stevenson and Willa Cather wrote with grace on several lighter subjects, and many writers—including Virginia Woolf, Edmund Wilson, and Charles du Bos—mastered the essay as a form of literary criticism.'''
# print(strp.count("o"))
# result=-1
# for i in range(strp.count("o")):
#     result=strp.find("the",result+1,len(strp)-1)
#     print(result,ends=" ")

# str1="NAME"
# str2="GAUREY DON"
# print("{}:{}".format(str1,str2))
# print("{0}:{1}".format(str1,str2))
# print("{}:{}".format(str1,str2))
# print("{}:{}".format(str1,str2))

# str1="PCPS COLLEGE"
# str2="e"
#
# print(str1.count(str2),"times")
# if(str1.count(str2)>0):
#     result=  str1.index(str2,0,len(str1)-1)
#     print(result)
# else:
#     print("{} Not Found".format(str2))
#
# str1="123abc"
# print(str1.isalnum())
# str1="@abc"
# print(str1.isascii())
# str1="aBc"
# print(str1.isalpha())
# str1="abc"
# print(str1.isdigit())
# str1="abc"
# print(str1.islower())
# str1="123.52"
# print(str1.isdecimal())
# str1="123abc"
# print(str1.isidentifier())
# str1="123abc"
# print(str1.isprintable())
# str1="123abc123"
# print(str1.isprintable())
# # print(help(str))
#
# list1=["raj","keshar","raju","sandesh","shrawan"]
# str1=":"
# print(str1.join(list1))

# str1=" PCPS "
# print(len(str1))
# str2=str1.lstrip()
# print(len(str2))
# print(str1)
# print(str2)

# str1=" PCPS   "
# print(len(str1))
# str2=str1.rstrip()
# print(len(str2))
# print(str1)
# print(str2)

# str1=" PCPS   "
# print(len(str1))
# str2=str1.strip()
# print(len(str2))
# print(str1)
# print(str2)

# str1="Partition the, string, into three parts using the given separator"
# str2=str1.partition(",")
# print(str2)
# print(type(str2))
#
# str1="*return a str with the given prefix string removed if present ?"
# str2=str1.removeprefix("*")
# print(str2)

# str1="*return a str with the given prefix string removed if present ?"
# str2=str1.removesuffix("?")
# print(str2)

# str1="*return a str with the given prefix string removed if present ?"
# str2=str1.replace("given","not given")
# print(str2)

# str1="the seperator used to split the string"
# str2=str1.split(sep=" ")
# print(str2)

# list1=["k","xa","kta","kti","ho"]
# str2=" "
# str3=str2.join(list1)
# print(str3)

# str1= "k\nxa\nkta\nkti\nho\nkhana\nkhayeu"
# str2=str1.splitlines()
# print(str2)

# str1="k xa mugi bacha haru"
# print(str1.endswith("haru"))

# str1="K ma Hancy haina RA"
# str2=str1.swapcase()
# print(str2)

str1="paara paAra🤘🤘 "
str2=str1.title()
print(str1)
print(str2)

str1="para"
str2=str1.upper()
print(str1)

str1="123"
str2=str1.zfill(20)
print(str2)