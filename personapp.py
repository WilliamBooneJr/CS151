from person import Person



#create person object

p = Person("Trish", "Olson", 25)
p2 = Person("John", "Doe", 30)
print(p, p2)
p.birthday()
p.change_last_name("Smith")
print(p)



