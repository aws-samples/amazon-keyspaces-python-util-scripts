class User:
    def __init__(self, **kwargs):
        self.username = kwargs["username"]
        self.name = kwargs["name"]
        self.email = kwargs["email"]
        self.address = kwargs["address"]
        self.birthdate = kwargs["birthdate"]

    def __repr__(self):
        return "User<{} -- {}>".format(self.username, self.name)
