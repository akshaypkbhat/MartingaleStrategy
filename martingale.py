import random, sys
import matplotlib.pyplot as plt
import numpy as np


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

        if self.cash <= 0: return

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

def main():

    ITERATIONS = int(sys.argv[1])
    BETS = int(sys.argv[2])
    PRINCIPAL = int(sys.argv[3])
    STARTINGBET = int(sys.argv[4])

    wins, losses = 0, 0
    for i in range(ITERATIONS):
        m = MartingaleStrategy(PRINCIPAL, STARTINGBET)
        cash = []
        bets = []
        for i in range(BETS):
            m.bet()
            cash.append(m.cash)
            bets.append(i)
        if m.cash > m.principal:
            print(f'Gain of {m.cash - m.principal}')
            print(f'Last Bet: {m.betAmount}')
            wins += 1
        elif m.cash < m.principal:
            print(f'Loss of {m.cash - m.principal}')
            losses += 1
        else:
            print('Broke Even')
        
        plt.plot(bets, cash)

        

    print(f'wins: {wins} losses: {losses}')

    # Matplotlib #

    plt.xlabel("Bets")
    plt.ylabel("Cash")

    plt.xticks(np.arange(0, BETS, step=1))
    plt.yticks(np.arange(0, 2*PRINCIPAL, step=PRINCIPAL/10))

    plt.show()

main()
