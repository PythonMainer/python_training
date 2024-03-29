from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None,
                 nickname=None,  address=None, homephone=None, workphone=None, mobilephone=None,
                 secondaryphone=None, email=None, email2=None, email3=None, homepage=None,
                 all_phones_from_home_page=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize