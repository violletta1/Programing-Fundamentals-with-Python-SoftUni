# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees'id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"

information = input()
all_companies = {}
while "End" not in information:
    company_name, employee_id = information.split(" -> ")
    if company_name not in all_companies.keys():
        all_companies[company_name] = [employee_id]
    else:
        if employee_id in all_companies[company_name]:
            information = input()
            continue
        else:
            all_companies[company_name].append(employee_id)


    information = input()

for company_name, employees in all_companies.items():
    print(company_name)
    for employee in employees:
        print(f"-- {employee}")

