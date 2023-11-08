#Billy Boone
#This reads in the sports data using InStream.  Produces 3 filtered output files (3 instances of OutStream)
#The 1st file filters are all NBA teams all-time W/L %. The second file filters all NBA teams total championship wins. 
#The third file displays a bar graph of each teams W/L % and total championships. 


import sys
import stdarray
import stddraw
from instream import InStream
from outstream import OutStream


#-----------------------------------------------------------------------

# Accept string fileName from command-line
# filter and output to 3 files

DELIM = ','

fileName = sys.argv[1]

# Create the input stream.
inStream = InStream(fileName)

# Create output streams.
outStream1 = OutStream(fileName + 'wlp.txt')
outStream2 = OutStream(fileName + 'chips.txt')

header = inStream.readLine()

NBA_teams = []
championships = []


# Read lines from the input stream and filter the data.
while inStream.hasNextLine():
    line = inStream.readLine()
    fields = line.split(DELIM)

    # Parse the data and store it in appropriate lists.
    franchise = fields[0]
    wlp = float(fields[8])
    chips = int(fields[12])

    # Add the team to the list of teams.
    NBA_teams.append(franchise)
    championships.append(chips)
    
    #write to output files
    format_wlp = f"{franchise}: {wlp}"
    format_chips = f"{franchise}: {chips}"
    outStream1.writeln(format_wlp)
    outStream2.writeln(format_chips)





# Create a bar chart using stddraw.
stddraw.setXscale(-1, len(NBA_teams))
stddraw.setYscale(-5, max(championships) + 10)

# Display team names vertically above the bars

for i, team in enumerate(NBA_teams):
    team_name = team.split()[0]
    team_name_length = len(team_name)
    # Display team names vertically above the bars, going up the y-axis
    for j, char in enumerate(team_name):
        stddraw.text(i, championships[i] + 3 + j, char)
    stddraw.text(i, championships[i] + 1, str(championships[i]))
    stddraw.filledRectangle(i, 0, 0.6, championships[i])
stddraw.show()

#python sportsfilter.py sportsdata.csv






