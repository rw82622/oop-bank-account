class Owner:
    list_of_all_owners = []
    def __init__(self, owner_id, l_name, f_name, st_address, city, state):
        self.id = owner_id
        self.l_name = l_name
        self.f_name = f_name
        self.st_address = st_address
        self.city = city
        self.state = state
        Owner.list_of_all_owners.append(self)
        
    @classmethod
    def all_owners(self):
        return Owner.list_of_all_owners
        