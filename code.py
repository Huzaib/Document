import csv
with open('train.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    with open('submissions.csv', 'w')as new_file:
        f=1

        csv_writer=csv.writer(new_file)
        while f==1:
            g=0
            u = input("Enter \n")
            h=u.lower()
            if h=="quit":
                break


            for line in csv_reader:
                s=line[0]
                if s==u:
                    csv_writer.writerow([line[0], line[13]])
                    g=1
                    break
            if g==0:
                csv_writer.writerow([u, 'Nil'])










