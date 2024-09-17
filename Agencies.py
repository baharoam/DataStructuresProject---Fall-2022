import Customer
import Manager


class Agency :
    def __init__(self, name):
        self.name = name
        self.next = None
        self.services=[]
        self.PriorityQueue=Customer.MaxHeap(100)


class LinkedList: #linked list for
    def __init__(self):
        self.head = None

    def add_agency(self, newData): #adding a new agency in the linked list we created
        newAgency = Agency(name=newData)
        newAgency.next = self.head
        self.head = newAgency


    def show_list_agencies(self): #shows all the agenicies in the linked list
        t = self.head
        while t != None:
            print(t.name),
            t = t.next
    def add_offer(self,x,servicename):
        current = self.head

        while current != None: #looks for a wanted agency to add an offer in services list
            if current.name == x:
                current.services.append(servicename)

            current = current.next


    def delete_offer(self,x,servicename):
        current = self.head

        while current != None:
            if current.name == x:
                current.services.remove(servicename)

            current = current.next



    def search(self, x):

        current = self.head

        while current != None:
            if current.name == x:
                return current

            current = current.next

        print("Not found")

agency_list= LinkedList()
def menu_addoffer(str8,str9):
    agency_list.add_offer(str8,str9)


def menu_deleteoffer(str10, str11):
    agency_list.delete_offer(str10, str11)
def menu_add_agency(str12):
    agency_list.add_agency(str12)

def menu_show_agency():
    agency_list.show_list_agencies()

def get_order(serv,agenc,imm,time,customer):
    main_agent=agency_list.search(agenc)
    o=Customer.Order(serv,imm,time,customer)
    main_agent.PriorityQueue.insert(o)

def show_orders(agenc):
    agency=agency_list.search(agenc)

    print("popped",agency.PriorityQueue.extractMax().ordername)
    agency.PriorityQueue.Print()









