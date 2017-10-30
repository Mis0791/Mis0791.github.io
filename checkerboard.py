def checkerboard(rows):
    for i in range(rows):
        if i % 2  == 0:
            print ("* ") * (rows/2)
        else: 
            print (" *") * (rows/2)
checkerboard(8)
