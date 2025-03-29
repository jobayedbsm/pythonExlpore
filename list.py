timeline = [0, 10, 20, 30, 40, 50]

# Ads timestamp
ads_timestamp=25

# find the correct index for insertaion
for i in range(len(timeline)):
    if timeline[i]>ads_timestamp:
        timeline.insert(i,ads_timestamp)
        break

print(timeline)