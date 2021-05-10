class Haedal:

    def __init__(self, sname, sid):
        self.sname = sname
        self.sid = sid

    def info(self):
        print(f'이름 : {self.sname}')
        print(f'학번 : {self.sid}')
        print()


std1 = Haedal('김해규', 2017111111)
std2 = Haedal('이해규', 2018111111)
std3 = Haedal('박해규', 2019111111)

std1.info()
std2.info()
std3.info()
