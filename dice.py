import random
import matplotlib.pyplot as plt

def ev_max(n:int)-> float:
    '''# Returns the expected minimum value of the dice given a specified number of rolls (n)
    '''
    return 100*(n/(n+1))

def ev_min(n:int)-> float:
    '''# Returns the expected maximum value of the dice given a specified number of rolls (n)
    '''
    return 100/(n+1)

def monte_carlo(trials:int=100,rolls:int=1)-> list:
    """# The `Monte Carlo` function is conducting a simulation to estimate the expected
    # value (EV) of rolling a D100 dice. It rolls the dice a specified number of times for a
    # specified number of trials. For each trial, it calculates the maximum value obtained from the
    # rolls and accumulates these maximum values. It then calculates the average maximum value
    # across all trials to estimate the expected value. The function returns the final estimated
    # expected value and a list of all previous expected values calculated during the simulation.

    Args:
        trials (int, optional): [Number of trials to be conducted]. Defaults to 100.
        rolls (int, optional): [Number of rolls of the D100 per trial]. Defaults to 1.

    Returns:
        list: [A list containing the final EV value as the first element, and a list of all previous EV values as the second element]
    """    
    total_max=0
    n=rolls
    all_evs=[]
    for t in range(1,trials+1):
        trial_max=0
        for _ in range(rolls):
            roll_max=max(random.randint(1,100) for _ in range(n))
            trial_max+=roll_max
        total_max+=trial_max
        if t%(trials//100)==0:
            ev=total_max/(trials*rolls)
            percent=t / trials
            all_evs.append(ev)
            print(f"Progress: {percent * 100:3.0f}%    Current EV: {ev:.3f}")
    return ev,all_evs

trials=int(input("Enter the number of trials to be conducted: "))
rolls=int(input("Enter the number of rolls of the D100 dice: "))
print(f'Theoretical Maximum EV value: {ev_max(rolls)}\nTheoretical Minimum EV value: {ev_min(rolls)}')
final_ev,evs=monte_carlo(trials,rolls)
print(f'Monte Carlo Max EV: {final_ev}')

def plot_evs(trials,evs,rolls):
    plt.figure(figsize=(10,6))
    plt.plot(range(0,trials,trials//100),evs,label="Observed")
    plt.axhline(y=ev_max(rolls),color="r",label="Theoretical Max")
    plt.axhline(y=ev_min(rolls),color='b',label="Theoretical Min")
    plt.legend()
    plt.grid=True
    plt.show()

#plot_evs(trials,evs,rolls)