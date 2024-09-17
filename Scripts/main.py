class service:
    def __init__(self, serviceName="", CarModel="", Description_C="", Description_A="", expense=0):
        self.next=None
        self.servicename = serviceName
        self.CarModel = CarModel
        self.Description_C = Description_C
        self.Description_A = Description_A
        self.exprnse = expense
        self.subsrves = []

class LinkedList:
    def __init__(self):
        self.head = None

    def add_service(self, new_serv_name,CarModel, Description_C, Description_A, expense):
        new_serv= service(new_serv_name,CarModel,Description_C,Description_A,expense)
        new_serv.next = self.head
        self.head = new_serv

    def add_subservice(self, new_sub_name , servname):
        new_sub=service(serviceName=new_sub_name)
        self.search('badane')

    def search(self, x):

        current = self.head

        while current != None:
            if current.data == x:
                print(x)
                return True

            current = current.next

        return False



if __name__ == '__main__':

    llist = LinkedList()


    llist.add_service('badane','benz','tozihe moshtari','tozihe agency',1000)
    llist.add_subservice('safkari','badane')