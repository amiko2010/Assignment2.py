
import re

text = "ჩვენი გუნდის წევრები არიან: saba.ananidze@itstep.com, მეგობარი დიმა dima123@gmail.com და test_user@yahoo.com"

emails = re.findall(r'\S+@\S+', text)

result = "+".join(emails)

