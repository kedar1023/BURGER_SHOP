#Node Class Declared
class Node(object):

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

#Class Declared For Queue and enqueue and de-queue methods

class Queue(object):

    def __init__(self,front=None,rear=None):
        self.front = None
        self.rear = None

#En-queue declared for adding the Back

    def enqueue(self,data):
        NewNode = Node(data)

        if self.front==None and self.rear==None:
            self.front=self.rear=NewNode
            return

        temp = self.front
        c = 0
        max = NewNode.data
        while temp!=self.rear:
            if temp.data>max:
                current = temp
                c = c+1
                temp=temp.next    
                continue

            elif c == 0:
                NewNode.next=self.front
                self.front=NewNode
                print("New Customer Order Placed Successfully")
                return

            else:
                current.next=NewNode
                NewNode.next=temp
                print("New Customer Order Placed Successfully")
                return

        if self.front==self.rear:
            if self.front.data[1]>max:
                self.front.next=NewNode
                self.rear=NewNode
                print("New Customer Order Placed Successfully")
                return

            else:
                NewNode.next=self.front
                self.front=NewNode
                print("New Customer Order Placed Successfully")
                return

        if temp== self.rear:
            if temp.data[1]<max:
                current.next=NewNode
                NewNode.next=temp
                print("New Customer Order Placed Successfully")
                return

            elif self.rear.data >max:
                self.rear.next=NewNode
                self.rear=NewNode
                print("New Customer Order Placed Successfully")
                return

#De-queue method declared to delete from front

    def dequeue(self):
        current=self.front
        if self.front==None:
            print("No Customer")  #Queue Empty                   
            return

        if self.front==self.rear:
            self.front=self.rear=None
            print ("Customer Deleted Successfully")
        else:
            self.front=self.front.next
            print("Customer Deleted Successfully") 

#Method to display all customer and orders

    def display(self):
        front1 = self.front
        if ((front1==None) and (self.rear==None)):
            print("No Customers")
            return
        print("Customer Name ") 

        while(front1!=self.rear):
            print ("Customer Name",front1.data)
            front1 = front1.next

        
def main():
    try:

        while True:
            print("-")*50 
            print("Welcome To My Burger,Alandi")
            print("-")*50
            print("1.Create The Queue")
            print("2.Place Order")
            print("3.Delete Customer Info")
            print("4.Display Customer With Highest Priority")
            print("5.Exit")
            print("-")*50             

            choice = input("Enter Your Choice:")

            if choice==1:
                q = Queue()

            elif choice==2:
                customer_name=raw_input("Enter Your Name")
                c = 1
                while c==1:
                    if customer_name >1 and customer_name!=None:
                        customer_name=customer_name
                        break
                    

               

                q.enqueue(customer_name)
            elif choice==3:
                q.dequeue()

            elif choice==4:
                print("Display Customers in Queue")
                q.display()

            elif choice==5:
                print("Thank You Do visit again")
                break

    except Exception as e:
        print ("Invalid",e)

if __name__ == '__main__':
    main()
