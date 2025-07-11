import random
import matplotlib
import matplotlib.pyplot as plt
import time


# tracks how many times the player goes broke
broke_count = 0

def rolldice(): #random roll function for win & loss (50/50)
    roll = random.randint(1, 100)
    if roll <= 50:
        # print(roll, "You rolled too low, try again!")
        return False
    else:
        # print(roll, "You rolled right, you won!")
        return True

def dalembert(funds, initial_wager, wager_count, color,plot=False):
# Strategy that describes increasing wager one unit after loss and decreasing by one unit after win
    global da_busts
    global da_profits

    value = funds
    currentwager = 1

    units = 1
    wX = []
    wY = []

    while currentwager <= wager_count:
        if units < 1:
            units = 1  # Minimum wager is 1 unit

        wager = units * initial_wager

        if wager > value:
            wager = value  # Can't bet more than you have

        if rolldice():
            value += wager
            units -= 1  # Decrease wager by 1 unit after win
        else:
            value -= wager
            units += 1  # Increase wager by 1 unit after loss
            if value <= 0:
                da_busts += 1
                break

        wX.append(currentwager)
        wY.append(value)

        currentwager += 1
    if plot:
        plt.plot(wX, wY, color)

    if value > funds:
        da_profits += 1

    return value

def multiple_bettor(funds,initial_wager,wager_count):
# Betting strategy aid to help denote the best multiple for "doubling down"
    """
          funds : The initial amount of money the player has
          initial_wager : The starting wager amount
          wager_count : The maximum number of wagers to simulate
    """

    global multiple_busts
    global multiple_profits

    value = funds
    currentwager = 1
    wX = []
    vY = []

    previouswager = 'win'
    previouswageramount = initial_wager
    # print('Starting doubler_bettor with funds:' funds, 'initial wager' initial_wager)

    # Loop for specified number of wagers
    while currentwager <= wager_count:
        # Determines next wager based on the previous
        if previouswager == 'win':
            wager = initial_wager
        else:
            wager = previouswageramount * random_multiple

        # Ensures wager does not exceed available funds
        # If the calculated wager is more than left, bet all remaining funds
        if wager > value:
            wager = value

            # print(f"Adjusting wager to remaining funds: {wager} (was higher)")
            # If funds are zero or less, we cannot make any more wagers
            if value <= 0:
                # print(f"Funds are zero or less. Cannot place wager {currentwager}. Broke.")
                multiple_busts += 1
                break  # Exit the loop when broke

        # Dice roll
        if rolldice():
            value += wager  # player wins, + wager to funds
            previouswager = 'win'
            previouswageramount = wager
            # print(f"Wager {currentwager}: WIN (+{wager}). New funds: {value}")
        else:
            value -= wager  # player loses, - wager from funds
            previouswager = 'loss'
            previouswageramount = wager
            # print(f"Wager {currentwager}: LOSS (-{wager}). New funds: {value}")

        # Records the current state for plot
        wX.append(currentwager)
        vY.append(value)

        # Double check if the player went broke after this wager
        if value <= 0:
            # print(f"We went broke after {currentwager} bets (funds: {value})")
            multiple_busts += 1
            break  # Exit the loop when broke

        currentwager += 1  # moves to next wager

    # print(f"Final funds after {currentwager - 1} bets: {value}")
    # Plot the results
    #plt.plot(wX, vY, color)
    if value > funds:
        multiple_profits += 1


def doubler_bettor(funds, initial_wager, wager_count, color):
#Method mimics the Martingale strategy of doubling down after a loss.
    value = funds
    currentwager = 1
    global doubler_busts
    global doubler_profits
    wX = [] # List to store wager counts for plot
    vY = [] # List to store fund values for plot

    previouswager = 'win' # Track of outcome of the previous wager
    previouswageramount = initial_wager # Tracks the amount of the previous wager

    # print(f"Starting doubler_bettor with funds: {funds}, initial wager: {initial_wager}")

    # Loop specified number of wagers
    while currentwager <= wager_count:
        # next wager based on the previous outcome
        if previouswager == 'win':
            wager = initial_wager
        else:
            wager = previouswageramount * 2


        # Ensure wager does not exceed available funds
        # If the calculated wager is more than what's left, bet all remaining funds.
        if wager > value:
            wager = value

            # print(f"Adjusting wager to remaining funds: {wager} (was higher)")
            # If funds are zero or less, cannot make any more wagers
            if value <= 0:
                # print(f"Funds are zero or less. Cannot place wager {currentwager}. Broke.")
                doubler_busts += 1
                break  # Exit the loop, player is broke

        # dice roll
        if rolldice():
            value += wager # Player wins, + wager to funds
            previouswager = 'win'
            previouswageramount = wager
            # print(f"Wager {currentwager}: WIN (+{wager}). New funds: {value}")
        else:
            value -= wager # Player loses, -  wager from funds
            previouswager = 'loss'
            previouswageramount = wager
            # print(f"Wager {currentwager}: LOSS (-{wager}). New funds: {value}")

        # current state for plotting
        wX.append(currentwager)
        vY.append(value)

        # Check if the player went broke after this wager
        if value <= 0:
            # print(f"We went broke after {currentwager} bets (funds: {value})")
            doubler_busts += 1
            break # Exit the loop if broke

        currentwager += 1 # Move to next wager

    # print(f"Final funds after {currentwager - 1} bets: {value}")
    # Plot results
    plt.plot(wX, vY, color)
    if value > funds:
        doubler_profits += 1

def simple_bettor(funds, initial_wager, wager_count,color):
#Simulates a simple betting strategy where the wager remains constant.
#The player can only wager what they have left, not into negatives.

    value = funds
    wager = initial_wager
    global simple_busts
    global simple_profits
    wX = []
    vY = []

    currentwager = 1

    # print(f"Starting simple_bettor with funds: {funds}, initial wager: {initial_wager}")

    while currentwager <= wager_count:
        # Ensure the wager does not exceed the available funds for simple bettor too
        if wager > value:
            wager = value
            # print(f"Adjusting simple wager to remaining funds: {wager} (was higher)")

        # If funds are zero or less, we cannot make any more wagers
        if value <= 0:
            # print(f"Funds are zero or less. Cannot place wager {currentwager}. Broke.")
            simple_busts += 1
            break # Exit the loop as the player is broke

        if rolldice():
            value += wager
            # print(f"Wager {currentwager}: WIN (+{wager}). New funds: {value}")
        else:
            value -= wager
            # print(f"Wager {currentwager}: LOSS (-{wager}). New funds: {value}")

        wX.append(currentwager)
        vY.append(value)

        # Check if the player went broke after this wager
        if value <= 0:
            # print(f"We went broke after {currentwager} bets (funds: {value})")
            simple_busts += 1
            break # Exit the loop if broke

        currentwager += 1

    # print(f"Final funds after {currentwager - 1} bets: {value}")

    #plot results
    plt.plot(wX, vY,color)
    if value > funds:
        simple_profits += 1

# comparison
lower_bust = 31.235
higher_profit = 63.208
# working with our other functions
samplesize = 1000
startfundings = 10000

#our while function for graping results in any of betting strategies (most currently d'alembert)
while True:
    #wagersize = 100
    #wagercount = 100000
    wagersize = random.uniform(1.0,1000.00)
    wagercount = random.uniform(10.0,10000.00)

    #setting variables
    ret = 0.0
    da_profits = 0.0
    da_busts = 0.0
    dasampsize = 10000
    counter = 1

    # How did we make out, defining our important measures
    while counter <= dasampsize:
        ret += dalembert(startfundings,wagersize,wagercount, 'b')
        counter += 1
    ROI = ret - (dasampsize*startfundings)
    totalinvested = dasampsize*startfundings
    percentROI = (ROI/totalinvested) * 100.00
    wagersizepercentage = (wagersize/startfundings)*100.00

# Want to get about 20 of these results for graphing, saves to CSV file for graphing purposes
# Show us the important stuff (greater than a 1% change either way)
    if percentROI > 1:

        print('____________________________')
        print('Total invested:', dasampsize*startfundings)
        print('Total Return:', ret)
        print('Percent ROI:', percentROI)
        print('ROI', ret - (dasampsize*startfundings))
        print('Bust Rate:',(da_busts/dasampsize)*100.00)
        print('Profit Rate:', (da_profits/dasampsize)*100.00)
        print('wager size:', wagersize)
        print('wager count:', wagercount)
        print('wager size percentage:', wagersizepercentage)

        savefile = open('monteCarloLiberal.csv','a')
        saveLine = '\n'+str(percentROI)+','+str(wagersizepercentage)+','+ str(wagercount)+',g'
        savefile.write(saveLine)
        savefile.close()
    elif percentROI < -1:
        print('____________________________')
        print('Total invested:', dasampsize * startfundings)
        print('Total Return:', ret)
        print('Percent ROI:', percentROI)
        print('ROI', ret - (dasampsize * startfundings))
        print('Bust Rate:', (da_busts / dasampsize) * 100.00)
        print('Profit Rate:', (da_profits / dasampsize) * 100.00)
        print('wager size:', wagersize)
        print('wager count:', wagercount)
        print('wager size percentage:', wagersizepercentage)

        savefile = open('monteCarloLiberal.csv', 'a')
        saveLine = '\n' + str(percentROI) + ',' + str(wagersizepercentage) + ',' + str(wagercount) + ',r'
        savefile.write(saveLine)
        savefile.close()





# Main simulation loop for determining good multiple_better outcome

'''while True:
    multiple_busts = 0.0
    multiple_profits = 0.0

    multiplesampsize = 100000
    currentsample = 1

    random_multiple = random.uniform(0.1,10.0)

    while currentsample <= multiplesampsize:
        multiple_bettor(startfundings,wagersize,wagercount)
        currentsample += 1

    if ((multiple_busts/multiplesampsize) * 100.00) < lower_bust and ((multiple_profits/multiplesampsize)*100.00) > higher_profit:
        print('#################################')
        print('Found a winner, the multiple was:', random_multiple)
        print('Lower bust to beat:', lower_bust)
        print('Higher profit to beat:', higher_profit)
        print('bust rate:', (multiple_busts/multiplesampsize)*100.00)
        print('profit rate:', (multiple_profits/multiplesampsize)*100.00)
    else:
        
        print('#################################')
        print('Found a loser, the multiple was:', random_multiple)
        print('Lower bust to beat:', lower_bust)
        print('Higher profit to beat:', higher_profit)
        print('bust rate:', (multiple_busts / multiplesampsize) * 100.00)
        print('profit rate:', (multiple_profits / multiplesampsize) * 100.00)
    plt.figure(figsize=(12, 7))'''


