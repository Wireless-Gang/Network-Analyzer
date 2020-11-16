import datetime
def main():

    a_file = open("testData.txt", "r")

    list_of_lists = []
    uniqueIP = []

    #each line in test data is separated into an array of


    #line1 totalPackets
    #every other line follows as:
    #array[0] = packet #, array[1] = ip#1, array[2] = ip#2
    for line in a_file:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      list_of_lists.append(line_list)

    a_file.close()

    #loop checks for ip uniqueness
    for listLine in list_of_lists:
        #skips over first line of testData file that displays num of packets
        if len(listLine) > 1:
            if listLine[1] not in uniqueIP:
                uniqueIP.append(listLine[1])
            if listLine[2] not in uniqueIP:
                uniqueIP.append(listLine[2])


    b_file = open("output.txt", "r")

    list_of_speed_data = []
    totalBytes = 0
    totalTime = 0.0
    totalTimeUnits =""
    totalSpeed = 0

#Format for output.txt
#
#===================================
#| IO Statistics                   |
#|                                 |
#| Duration: 50.3 secs             | time at [4][2] units at [4][3]
#| Interval: 50.3 secs             |
#|                                 |
#| Col 1: Frames and bytes         |
#|---------------------------------|
#|              |1                 |
#| Interval     | Frames |  Bytes  |
#|---------------------------------|
#|  0.0 <> 50.3 |   6858 | 5318225 | bytes at [12][7]
#===================================


    for line in b_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_speed_data.append(line_list)
    b_file.close()

    totalTime = list_of_speed_data[4][2] 
    totalTime = float(totalTime) #converting str into float
    totalBytes = list_of_speed_data[12][7]
    totalBytes = int(totalBytes) #converting str into int

    totalSpeed = totalBytes/totalTime
    totalSpeed = totalSpeed/1000000 #converting to mbps


    open('results.txt', 'w').close() #this clears the file of previous data before appending more data to it
    c_file = open("results.txt", "a")

    time = datetime.datetime.now()
    c_file.write("Current date and time : ")
    c_file.write(time.strftime("%m-%d-%Y, %H:%M:%S"))
    c_file.write('\n')
    c_file.write("Duration: ")
    c_file.write('%d' % totalTime)
    c_file.write(" seconds\n")
    c_file.write("Bytes: ")
    c_file.write('%d' % totalBytes)
    c_file.write('\n')
    c_file.write("Speed: ")
    c_file.write('%f' % totalSpeed)
    c_file.write(" Megabytes per second\n")
    c_file.write("There are ")
    c_file.write('%d' % len(uniqueIP))
    c_file.write(" unique IP values: ")
    c_file.write("\n")
    c_file.write('%s' % uniqueIP)
    c_file.write("\n")
    
    c_file.close

    del uniqueIP[:]

if __name__ == '__main__':
    main()