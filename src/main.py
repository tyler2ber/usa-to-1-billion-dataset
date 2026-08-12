
# data
regions_coastal = {
    "East Coast north": 74040972,
    "East Coast south": 47211247,
    "Great Lakes": 46869214,
    "Gulf Coast": 62392003,
    "West Coast": 51034834,
}
regions_coastal_total = sum(regions_coastal.values())

# projection data
projections = {
    "East Coast north": -1,
    "East Coast south": -1,
    "Great Lakes": -1,
    "Gulf Coast": -1,
    "West Coast": -1
}
projections_total = -1

# PROJECTIONS
print("\nPROJECTIONS")

gen_counter = 0
while projections_total < 1000000000:

    # CALCULATE
    if projections_total == -1:

        # projections total (init)
        projections_total = regions_coastal_total

        # projections (init)
        for projection in projections:
            projections[projection] = regions_coastal[projection]

        # gen (init)
        gen_counter = 1

    else:

        # projections total
        projections_total = (projections_total / 2) * 3

        # projections
        for projection in projections:
            projections[projection] = (projections[projection] / 2) * 3

        # gen
        gen_counter += 1

    # PRINT
    print(f"====> usa_regions(gen{gen_counter}): {round(projections_total):,}")

    entry_total = -1
    for projection in projections:
        print(f"- {round(projections[projection]):,} in {projection}")

print("") # lul