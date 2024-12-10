# Gabriel 
# 17SEP2024
# P3HW1
# Using Branching 

grade_mods = ("Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6")

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()


mod_list = [mod1, mod2, mod3, mod4, mod5, mod6]

lowest = min(mod_list)
highest = max(mod_list)
total = sum(mod_list)
avg = sum(mod_list) /len(mod_list)

print("------------Results------------")
print(f"{'Lowest Grade:':<20}{min(mod_list)}")
print(f"{'Highest Grade:':<20}{max(mod_list)}")
print(f"{'Sum of Grades:':<20}{sum(mod_list)}")
print(f"{'Average Grade:':<20}{sum(mod_list)/ len(mod_list):.2f}")
print("----------------------------------------")

# Branching to determine the letter grade

letter_grade = ""

if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print()
print(f"Your Grade is: {letter_grade}")
