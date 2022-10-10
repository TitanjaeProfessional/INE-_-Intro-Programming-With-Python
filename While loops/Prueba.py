def compound_interest_result(initial_investment,interest_percentaje,num_periods):
    inicial=initial_investment
    percentaje=(1/(interest_percentaje))
    x=inicial*percentaje
    count=0
    if(num_periods == 0):
        return inicial
    elif (num_periods == 1):
        inicial+=inicial*percentaje
        return total
    elif (num_periods>1):
        inicial+=inicial*percentaje
        while count < num_periods-1:
            x+=x*percentaje
            inicial+=x
            count+=1
        return inicial

print(round(compound_interest_result(1000, 10, 5), 2))


def interestsum():
    inicial=1000
    x=inicial*.1
    count2=0
    inicial+=100
    while count2 < 2 - 1:
        x+=x*.1
        #print(x)
        inicial+=x
        #print(inicial)
        count2+=1
    return x

interestsum()