#35*2=70; 94-70=24; 24/2=12 - rabbits; 35-12=23 - chickens
def puzzle(heads, legs):
    print('number of rabbits ' + str((legs-heads*2)/2))
    print('number of chickens ' + str(heads-(legs-heads*2)/2))

puzzle(35, 94)
