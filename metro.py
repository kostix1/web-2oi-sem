def metro(entries, exits, time):
    count = 0
    for entry, exit in zip(entries, exits):
        if entry <= time <= exit:
            count += 1
    print(count)