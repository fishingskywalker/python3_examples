
# create a list of characters using list comprehension
elem_list = [ elem for elem in "Earth Wind Water Fire" ]
print(elem_list)

# define a tuple of linux distributions
distros = ("Mint",
           "Ubuntu",
           "Debian",
           "Arch",
           "Slackware",
           "CentOS")

# create a list from the tuple using list comprehension
distro_list = [ distro for distro in distros ]
distro_list.sort()
print(distro_list)

