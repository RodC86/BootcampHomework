import csv

with open('election_data.csv', 'r') as open_file:
    records = csv.reader(open_file, delimiter=',')

    count = 0
    candidates = {}

    for row in records:
        if count > 0:
            label =  row[2]
            if label in candidates:
                candidates[row[2]]["count"] = int(candidates[row[2]]["count"]) + 1
            else:
                candidates[row[2]] = {
                    "count": 1,
                    "value": row[2]
                }

        count = count + 1

    print 'Election Results'
    print '-------------------------'
    print 'Total Votes: ', count
    print '-------------------------'

    winner = 0
    winnerLabel = ''
    for candidate in candidates:
        print candidates[candidate]["value"], ': ', (candidates[candidate]["count"] * 100 / count), '% (', candidates[candidate]["count"], ')'
        if candidates[candidate]["count"] > winner:
            winner = candidates[candidate]["count"]
            winnerLabel = candidates[candidate]["value"]
    print '-------------------------'
    print 'Winner: ', winnerLabel
    print '-------------------------'
        

