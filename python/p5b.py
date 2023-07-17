# b) Develop a python program that could search the text in a file for phone numbers(+919900889977)

# and email addresses (sample@gmail.com)

import re
phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')
with open('example.txt', 'r') as f:
        for line in f:
                matches = phone_regex.findall(line)
                for match in matches:
                        print(match)

                matches = email_regex.findall(line)
                for match in matches:
                        print(match)


# OUTPUT:
# tomcat@gmail.com
# jerrymouse@gmail.com
# spikethedog@gmail.com
# +919986059013
# +918310681568