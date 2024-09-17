
class service:
    def __init__(self, serviceName="", CarModel="", Description_C="", Description_A="", expense=0, Root=None):
        self.next = None  #properties for service object
        self.serviceName = serviceName
        self.CarModel = CarModel
        self.Description_C = Description_C
        self.Description_A = Description_A
        self.exprnse = expense
        self.subserves = []
        self.root = None



def add_service(new_serv_name, CarModel, Description_C, Description_A, expense): #add service method
    service_list.append(service(serviceName=new_serv_name,CarModel= CarModel,
                                Description_C=Description_C,Description_A=Description_A, expense=expense))\

def add_subservice(sub_name, servname):
                                    #method for adding subservices. it suerveys all over the tree to find the service that we are looking for
    for i in service_list:
        if i.serviceName==servname:
            new_subserv=service(serviceName=sub_name)
            i.subserves.append(new_subserv)
            new_subserv.root=i
            break

        s=find_service(i,servname)

        if s!= None and s.serviceName==servname:


            newservice=service(serviceName=sub_name)
            s.subserves.append(newservice)



def find_service(main_service, wanted_service):
    if main_service.serviceName == wanted_service:
        return main_service

    for j in main_service.subserves:
            print()
            r= find_service(j, wanted_service)
            if r!=None :
                return r

    return None


service_list = []

def show_services():  #shows all services and subservices that we have
    for i in service_list:
        print(i.serviceName)
        show(i)

def show(serv):
    for j in serv.subserves:
            print(j.serviceName)
            r= show(j)
            if r!=None :
                return r

    return None

def show_subserves_fromserv(servname): # shoes subservices of one specific service we are looking for
    for i in service_list:
        if i.serviceName == servname:
            for j in i.subserves:
               print(j.serviceName)
            break


        s = find_service(i, servname)

        if s != None and s.serviceName == servname:
            for j in s.subserves:
                 print(j.serviceName)


