import csv

def display(fileName,fields):
    with open(fileName,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            for i in fields:
                if i in row:
                    print(row[i])
                else:
                    print(f"Field '{i}' not found in the CSV file.")

def insert(fileName,entered):
    with open(fileName,'a') as f:
        writer=csv.DictWriter(f,fieldnames=entered.keys())
        if f.tell()==0:         # Check if file is empty, write header if so
            writer.writeheader()
        writer.writerow(entered)
        print("Data inserted successfully.")
        

def deleteFields(fileName,delete):
    rows=[]
    with open(fileName,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            new_row={}
            for i,j in row.items():
                if i not in delete:
                    new_row[i]=j
            rows.append(new_row)
    with open(fileName,'w') as f:
        writer=csv.DictWriter(f,fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(F"Fields {delete} deleted successfully.")

def deleteRecord(fileName,id):
    rows=[]
    with open(fileName,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['id']!=id:
                rows.append(row)
            else:
                print(f"Record deleted with id {id} successfully.")
    with open(fileName,'w') as f:
        writer=csv.DictWriter(f,fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

fileName="data.csv"
available=['id','name','age','department','year']
while True:
    print("Options menu:")
    print("1.Display data")
    print("2.Insert data")
    print("3.Delete fields")
    print("4.Delete record(ROW)")
    print("5.Exit")
    ch=input("Enter choice (1/2/3/4/5) : ")
    if ch=='1':
        print(f"Available fields are : {', '.join(available)}")
        fields=input("Enter the fields you want to display separated by comma : ").strip().split(',')
        display(fileName,fields)
    elif ch=='2':
        newData={}
        print("Insert new data.")
        for i in available:
            newData[i]=input(f"Enter {i} : ")
        insert(fileName,newData)
    elif ch=='3':
        print(f"Available fields are : {', '.join(available)}")
        delete=input("Enter the fields you want to delete separated by comma : ").strip().split(',')
        deleteFields(fileName,delete)
    elif ch=='4':
        id=input("Enter the id of the record you want to delete : ")
        deleteRecord(fileName,id)
    elif ch=='5':
        print("Bye!")
        exit()
    else:
        print("Invalid choice!")