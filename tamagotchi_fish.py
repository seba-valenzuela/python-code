from datetime import date

# This creates a Tamagotchi Fish class for the end user to interact with

class Tamagotchi_fish:
    def __init__(self, name):
        self.name = name
        self.birthday = date.today()
        print("\nYour fish '"+name+"' was born on "+str(self.birthday))
        self.__print_fish1()
        self.size = 1

    def feed_fish(self):
        print("After feeding "+self.name+", they have grown...")
        self.size += 1
        if self.size == 1:
            self.__print_fish1()
        elif self.size == 2:
            self.__print_fish2()
        elif self.size == 3:
            self.__print_fish3()
        elif self.size == 4:
            self.__print_fish4()
        else:
            print("Ran out of fish drawings!\n")


    def __print_fish1(self):
        print(r"""
        
       ,,
      (')<
       ``
        """)

    def __print_fish2(self):
        print(r"""
       _
      /_|
     ('_)<|
      \_|    

        """)

    def __print_fish3(self):
        print(r"""
      __
     /__|
    /'  \/|
    \<__/\|
     \__|

        """)

    def __print_fish4(self):
        print(r"""

   ,-----.
  /____  /
 /     \/ _
/ O     \/ |
>          |
\ <)    /\_|
 \_____/\    
  \      \
   `-----'    

        """)

    

a = Tamagotchi_fish("Tom")
a.feed_fish()

b = Tamagotchi_fish("Steven")
b.feed_fish()