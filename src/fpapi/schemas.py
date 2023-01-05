from typing import List
from pydantic import BaseModel, Field


class PredictIncomeRequest(BaseModel):
    net_income: int = Field(..., title="Annual net income", example="3987654", description="給与振込口座等に記録された給与・賞与の手取りの年間合計金額")


class PredictIncomeResponse(BaseModel):
    gross_income: int = Field(..., title="Annual gross income", example="5000000", description="手取り額から推定された税込年収")


class SimulateLifetimeIncomeRequest(BaseModel):
    birthday: str = Field(..., title="Birthday", min_length=8, max_length=8, example="19890718", description="yyyymmdd形式で表現した生年月日")
    current_annual_income: int = Field(..., title="Current annual income", example="5000000", description="今年の見込年収。税込の総支給額")
    current_annual_bonus: int = Field(..., title="Current annual bonus", example="1500000", description="今年の年収のうち、賞与の見込金額。税込の総支給額")
    initial_age: int = Field(22, title="Initial age", example="22", description="給与所得が始まった年齢")
    initial_annual_income: int = Field(0, title="Initial annual income", example="3000000", description="初年度の年収。税込の総支給額")
    initial_annual_bonus: int = Field(0, title="Initial annual bonus", example="1500000", description="初年度の年収のうち、賞与の金額。税込の総支給額")
    retire_age: int = Field(60, title="Retire age", example="60", description="退職する年齢")
    retire_annual_income: int = Field(0, title="Retire annual income", example="7000000", description="退職する年の年収。税込の総支給額")
    retire_annual_bonus: int = Field(0, title="Retire annual bonus", example="2000000", description="退職する年の年収のうち、賞与の金額。税込の総支給額")
    max_age: int = Field(0, title="Max age", example="55", description="年収が最高額に達する年齢。たとえば55歳に役職定年がある場合などに設定")
    max_annual_income: int = Field(0, title="Max annual income", example="8000000", description="最高額の年収。税込の総支給額")
    max_annual_bonus: int = Field(0, title="Max annual income", example="8000000", description="最高額の年収のうち、賞与の金額。税込の総支給額")


class Income(BaseModel):
    amount: int = Field(..., title="Amount", description="給与または賞与の支給額")
    payday: str = Field(..., title="Payday", min_length=8, max_length=8, example="20220701", description="yyyymmdd形式で表現した支給日。計算便宜上すべて1日に設定")
    fiscal_year: int = Field(..., title="Fiscal year", description="年度。年金制度を考慮し一律4月始まりで計算")
    age: int = Field(..., title="Age", description="支給日の年齢")
    is_bonus: bool = Field(..., title="Is bonus", description="この収入が賞与か否か")


class SimulateLifetimeIncomeResponse(BaseModel):
    salary: List[Income] = Field(..., title="Salary", description="生涯に支給される給与の一覧")
    bonus: List[Income] = Field(..., title="Bonus", description="生涯に支給される賞与の一覧")


class CalculatePensionRequest(BaseModel):
    salary: List[Income] = Field(..., title="Lifetime salary", description="生涯に支給される給与の一覧")
    bonus: List[Income] = Field(..., title="Lifetime bonus", description="生涯に支給される賞与の一覧")
    basic_premium_period: int = Field(None, title="Basic premium period", description="老齢基礎年金の保険料支払月数")


class Pension(BaseModel):
    name: str = Field(..., title="Name", description="年金の名称")
    annual_amount: int = Field(..., title="Annual amount", description="年間受給額")
    monthly_amount: int = Field(..., title="Monthly amount", description="1ヶ月あたりの受給額")


class CalculatePensionResponse(BaseModel):
    basic_pension: Pension = Field(..., title="Basic pension", description="老齢基礎年金")
    employee_pension: Pension = Field(..., title="Employee pension", description="老齢厚生年金")


class SimulatePensionRequest(SimulateLifetimeIncomeRequest):
    basic_premium_period: int = Field(None, title="Basic premium period", example=480, description="老齢基礎年金の保険料支払月数")


class SimulatePensionResponse(CalculatePensionResponse):
    pass
