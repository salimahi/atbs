import re
dashPhone = re.compile(r'\d{3}-\d{3}-\d{4}')
areacodePhone = re.compile(r'(\d{3})-(\d{3}-\d{4})')
brackPhone = re.compile(r'\(\d{3}\)\d{3}-\d{4}')
plainPhone = re.compile(r'\d{10}')
dotPhone = re.compile(r'\d{3}\.\d{3}\.\d{4}')
lotsPhone = re.compile(r'.\d{3}.\d{3}.\d{4}')

def findPhoneNumber(text):
    print(dashPhone.findall(text))
    areacodesearch = areacodePhone.search(text)
    print(areacodesearch.group(1))
    print(brackPhone.findall(text))
    print(plainPhone.findall(text))
    print(dotPhone.findall(text))
    print(lotsPhone.findall(text))


message = "Here are all the numbers you can use to call me: 444-333-2222 or (433)332-5768 or 3214567890 or 412.345.6784"

findPhoneNumber(message)


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

note = "Batmobile is driven by Batman holy Batbat"

print(batRegex.findall(note))

### if you add a ()?  it will find that part of the string 0 or 1 time
### e.g. Bat(wo)?man - will find Batman or Batwoman
### or 0 or more than 1 time ()*
### e.g. Bat(wo)*man will find Batwowowoman
### ()+ will be at least 1 or more
### so Bat(wo)+man will find Batwoman or Batwowowomand
### {#} - allows you to find exact number of repetition where # = number
### {#,#} gives the range e.g. {3,5} will match 3 -5 but will find
### the most in the range. Unless you add a ?(e.g. {}? ) where it will match
### the shortest length 'non-greedy match'
### leaving out a number will be without a min or max

###.search finds the first time, .findall finds everything
###.findall will finds groups

### character classes \d is all digits 0 - 9
### \D any character that is NOT a numeric digit
### \w - letter, number or _ (underscore) \W any NON
### \s space, tab, newline \S anything that is NOT \s
