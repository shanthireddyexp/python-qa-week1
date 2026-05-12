"""Variables & data types:No type declaration needed — Python infers it:"""
name = "Prasanthi"   # str
age  = 28            # int
score = 95.5         # float
is_qa = True         # bool
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of score:", type(score))
print("Type of is_qa:", type(is_qa))


"""f-strings
Embed variables directly inside strings using f"...":"""
print("f-strings output:")
print(f"Name: {name}, Age: {age}, Score: {score}, Is QA: {is_qa}")


"""if / elif / else blocks
Indentation (4 spaces) replaces curly braces in Python:"""

score = 72
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
    
"""for loop — iterate a list
Loop over any list directly:"""
browsers = ["Chrome", "Firefox", "Safari"]
for browser in browsers:
    print(f"Testing on {browser}")

for i in range(1, 6):   # 1 to 5
    print(f"Test case #{i}")