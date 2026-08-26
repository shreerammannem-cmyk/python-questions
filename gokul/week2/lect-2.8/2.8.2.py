# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB

yob = int(input())
current_age = 2026 - yob

if current_age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")