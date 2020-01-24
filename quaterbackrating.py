# Running the program will print all of the qb's and their ratings.
def qbrating(cy, ya, ty, i, td, qb_name):
    eqn = (((((cy/ya)*100)-30)*0.05)+(((ty/ya)-3)*0.25)+((((td/ya)*100))*0.2)+(2.375-((i/ya)*100)*0.25))/6
    rating = eqn * 100
    print(f"{qb_name}'s rating is {round(rating, 2)}")

if __name__ == "__main__":
    qbrating(4967,8358,61361,252,420,"Dan Marino")
    qbrating(1166,1869,14219,42,87,"Jared Goff")
    qbrating(1278,2356,15315,73,77,"Tony Banks")
    qbrating(1855,2967,19449,61,103,"Sam Bradford")
    qbrating(1969,3171,22814,93,122,"Marc Bulger")
    qbrating(2666,4070,32344,128,208,"Kurt Warner")