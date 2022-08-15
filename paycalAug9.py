pay_rate = input("Please enter your pay rate: ")
pay_rate_converted = float(pay_rate)
hours_worked = input("Please enter your hours worked: ")
hours_worked_converted = float(hours_worked)
total_pay = 0
standard_work_week = 40
overtime_multiplier = 1.5

if hours_worked_converted > standard_work_week:
    #calc overtime pay
    regular_pay = pay_rate_converted * standard_work_week
    hours_of_overtime = hours_worked_converted - standard_work_week
    pay_rate_on_overtime = pay_rate_converted * overtime_multiplier
    overtime_pay = hours_of_overtime * pay_rate_on_overtime
    total_pay = overtime_pay + regular_pay
else:
    total_pay = pay_rate_converted * hours_worked_converted

print(total_pay)

income_tax_rate = 0.12
income_tax = total_pay * income_tax_rate

total_pay_minus_tax = total_pay - income_tax
print(total_pay_minus_tax)

weeks_in_a_year = 52
annual_PTO_hours = 35
weeks_worked = hours_worked_converted / standard_work_week
PTO_accured_per_week = annual_PTO_hours / weeks_in_a_year
print(PTO_accured_per_week)

Paid_time_off_accrued = weeks_worked * PTO_accured_per_week
print(Paid_time_off_accrued)

time_oofff = (hours_worked_converted * PTO_accured_per_week) / standard_work_week
print(f"this is your accrued time off:{time_oofff} hours")