class Oboi():
    def __init__(self,x,y,z):
        try:
            self.x = int(x)
            self.y = int(y)
            self.z = int(z)
            self.okno = 0
            self.dver = 0
        except TypeError:
            self.x = 0
            self.y = 0
            self.z = 0

    def Okna(self,xo,zo):
        xo=int(xo)
        zo = int(zo)
        self.okno +=(xo*zo)

    def Dveri(self,xd,zd):
        xd = int(xd)
        zd = int(zd)
        self.dver += (xd * zd)
    def ploshad(self):
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            print("Данные введены некоректно")
        else:
            self.plos = ((int(self.x)*int(self.z*2))+(int(self.y* int(self.z))*2)) - (int(self.dver )+int(self.okno))
            print(f"Для обклейки вашей комнаты потребуется {self.plos} м^2 обоев")


    def Komnata(self):

        xx = 0
        print("Введите параметры комнаты")
        plos = Oboi(input(), input(), input())

        while xx != 'Готово' and xx != "Нет":
            print(
                "Есть ли ещё в вашей комнате окно или дверь? Если есть окно - напишите Окно, если есть дверь - напишите Дверь, если ничего из этого нет - напишите Нет")
            xx = input()
            if xx == "Окно":
                print("Введите параметры окна")
                plos.Okna(input(), input())
            elif xx == "Дверь":
                print("Введите параметры двери")
                plos.Dveri(input(), input())
            else:
                xx = input("Хотите ли вы закончить ввод данных?")
        print(plos.ploshad())
