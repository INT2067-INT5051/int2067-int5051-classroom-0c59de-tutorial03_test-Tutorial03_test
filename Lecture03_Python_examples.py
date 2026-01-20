# ==========================================
# Lecture 3 – Basic II
#INT2067 & INT5051
#Introduction to Programming and Problem Solving
# ==========================================

# --- 1. ASSIGNMENT-----
print("--- Section 1: Assignment ---")
# FIELD TRIP CALCULATOR
# Declare variables
a = 32
y = 10

# ARITHMETIC---
print("--- Section 2: Arithmetic ---")

# 1. Addition (+)
b = 4
c = a + b
print(f"c= {c}")

# 2. Subtraction (-)
absent_students = 2
actual_students = total_students - absent_students
print(f"Students actually attending: {actual_students}")

# 3. Multiplication (*)
ticket_price = 20.50
total_cost = actual_students * ticket_price
print(f"Total cost for students: ${total_cost}")

# 4. Division (/)
# Notice how it becomes 3.2 (a float)
exact_buses_needed = total_students / bus_capacity
print(f"Exact buses mathematical result: {exact_buses_needed}")

# 5. Floor Division (//)
# Tells us how many buses are completely full
full_buses = total_students // bus_capacity
print(f"Number of completely full buses: {full_buses}")

# 6. Modulo (%)
# Tells us how many students are in the partially filled bus
students_left_over = total_students % bus_capacity
print(f"Students in the last (partial) bus: {students_left_over}")

# 7. Exponent (**)
# Used for things like calculating area in a geometry lesson
square_playground_side = 5
area = square_playground_side ** 2
print(f"Area of a 5x5 playground: {area} sq units")

# --- 2. COMPARISON & LOGICAL ---
print("--- Section 2: Comparison & Logic ---")
score = 85
attendance = 92
has_golden_ticket = False

# Eligibility Logic
# Criteria: (Score 70+ AND Attendance 80+) OR Golden Ticket
is_valid_score = 0 <= score <= 100  # Python's chained comparison
passed = (score >= 70 and attendance >= 80) or has_golden_ticket

print(f"Is the score {score} valid? {is_valid_score}")
print(f"Student passed? {passed}")
print("-" * 30)


# --- 3. PRECEDENCE & ASSOCIATIVITY ---
print("--- Section 3: Precedence ---")
# PEMDAS check
calc_1 = 10 + 5 * 2    # Should be 20
calc_2 = (10 + 5) * 2  # Should be 30

# Exponents are Right-to-Left
# 2 ** 3 ** 2 is 2 ** (3 ** 2) = 2 ** 9
right_to_left = 2 ** 3 ** 2 

print(f"10 + 5 * 2 = {calc_1}")
print(f"(10 + 5) * 2 = {calc_2}")
print(f"2 ** 3 ** 2 = {right_to_left}")
print("-" * 30)


# --- 4. ATTENTION CASES (Common Mistakes) ---
print("--- Section 4: Attention Cases ---")

# String repetition vs math
string_math = "Apple" * 3
print(f"'Apple' * 3 = {string_math}")

# String concatenation vs addition
str_add = "5" + "5"
int_add = 5 + 5
print(f"'5' + '5' as strings: {str_add}")
print(f"5 + 5 as integers: {int_add}")

# The Equality vs Assignment trap
# x = 10 (Assignment)
# x == 10 (Comparison)
x = 10
print(f"Is x equal to 10? {x == 10}")
print("-" * 30)


# --- 5. CLASSROOM PRACTICE SOLUTIONS ---
print("--- Section 5: Practice Solutions ---")

# Exercise A: The Bus Trip
students_trip = 142
bus_capacity = 40
full_buses = students_trip // bus_capacity
last_bus_count = students_trip % bus_capacity
print(f"Buses needed: {full_buses} full, and 1 with {last_bus_count} students.")

# Exercise C: Password Logic
pwd = "mypassword"
is_secure = len(pwd) >= 8 and pwd != "password123"
print(f"Is the password '{pwd}' secure? {is_secure}")