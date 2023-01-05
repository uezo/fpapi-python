from datetime import date
from fpapi.services.income import Income


class Pension:
    def __init__(self, name: str, annual_amount: int) -> None:
        self.name = name
        self.annual_amount = annual_amount
        self.monthly_amount = int(annual_amount / 12)


class PensionService:
    def __init__(self) -> None:
        self.basic_pension_amount = 778_000

    @classmethod
    def to_standard_salary(cls, monthly_salary: int, year: int, month: int) -> int:
        if monthly_salary < 93000:
            return 88000
        elif monthly_salary >= 93000 and monthly_salary < 101000:
            return 98000
        elif monthly_salary >= 101000 and monthly_salary < 107000:
            return 104000
        elif monthly_salary >= 107000 and monthly_salary < 114000:
            return 110000
        elif monthly_salary >= 114000 and monthly_salary < 122000:
            return 118000
        elif monthly_salary >= 122000 and monthly_salary < 130000:
            return 126000
        elif monthly_salary >= 130000 and monthly_salary < 138000:
            return 134000
        elif monthly_salary >= 138000 and monthly_salary < 146000:
            return 142000
        elif monthly_salary >= 146000 and monthly_salary < 155000:
            return 150000
        elif monthly_salary >= 155000 and monthly_salary < 165000:
            return 160000
        elif monthly_salary >= 165000 and monthly_salary < 175000:
            return 170000
        elif monthly_salary >= 175000 and monthly_salary < 185000:
            return 180000
        elif monthly_salary >= 185000 and monthly_salary < 195000:
            return 190000
        elif monthly_salary >= 195000 and monthly_salary < 210000:
            return 200000
        elif monthly_salary >= 210000 and monthly_salary < 230000:
            return 220000
        elif monthly_salary >= 230000 and monthly_salary < 250000:
            return 240000
        elif monthly_salary >= 250000 and monthly_salary < 270000:
            return 260000
        elif monthly_salary >= 270000 and monthly_salary < 290000:
            return 280000
        elif monthly_salary >= 290000 and monthly_salary < 310000:
            return 300000
        elif monthly_salary >= 310000 and monthly_salary < 330000:
            return 320000
        elif monthly_salary >= 330000 and monthly_salary < 350000:
            return 340000
        elif monthly_salary >= 350000 and monthly_salary < 370000:
            return 360000
        elif monthly_salary >= 370000 and monthly_salary < 395000:
            return 380000
        elif monthly_salary >= 395000 and monthly_salary < 425000:
            return 410000
        elif monthly_salary >= 425000 and monthly_salary < 455000:
            return 440000
        elif monthly_salary >= 455000 and monthly_salary < 485000:
            return 470000
        elif monthly_salary >= 485000 and monthly_salary < 515000:
            return 500000
        elif monthly_salary >= 515000 and monthly_salary < 545000:
            return 530000
        elif monthly_salary >= 545000 and monthly_salary < 575000:
            return 560000
        elif monthly_salary >= 575000 and monthly_salary < 605000:
            return 590000
        elif monthly_salary >= 605000 and monthly_salary < 635000:
            return 620000
        elif monthly_salary >= 635000:
            if year * 100 + month >= 202009:
                return 650000
            else:
                return 620000
        else:
            return 0

    @classmethod
    def to_standard_bonus(cls, amount: int) -> int:
        return min(amount // 1000 * 1000, 1_500_000)

    def get_basic_pension(self, paid_months: int) -> Pension:
        return Pension("老齢基礎年金", int(self.basic_pension_amount * paid_months / 480))

    def get_employee_pension(self, lifetime_salary: list[Income], lifetime_bonus: list[Income]) -> Pension:
        salary_period_A = [self.to_standard_salary(s.amount, s.payday.year, s.payday.month) for s in lifetime_salary if s.payday < date(2003, 4, 1)]
        if len(salary_period_A) > 0:
            standard_monthly_income_average = int(sum(salary_period_A) / len(salary_period_A))
            annual_pension_a = int(standard_monthly_income_average * 0.007125 * len(salary_period_A))
        else:
            annual_pension_a = 0

        salary_period_B = [self.to_standard_salary(s.amount, s.payday.year, s.payday.month) for s in lifetime_salary if s.payday >= date(2003, 4, 1)]
        bonus_period_B = [self.to_standard_bonus(b.amount) for b in lifetime_bonus if b.payday >= date(2003, 4, 1)]
        standard_income_total = sum(salary_period_B) + sum(bonus_period_B)
        standard_income_average = int(standard_income_total / len(salary_period_B))
        annual_pension_b = int(standard_income_average * 0.005481 * len(salary_period_B))

        annual_pension = annual_pension_a + annual_pension_b

        return Pension("老齢厚生年金", annual_pension)

    def get_pension(self, lifetime_salary: list[Income], lifetime_bonus: list[Income], basic_premium_period: int = None) -> tuple[Pension]:
        basic_pension = self.get_basic_pension(
            len(lifetime_salary) if basic_premium_period is None
            else basic_premium_period)
        employee_pension = self.get_employee_pension(lifetime_salary, lifetime_bonus)

        return [basic_pension, employee_pension]
