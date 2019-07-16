from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbol = string.digits
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 6),
            lastname=random_string("lastname", 10), nickname='Вадик', address=random_string("address", 25),
            homephone=random_number("+", 11), mobilephone=random_number("+", 11), workphone=random_number("+", 11),
            secondaryphone=random_number("+", 2), email='1@mail.ru', email2='2@mail.ru', email3='3@mail.ru',
            homepage='www.mypage.ru')
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

