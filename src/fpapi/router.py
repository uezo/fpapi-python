from datetime import datetime
from fastapi import APIRouter
from fpapi.schemas import (
    Income,
    PredictIncomeRequest, PredictIncomeResponse,
    SimulateLifetimeIncomeRequest, SimulateLifetimeIncomeResponse,
    Pension, CalculatePensionRequest, CalculatePensionResponse,
    SimulatePensionRequest, SimulatePensionResponse
)
from fpapi.services.income import (
    IncomeCondition, IncomeService
)
from fpapi.services.pension import (
    PensionService
)

router = APIRouter()


@router.post("/income/predict",
             response_model=PredictIncomeResponse,
             summary="給与・賞与の手取額から年収を推定",
             description="給与振り込み口座などに記録された給与や賞与の振込金額の年間合計値から年金などの計算の基礎となる税込年収を推定",
             tags=["収入"])
async def predict_income(request: PredictIncomeRequest):
    gross_income = IncomeService.predict_gross_income(request.net_income)
    response = PredictIncomeResponse(gross_income=gross_income)

    return response


@router.post("/income/simulate",
             response_model=SimulateLifetimeIncomeResponse,
             summary="生涯収入のシミュレーション結果の取得",
             description="現在の年収や将来の見込み年収などから生涯にわたる給与および賞与をシミュレートし、その結果を一覧として取得",
             tags=["収入"])
async def simulate_income(request: SimulateLifetimeIncomeRequest):
    condition = IncomeCondition(
        birthday=datetime.strptime(request.birthday, "%Y%m%d").date(),
        current_annual_income=request.current_annual_income,
        current_annual_bonus=request.current_annual_bonus,
        initial_age=request.initial_age,
        initial_annual_income=request.initial_annual_income,
        initial_annual_bonus=request.initial_annual_bonus,
        retire_age=request.retire_age,
        retire_annual_income=request.retire_annual_income,
        retire_annual_bonus=request.retire_annual_bonus,
        max_age=request.max_age,
        max_annual_income=request.max_annual_income,
        max_annual_bonus=request.max_annual_bonus
    )

    lifetime_incomes = IncomeService.get_lifetime_incomes(condition=condition)

    salary = [
        Income(
            amount=s.amount,
            payday=s.payday.strftime("%Y%m%d"),
            fiscal_year=s.fiscal_year,
            age=s.age,
            is_bonus=False
        )
        for s in lifetime_incomes[0]
    ]
    bonus = [
        Income(
            amount=s.amount,
            payday=s.payday.strftime("%Y%m%d"),
            fiscal_year=s.fiscal_year,
            age=s.age,
            is_bonus=False
        )
        for s in lifetime_incomes[1]
    ]

    response = SimulateLifetimeIncomeResponse(salary=salary, bonus=bonus)

    return response


@router.post("/pension/calculate",
             response_model=CalculatePensionResponse,
             summary="年金受給額の計算結果の取得",
             description="給与・賞与の一覧から年金受給額を計算",
             tags=["年金"])
async def calculate_pension(request: CalculatePensionRequest):
    for s in request.salary:
        s.payday = datetime.strptime(s.payday, "%Y%m%d").date()
    for s in request.bonus:
        s.payday = datetime.strptime(s.payday, "%Y%m%d").date()

    p = PensionService()
    pensions = p.get_pension(request.salary, request.bonus, request.basic_premium_period)

    basic_pension = Pension(
        name=pensions[0].name,
        annual_amount=pensions[0].annual_amount,
        monthly_amount=pensions[0].monthly_amount,
    )

    employee_pension = Pension(
        name=pensions[1].name,
        annual_amount=pensions[1].annual_amount,
        monthly_amount=pensions[1].monthly_amount,
    )

    response = SimulatePensionResponse(basic_pension=basic_pension, employee_pension=employee_pension)

    return response


@router.post("/pension/simulate",
             response_model=SimulatePensionResponse,
             summary="年金受給額のシミュレーション結果の取得",
             description="現在の年収や将来の見込み年収などから生涯にわたる給与および賞与をシミュレートし、その結果を用いて年金受給額を計算",
             tags=["年金"])
async def simulate_pension(request: SimulatePensionRequest):
    condition = IncomeCondition(
        birthday=datetime.strptime(request.birthday, "%Y%m%d").date(),
        current_annual_income=request.current_annual_income,
        current_annual_bonus=request.current_annual_bonus,
        initial_age=request.initial_age,
        initial_annual_income=request.initial_annual_income,
        initial_annual_bonus=request.initial_annual_bonus,
        retire_age=request.retire_age,
        retire_annual_income=request.retire_annual_income,
        retire_annual_bonus=request.retire_annual_bonus,
        max_age=request.max_age,
        max_annual_income=request.max_annual_income,
        max_annual_bonus=request.max_annual_bonus
    )

    lifetime_incomes = IncomeService.get_lifetime_incomes(condition=condition)
    p = PensionService()
    pensions = p.get_pension(lifetime_incomes[0], lifetime_incomes[1], request.basic_premium_period)

    basic_pension = Pension(
        name=pensions[0].name,
        annual_amount=pensions[0].annual_amount,
        monthly_amount=pensions[0].monthly_amount,
    )

    employee_pension = Pension(
        name=pensions[1].name,
        annual_amount=pensions[1].annual_amount,
        monthly_amount=pensions[1].monthly_amount,
    )

    response = SimulatePensionResponse(basic_pension=basic_pension, employee_pension=employee_pension)

    return response
