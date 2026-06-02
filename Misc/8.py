class person:
    name = "devansh"
    occupation = "Software Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation} with a net worth of {self.networth} million dollars.")

a = person()
a.name = "harry"
a.occupation = "Data Scientist"
a.info()

# print(a.name)    