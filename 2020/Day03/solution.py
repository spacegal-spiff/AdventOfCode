import numpy as np

f = open('input.txt', 'r')

# part 1, tobogganing

# we're going to make a list of the input. 
# we're also going to replace the pesky comment symbols!

inp = []

for x in f:
    inp.append(x.strip('\n').replace('#','T'))

# now make the input an array for us to work with
forest = np.array(inp)

rowlen = len(forest[0])


# left for posterity - this doesn't work for steps down = 2!
def treecount(stepsright, stepsdown):
    you = 0

    treecounter = 0

    for ii, row in enumerate(forest):
        # determine value at right position in row below
        you += stepsright
        if you > (rowlen-1):
            you = you % rowlen

        if (ii+stepsdown) < len(forest):
            checkpoint = forest[ii+stepsdown][you]

            # print(checkpoint)
            
            if checkpoint == 'T':
                treecounter += 1

        else:
            pass
            #print("Escaped!")
    return treecounter

# part 2, check a whole lotta toboggan slopes

# have to make a better function
def treecountnew(right, down):
    you = 0
    stepsdown = down
    treecounter = 0

    while stepsdown < len(forest):
        # determine value at right position in row below
        you += right
        if you > (rowlen-1):
            you = you % rowlen

        checkpoint = forest[stepsdown][you]

            
        if checkpoint == 'T':
            treecounter += 1
        else:
            pass
        
        stepsdown += down 
    
    return treecounter

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

totaltrees = 1

for slope in slopes:
    trees = treecountnew(slope[0],slope[1])
    print(f"Right {slope[0]}, down {slope[1]}: ", trees, "trees")
    totaltrees *= trees

print("Product of all the trees encountered: ", totaltrees)
