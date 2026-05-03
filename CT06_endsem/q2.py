"""
============================================================
Q2. List Operations
============================================================
You are working with a list of planets.
The program must perform several operations on this list.

Program Requirements:
- Use the list:
  planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
- Print the 3rd item using index
- Append "neptune" to the list
- Rename "mars" to "muskworld"
- Remove "uranus" from the list
- Using a for loop, print all the planets one by one

============================================================
"""

# ============================================================
# Step 1: Create the list
# ============================================================

planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]

# ============================================================
# Step 2: Print the 3rd item (Test Case 1)
#     - Comment after testing
# ============================================================

print(planets[2])

# ============================================================
# Step 3: Append "neptune"
# ============================================================

planets.append("neptune")

# ============================================================
# Step 4: Rename "mars" to "muskworld"
# ============================================================


planets[3]="muskworld"

# ============================================================
# Step 5: Remove "uranus"
# ============================================================

planets.remove ("uranus")

# ============================================================
# Step 6: Loop through and print all planets
# ============================================================

for i in planets:
    print(i)