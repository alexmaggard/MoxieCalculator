#Moxie Calculator
#Created By Alexander Maggard
#Use program to find estimated completion date for a project

#METHOD FOR ESTIMATING PROJECT COMPLETION TIME
def timeEstimator():
    print("Enter the following to get estimated completion time.")
    print("")
    totalCtn = int(input("How many total cartons are in the order? "))
    unitPerCtn = int(input("How many units per carton? "))
    finishCtn = int(input("How many cartons are currently finished? "))
    ctnPer15 = int(input("How many cartons are you finishing in a 15 minute period? "))
    #calculate
    totalUnits = totalCtn * unitPerCtn
    totalCtn = totalCtn - finishCtn
    totalUnits = totalUnits - (finishCtn*unitPerCtn)
    ctnPerDay = ctnPer15 * 8 * 4
    forecast = totalCtn/ctnPerDay
    forecast += .50 #add half-day variable for unexpected stalls
    #format decimal
    #display statements
    print("")
    print("Total Cartons Remaining: " + str(totalCtn))
    print("Days Until Completion: " + "%.2f" % (forecast))
    print("Total Units Remaining: " + str(totalUnits))
    print("")
    main()

#METHOD FOR CALCULATING MAX BOX HEIGHT and CUBE
def cube():
    pallet = 5
    boxH = int(input("Enter Box Height: "))
    maxLevels = int(input("Determine Max Levels: "))

    count = 0
    while (count < maxLevels):
        count = count + 1
        palletH = boxH*count+pallet
        
        print(str(count) + " Levels = " + str(palletH) + "inches")

    width = 40
    length = 48
    height = float(input("Enter Pallet Height used: "))
    cube = (length*width*height)/1728
    print("%.2f" % cube +" ft cube")
        
    main()

def main():
    print("")
    print("Enter time for Time Estimates")
    print("Enter cube for Max Height and Cube")
    print("Enter pallet for pallet/ctn count")
    print("Enter weight for total weight")
    userInput = input("Function: ")
    if(userInput == "time"):
        timeEstimator()
    elif(userInput == "cube"):
        cube()
    elif(userInput == "pallet"):
        pallet()
    elif(userInput == "weight"):
        totalWeight()
    else:
        print("You need to enter a valid function.")
        main()

#Calculate carton and pallet count
def pallet():
    print("")
    menOrWomen = input("Type m or w for men or women: ")
    if(menOrWomen == "m" or menOrWomen == "M" or menOrWomen == "men"):
        men()
    elif(menOrWomen == "w" or menOrWomen == "W" or menOrWomen == "women"):
        women()
    else:
        print("Please enter a valid entry.")
        pallet()

def men():
    colors = int(input("How many colors in this order?: "))
    unitMD = int(input("How many medium units?: "))
    base = int(input("How many cartons on the base?: "))
    height = int(input("How many levels high?: "))

    totalCtn = unitMD
    ctnPerPallet = base*height
    totalPallets = totalCtn/ctnPerPallet

    print("\n"+"Total Cartons: " + str(totalCtn))
    print("Cartons Per Pallet: " + str(ctnPerPallet))
    print("Total Pallets: " + "%.2f" % totalPallets)
    main()

def women():
    colors = int(input("How many colors in this order?: "))
    unitSM = int(input("How many small units?: "))
    base = int(input("How many cartons on the base?: "))
    height = int(input("How many levels high?: "))

    totalCtn = unitSM
    ctnPerPallet = base*height
    totalPallets = totalCtn/ctnPerPallet

    print("\n"+"Total Cartons: " + str(totalCtn))
    print("Cartons Per Pallet: " + str(ctnPerPallet))
    print("Total Pallets: " + "%.2f" % totalPallets)
    main()

#calculate total weight
def totalWeight():
    cartonWeight = float(input("Weight of single carton: "))
    amount = int(input("How many cartons?: "))
    pallet = 30
    palletCount = int(input("Total Pallets: "))

    totalWeight = ((cartonWeight * amount) + (pallet * palletCount))
    print("Total Weight: " + str(totalWeight))
    main()

main()





