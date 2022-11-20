class Worker:
    def __init__(self, n, s, p,w,b):
        self.name = n
        self.surname = s
        self.position = p
        self.__income = {"wage": w, "bonus": b}
    def get_income(self):
        return self.__income
class Position(Worker):
    def __init__(self, n, s, p,w,b):
        super().__init__(n, s, p,w,b)

    def summary_income(self):
        summary_income= float(self.get_income().get("bonus")) + float(self.get_income().get("wage"))
        return summary_income
    def full_name(self):
        return self.surname + " " + self.name
worker_1 = Worker("Alex","Klimov","VedSpec",49000,24000)
pos_1 = Position("Alex","Klimov","VedSpec",49000,24000)
pos_1.summary_income()

print(f"Общий доход сотрудника {pos_1.full_name()} равен {pos_1.summary_income()}")



