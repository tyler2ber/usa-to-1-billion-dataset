import pandas as pd

# data
regions_coastal = {
    "East Coast north": 74040972,
    "East Coast south": 47211247,
    "Great Lakes": 46869214,
    "Gulf Coast": 62392003,
    "West Coast": 51034834,
}
regions_coastal_total = sum(regions_coastal.values())

# projections data w/ df_projections
projections = {
    "East Coast north": -1,
    "East Coast south": -1,
    "Great Lakes": -1,
    "Gulf Coast": -1,
    "West Coast": -1
}
projections_total = -1

df_projections = pd.DataFrame(columns=
    [
        "GEN",
        "total_population",
        "East Coast north",
        "East Coast south",
        "Great Lakes",
        "Gulf Coast",
        "West Coast"
    ]
).astype(
    {
        "GEN": "int64",
        "total_population": "int64",
        "East Coast north": "int64",
        "East Coast south": "int64",
        "Great Lakes": "int64",
        "Gulf Coast": "int64",
        "West Coast": "int64"
    }
)

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

    # PRINT...
    print(f"====> usa_regions(gen{gen_counter}): {round(projections_total):,}")
    for projection in projections:
        print(f"- {round(projections[projection]):,} in {projection}")

    # ...and update df_projections
    df_projections.loc[len(df_projections)] = [
        gen_counter,
        round(projections_total),
        round(projections["East Coast north"]),
        round(projections["East Coast south"]),
        round(projections["Great Lakes"]),
        round(projections["Gulf Coast"]),
        round(projections["West Coast"])
    ]

print("") # lul
df_projections.to_csv("dataset/usa-to-1-billion.csv", index=False)