class Mixin1:
    def run(self):
        print('Mixin1')


class Mixin2:
    def run(self):
        print('Mixin2')


class Case1(Mixin1, Mixin2): #Case1 -▷ Mixin1 -▷ Mixin2
    pass


class Case2(Mixin2, Mixin1): #Case1 -▷ Mixin2 -▷ Mixin1
    pass

Case1().run()   #Mixin1
Case2().run()   #Mixin2
