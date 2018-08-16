from sources import weekly, daily

print("Daily forecast:",daily.forecast())
print("Weekly forcase:")
for number,outlook in enumerate(weekly.forecast(),1):
    print(number, outlook)
