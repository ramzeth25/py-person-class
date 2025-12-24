class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        instance = Person.people[person.get("name")]
        if person.get("wife"):
            partner = Person.people.get(person.get("wife"))
            if partner:
                instance.wife = partner
        elif person.get("husband"):
            partner = Person.people.get(person.get("husband"))
            if partner:
                instance.husband = partner
    return instances
