class Home:
    def Knock(self, person_one=None, person_two=None): #o que acontece se eu tirar o None
        if person_one is not None and person_two is None:
            print("Hi, " + person_one)
        elif person_one is not None and person_two is not None:
            print("Hi, " + person_one + " and " + person_two)
        else: 
            print("Who's there? ")

DefObj = Home()

DefObj.Knock()
DefObj.Knock('Rick','Morty')
DefObj.Knock('Sam')