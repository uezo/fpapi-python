from datetime import date, datetime


class Income:
    def __init__(self, amount: int, payday: date, fiscal_year: int, age: int, is_bonus: bool = False):
        self.amount = amount
        self.payday = payday
        self.fiscal_year = fiscal_year
        self.age = age
        self.is_bonus = is_bonus


class IncomeCondition:
    def __init__(
        self,
        birthday: date,
        current_annual_income: int,
        current_annual_bonus: int,
        initial_age: int = 22,
        initial_annual_income: int = 0,
        initial_annual_bonus: int = 0,
        retire_age: int = 60,
        retire_annual_income: int = 0,
        retire_annual_bonus: int = 0,
        max_age: int = 60,
        max_annual_income: int = 0,
        max_annual_bonus: int = 0
    ):
        self.birthday = birthday
        self.current_annual_income = current_annual_income
        self.current_annual_bonus = current_annual_bonus
        self.initial_age = initial_age
        self.initial_annual_income = initial_annual_income
        self.initial_annual_bonus = initial_annual_bonus
        self.retire_age = retire_age
        self.retire_annual_income = retire_annual_income
        self.retire_annual_bonus = retire_annual_bonus
        self.max_age = max_age
        self.max_annual_income = max_annual_income
        self.max_annual_bonus = max_annual_bonus


class IncomeService:
    net_income_mapper = [
        (834920,1000000),
        (934620,1100000),
        (1012476,1200000),
        (1081956,1300000),
        (1154276,1400000),
        (1226896,1500000),
        (1299416,1600000),
        (1376536,1700000),
        (1455156,1800000),
        (1529100,1900000),
        (1603056,2000000),
        (1677100,2100000),
        (1766300,2200000),
        (1840456,2300000),
        (1914300,2400000),
        (2003400,2500000),
        (2062400,2600000),
        (2151500,2700000),
        (2210400,2800000),
        (2299700,2900000),
        (2358500,3000000),
        (2447700,3100000),
        (2536800,3200000),
        (2595500,3300000),
        (2684700,3400000),
        (2743600,3500000),
        (2832900,3600000),
        (2920500,3700000),
        (2977900,3800000),
        (3065500,3900000),
        (3122900,4000000),
        (3210500,4100000),
        (3268000,4200000),
        (3355600,4300000),
        (3443200,4400000),
        (3498600,4500000),
        (3582400,4600000),
        (3665900,4700000),
        (3706756,4800000),
        (3790356,4900000),
        (3873856,5000000),
        (3914700,5100000),
        (3998300,5200000),
        (4082000,5300000),
        (4165500,5400000),
        (4206456,5500000),
        (4289956,5600000),
        (4373756,5700000),
        (4457256,5800000),
        (4498100,5900000),
        (4581700,6000000),
        (4665200,6100000),
        (4705956,6200000),
        (4789556,6300000),
        (4873356,6400000),
        (4955456,6500000),
        (4993600,6600000),
        (5065900,6700000),
        (5138200,6800000),
        (5173556,6900000),
        (5246056,7000000),
        (5318356,7100000),
        (5390756,7200000),
        (5426000,7300000),
        (5498300,7400000),
        (5570900,7500000),
        (5643200,7600000),
        (5678456,7700000),
        (5750856,7800000),
        (5823156,7900000),
        (5881140,8000000),
        (5953840,8100000),
        (6026140,8200000),
        (6098540,8300000),
        (6156636,8400000),
        (6228936,8500000),
        (6298536,8600000),
        (6367836,8700000),
        (6418056,8800000),
        (6487356,8900000),
        (6556656,9000000),
        (6626256,9100000),
        (6695556,9200000),
        (6745776,9300000),
        (6815076,9400000),
        (6884276,9500000),
        (6953976,9600000),
        (7023276,9700000),
        (7073596,9800000),
        (7142896,9900000),
        (7212196,10000000),
        (7850996,11000000),
        (8491140,12000000),
        (9120596,13000000),
        (9635356,14000000),
        (10150616,15000000),
        (10688696,16000000),
        (11226676,17000000),
        (11788076,18000000),
        (12349476,19000000),
        (12910876,20000000),
        (13472276,21000000),
        (14033576,22000000),
        (14535576,23000000),
        (15025676,24000000),
        (15515776,25000000),
        (15926576,26000000),
        (16256876,27000000),
        (16747176,28000000),
        (17234776,29000000),
        (17724876,30000000),
        (18214976,31000000),
        (18705076,32000000),
        (19195276,33000000),
        (19685376,34000000),
        (20175476,35000000),
        (20665676,36000000),
        (21155676,37000000),
        (21645876,38000000),
        (22135976,39000000),
        (22626176,40000000),
        (23116276,41000000),
        (23606276,42000000),
        (24096476,43000000),
        (24573976,44000000),
        (25013176,45000000),
        (25452376,46000000),
        (25891476,47000000),
        (26330876,48000000),
        (26770076,49000000),
        (27209276,50000000),
        (27648576,51000000),
        (28087676,52000000),
        (28526976,53000000),
        (28966176,54000000),
        (29405476,55000000),
        (29844676,56000000),
        (30283776,57000000),
        (30723176,58000000),
        (31162376,59000000),
        (31601576,60000000),
        (32040776,61000000),
        (32479976,62000000),
        (32919276,63000000),
        (33358476,64000000),
        (33797776,65000000),
        (34236976,66000000),
        (34676076,67000000),
        (35115376,68000000),
        (35554676,69000000),
        (35993876,70000000),
        (36433076,71000000),
        (36872276,72000000),
        (37311576,73000000),
        (37750776,74000000),
        (38189976,75000000),
        (38629276,76000000),
        (39068376,77000000),
        (39507676,78000000),
        (39946976,79000000),
        (40386176,80000000),
        (40825376,81000000),
        (41264476,82000000),
        (41703876,83000000),
        (42143076,84000000),
        (42582276,85000000),
        (43021576,86000000),
        (43460676,87000000),
        (43899976,88000000),
        (44339176,89000000),
        (44778476,90000000),
        (45217676,91000000),
        (45656776,92000000),
        (46096176,93000000),
        (46535376,94000000),
        (46974576,95000000),
        (47413776,96000000),
        (47852976,97000000),
        (48292276,98000000),
        (48731476,99000000),
        (49170776,100000000)
    ]

    @classmethod
    def get_linearized_incomes(
        cls,
        start_income: int, start_age: int,
        end_income: int, end_age: int
    ) -> dict[int, int]:

        linearized_incomes = {}

        if end_age > start_age:
            income_gap = end_income - start_income
            age_gap = end_age - start_age
            gap_per_year = income_gap / age_gap
            for i in range(age_gap):
                linearized_incomes[start_age + i] = int(start_income + gap_per_year * i)

        linearized_incomes[end_age] = end_income

        return linearized_incomes

    @classmethod
    def get_lifetime_annual_incomes(
        cls,
        current_income: int, current_age: int,
        initial_income: int = 0, initial_age: int = 22,
        retire_income: int = 0, retire_age: int = 60,
        max_income: int = 0, max_age: int = 0
    ) -> dict[int, int]:

        annual_incomes = cls.get_linearized_incomes(
            initial_income if initial_income > 0 else current_income,
            initial_age, current_income, current_age
        )

        if max_income > 0 and max_age > 0:
            annual_incomes |= cls.get_linearized_incomes(
                current_income, current_age, max_income, max_age
            )
            annual_incomes |= cls.get_linearized_incomes(
                max_income, max_age,
                retire_income if retire_income > 0 else max_income,
                retire_age - 1
            )

        else:
            annual_incomes |= cls.get_linearized_incomes(
                current_income, current_age,
                retire_income if retire_income > 0 else current_income,
                retire_age - 1
            )

        return annual_incomes

    @classmethod
    def age_at(cls, day: date, birthday: date) -> int:
        return (int(day.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

    @classmethod
    def get_initial_year(cls, initial_age: int, birthday: date) -> int:
        current_age = cls.age_at(date.today(), birthday)
        initial_year = date.today().year - (current_age - initial_age)
        if birthday.month <= 3:
            initial_year -= 1
        if date.today() >= date(date.today().year, birthday.month, birthday.day):
            initial_year += 1
        return initial_year

    @classmethod
    def get_lifetime_incomes(
        cls,
        condition: IncomeCondition
    ) -> tuple[list[Income], list[Income]]:
        current_age = (int(datetime.now().strftime("%Y%m%d")) - int(condition.birthday.strftime("%Y%m%d"))) // 10000
        initial_year = cls.get_initial_year(condition.initial_age, condition.birthday)

        # salary
        lifetime_salary = []
        lifetime_annual_salary = cls.get_lifetime_annual_incomes(
            condition.current_annual_income - condition.current_annual_bonus, current_age,
            condition.initial_annual_income - condition.initial_annual_bonus, condition.initial_age,
            condition.retire_annual_income - condition.retire_annual_bonus, condition.retire_age,
            condition.max_annual_income - condition.max_annual_bonus, condition.max_age)

        for i, age in enumerate(lifetime_annual_salary):
            fy = initial_year + i
            for m in range(12):
                payday = date(fy if m < 9 else fy + 1, m + 4 if m < 9 else m - 8, 1)
                if payday >= date(condition.birthday.year + condition.retire_age, condition.birthday.month, 1):
                    break
                amount = int(lifetime_annual_salary[age] / 12)
                lifetime_salary.append(Income(amount, payday, fy, cls.age_at(payday, condition.birthday)))

        # bonus
        lifetime_bonus = []
        lifetime_annual_bonus = cls.get_lifetime_annual_incomes(
            condition.current_annual_bonus, current_age,
            condition.initial_annual_bonus, condition.initial_age,
            condition.retire_annual_bonus, condition.retire_age,
            condition.max_annual_bonus, condition.max_age)

        for i, age in enumerate(lifetime_annual_bonus):
            fy = initial_year + i
            lifetime_bonus.append(Income(
                int(lifetime_annual_bonus[age] / 2),
                date(fy, 6, 1), fy, cls.age_at(date(fy, 6, 1), condition.birthday), True
            ))
            lifetime_bonus.append(Income(
                int(lifetime_annual_bonus[age] / 2),
                date(fy, 12, 1), fy, cls.age_at(date(fy, 12, 1), condition.birthday), True
            ))

        return (lifetime_salary, lifetime_bonus)

    @classmethod
    def predict_gross_income(cls, net_income: int):
        for i, n in enumerate(cls.net_income_mapper):
            if n[0] >= net_income:
                n_lower = cls.net_income_mapper[i - 1]
                to_next_class_percentage = (net_income - n_lower[0]) / (n[0] - n_lower[0])
                to_next_class_amount = int((n[1] - n_lower[1]) * to_next_class_percentage)
                return n_lower[1] + to_next_class_amount
