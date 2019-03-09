import csv

with open('budget_data.csv', 'r') as open_file:
    records = csv.reader(open_file, delimiter=',')

    count = 0
    month_count = 0
    total = 0
    increase = 0
    increaseMonth = ''
    decrease = 0
    decreaseMonth = ''
    qtyChange = 0
    profit = 0
    fisrtAmount = 0
    registers = []

    

    for row in records:
        if count != 0:
            month_count = month_count + 1
            total = total + float(row[2])

            if (float(row[2]) < decrease):
                decrease = float(row[2])
                decreaseMonth = row[1]
            if (float(row[2]) > increase):
                increase = float(row[2])
                increaseMonth = row[1]            

        registers.append(row)

        if count == 1:
            lastAmount = float(row[2])
            
        if count > 1:
            if (float(row[2]) > lastAmount):
                # print 'lastAmount', lastAmount, 'actual', row[2], ' Gane'
                profit = float(row[2]) - lastAmount
                lastAmount = float(row[2])
                qtyChange = qtyChange + 1
                # print 'Ganancia ', profit
            if (float(row[2]) < lastAmount):
                # print 'lastAmount', lastAmount, 'actual', row[2], ' Perdi'
                profit = lastAmount - float(row[2])
                lastAmount = float(row[2])
                qtyChange = qtyChange + 1
                # print 'Perdida ', profit

        count = count + 1

    fisrtAmount = float(registers[1][2])

    print 'Total Months: ', month_count
    print 'Total: ', total
    print 'qtyChange: ', qtyChange
    print 'profit: ', (profit - fisrtAmount) / fisrtAmount
    print 'Greatest Increase in Profits: ', increaseMonth, '($', increase, ')'
    print 'Greatest Decrease in Profits: ', decreaseMonth, '($', decrease, ')'
