class Creature: #주석을 다시 쓰고 있음 ㅇㅇㄹㄹ
    num=0
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp
        print("{0} 동물 탄생".format(name))
        Creature.num+=1

    def __del__(self):
        Creature.num-=1
        print("{0} 동물 죽음".format(self.name))

    def eat(self):
        self.hp+=10
        print('밥을 먹어 체력이 10 회복되었습니다.')

    def sleep(self):
        self.hp+=10
        print('잠을 자 체력이 10 회복되었습니다.')

    def move(self):
        self.hp-=30
        print('뛰어서 체력이 30 깎였습니다.')

    @classmethod
    def show_count(cls):
        print('현재 동물 수 : {0}'.format(cls.num))

    @staticmethod
    def has_died(hp):
        return hp<=0

c1=Creature('wolf',50)
c2=Creature('rabbit',20)

c1.eat() # 늑대 체력 +10
c2.sleep() # 토끼 체력 +10
c2.move() # 토끼 체력 -30

Creature.show_count()수 # 토끼, 늑대 두마

if Creature.has_died(c2.hp):리 # 20+10-30<=0 : True
    print(f"{c2.name} 이 체력이 떨어져 죽었습니다.")
    Creature.num-=1

Creature.show_count() # 토끼 없어진 후 동물 
