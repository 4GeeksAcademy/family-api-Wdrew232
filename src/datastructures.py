class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 4  # Start at 4 since 3 predefined members
        self._members = [
            {"id": 1, "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "last_name": "Jackson", "age": 5, "lucky_numbers": [1]},
        ]

    def _generate_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_member(self, member):
        if "first_name" not in member or "age" not in member or "lucky_numbers" not in member:
            return None

        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member  


    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True, "id": id}
        return None

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
