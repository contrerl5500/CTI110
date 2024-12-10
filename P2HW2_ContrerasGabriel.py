# Gabriel 
# 10SEP2024
# P2HW2
# Using Python for school grades

grade_mods = ("Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6")

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

mod_list = [mod1, mod2, mod3, mod4, mod5, mod6]

print("------------Results------------")
print(f"{'Lowest Grade:':<20}{min(mod_list)}")
print(f"{'Highest Grade:':<20}{max(mod_list)}")
print(f"{'Sum of Grades:':<20}{sum(mod_list)}")
print(f"{'Average Grade:':<20}{sum(mod_list)/ len(mod_list):.2f}")
print("----------------------------------")
