# We either use indexing[] or slice()
# [start:stop:step] but step is an option field it means jump this much charactors

name = "Sahil Rai"

firstName = name[0:5]
firstName = name [:5]
print(firstName)

lastName = name[6:]
print(lastName)

# Steps
funkyName = name[::2]
print(funkyName)

# reverse string using slicing
reversedName = name[::-1]
print(reversedName)

# Now comes the SLICING
website = "http://hello.world"
slice = slice(7, -6)
print(website[slice])