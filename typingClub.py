import random
alphabet="azertyuiopqsdfghjklm "
l=len(alphabet)
visible=""
for item in range(100):
	word=random.randrange(l)
	visible+=alphabet[word]

print(visible)
user=input("taper ce texte\n")
print(user)