import csv
from datetime import datetime

def spend_points(amount, transactions):
    payer_points = {}
    ind = 0
    for i in range(0,len(transactions)):
        payer = transactions[i][0]
        points = transactions[i][1]
        
        if payer not in payer_points:
            payer_points[payer] = 0
        
        amount -= points
        
        if amount < 0:
            payer_points[payer] += abs(amount)
            ind = i
            break
        
        
        if amount == 0:
            ind = i
            break
    for i in range(ind+1,len(transactions)):
        payer = transactions[i][0]
        if payer not in payer_points:
            payer_points[payer] = 0
        payer_points[payer] += transactions[i][1]
            
    return payer_points

def read_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            payer = row[0]
            points = int(row[1])
            timestamp = datetime.strptime(row[2][1:-1], '%Y-%m-%dT%H:%M:%SZ')
            transactions.append((payer, points, timestamp))
    return sorted(transactions, key=lambda x: x[2])

if __name__ == '__main__':
    import sys
    
    amount = int(sys.argv[1])
    transactions = read_transactions_from_csv('transactions.csv')
    transactions.sort(key=lambda x: x[2])
    
    
    payer_points = spend_points(amount, transactions)
    print(payer_points)
