# Day 04
import numpy as np

bingo = np.array([6,69,28,50,36,84,49,13,48,90,1,33,71,0,94,59,53,58,60,96,30,34,29,91,11,41,77,95,17,80,85,93,7,9,74,89,18,25,26,8,87,38,68,5,12,43,27,46,62,73,16,55,22,4,65,76,54,52,83,10,21,67,15,47,45,40,35,66,79,51,75,39,64,24,37,72,3,44,82,32,78,63,57,2,86,31,19,92,14,97,20,56,88,81,70,61,42,99,23,98])

cards = np.genfromtxt('input.txt', skip_header=1)

num_cards = cards.shape[0]/5

card_list = np.arange(0,cards.shape[0],5)

for number in bingo:
    # for each bingo call, replace value with nan if matches
    cards[np.where(cards == number)] = np.nan

    for ii in card_list:
        card = cards[int(ii):int(ii)+5,:5]
            
        # check the rows and columns to see if the card has won bingo
        for jj in range(5):
            if sum(np.isnan(card[jj,:])) == 5 or sum(np.isnan(card[:,jj])) == 5:
                print("Bingo!")
                print(card)
                print("Winning bingo number is:", number)
                cardval = np.nansum(card)
                print(f"Solution is {cardval} * {number} = {cardval*number}")
                break

        else:
            continue
        break
    
    else:
        continue
    break


# Part 2
# Same as above, but without the breaks and modifying the cards to 'remove' them as they win

winningboards = []

cards = np.genfromtxt('input.txt', skip_header=1)

num_cards = cards.shape[0]/5

card_list = np.arange(0,cards.shape[0],5)

for number in bingo:
    # for each bingo call, replace value with nan if matches
    cards[np.where(cards == number)] = np.nan

    for ii in card_list:
        card = cards[int(ii):int(ii)+5,:5]
            
        # check the rows and columns to see if the card has won bingo
        for jj in range(5):
            if sum(np.isnan(card[jj,:])) == 5 or sum(np.isnan(card[:,jj])) == 5:
                print("Bingo!")
                print(card)
                print("Winning bingo number is:", number)
                cardval = np.nansum(card)
                print(f"Solution is {cardval} * {number} = {cardval*number}")
                
                # if the card wins, set it all equal to -1! 
                cards[int(ii):int(ii)+5,:5] = -1
                break

        else:
            continue
