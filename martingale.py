import random

class MartingaleStrategy():
    
    def __init__(self, principal, startingBet):
        self.principal = principal
        self.cash = self.principal
        self.STARTINGBET = startingBet
        self.betAmount = self.STARTINGBET
        
        self.win = 0.5
        self.bets = 0
        self.LAST_BET = True

    def bet(self):

        self.bets += 1
        r = random.randint(0, 1)
        
        if (r == 0):
            
            self.cash += self.betAmount * self.win
            self.betAmount = self.STARTINGBET
            self.LAST_BET = True
        
        else:

            self.cash -= self.betAmount * self.win
            self.betAmount *= 2
            self.LAST_BET = False

        print(f' Bet: {self.bets} Cash: {self.cash} LAST_BET {self.LAST_BET} Bet Amount: {self.betAmount}')

wins, losses = 0, 0
for i in range(1000):
    m = MartingaleStrategy(10_000, 1_000)
    for i in range(10):
        m.bet()
    if m.cash > m.principal:
        print(f'Gain of {m.cash - m.principal}')
        print(f'Last Bet: {m.betAmount}')
        wins += 1
    elif m.cash < m.principal:
        print(f'Loss of {m.cash - m.principal}')
        losses += 1
    else:
        print('Broke Even')

print(f'wins: {wins} losses: {losses}')