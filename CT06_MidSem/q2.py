"""
============================================================
Q2. Savings Simulator
============================================================
You are building a small savings simulator.
A person starts with a certain amount of money.

Every day, the person saves more money than the previous day:

Day 1 → save $1
Day 2 → save $2
Day 3 → save $3
Day 4 → save $4
… and so on

The program must:
- Ask for the starting amount of money.
- Ask for the number of days.
- For each day, add the correct savings amount.
- Print the total money after each day.
- Finally, print the final total amount.

Program Requirements:
- Use a for loop.
- Use range() correctly.
- Update the total amount inside the loop.
- Print exactly in this format:
    Day <X>: $<Y>
- After the loop, print:
    Total amount saved = $<Z>

Note:
- Follow the input order exactly as shown in the Test Cases.
- You must get the correct output for ALL 3 test cases.

============================================================
"""

# ============================================================
# Step 1: Ask for Starting Amount
# ============================================================

Start= input("how much money do you want to start with: ")

# ============================================================
# Step 2: Ask for Number of Days
# ============================================================

Days= input("how many days: ")

# ============================================================
# Step 3: Use a for loop to simulate savings
# ============================================================
# - Use range() correctly
# - Add the correct daily savings amount
# - Update and print the total each day
#   Day <X>: $<Y>
# ============================================================
total=int(Start)
for day in range (1,int(int(Days)+1)):
    total+=day

# ============================================================
# Step 4: Print Final Total
# ============================================================
# - Print the final amount in this format:
#   Total amount saved = $<Z>
# ============================================================
 
print ("Total amount saved=$" + str(total))