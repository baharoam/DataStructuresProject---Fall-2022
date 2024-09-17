import Manager, Agencies,Customer
from datetime import datetime
print(""
      "Choose your command : \n"
      "1) add service \n"
      "2) add subdervice \n"
      "3)add offer to agency\n"
      "4) delete service from agency\n"
      "5)add agency\n"
      "6) show agency list\n"
      "7)show services list\n"
      "8)show subservices from specific service  \n"
      "9) order \n"
      "10) show order list \n"
      "11) to  exit \n")




if __name__=="__main__":

     while True:
           n=int(input())
           if n==1:  #for method 1
                 str1=input("write service name")
                 str2=input("write car model")
                 str3=input("write explications for customers")
                 str4=input("write explications for agents")
                 str5=input("write expenses")
                 Manager.add_service(str1,str2,str3,str4,str5)

           if n==2:  #for method 2
                 str6=input("write subservice name")
                 str7=input("write service name")
                 Manager.add_subservice(str6,str7)
           if n==3: #for method 3
                 str8=input("write agency name")
                 str9=input("write service name")
                 Agencies.menu_addoffer(str8,str9)

           if n==4: #for method 4
                 str10=input("write agency name")
                 str11=input("write service name")
                 Agencies.menu_deleteoffer(str10,str11)

           if n==5:  #for method 5
                 str12=input("write agency name")
                 Agencies.menu_add_agency(str12)
           if n==6:  #for method 6
                 Agencies.menu_show_agency()
           if n==7: #for method 7
                 Manager.show_services()
           if n==8:  #for method 8
                 str13=input("write service name ")
                 Manager.show_subserves_fromserv(str13)
           if n==9: #for method 9
                 customer=input("what is your name")
                 str14=input("write service name")
                 str15=input("write agency name")
                 str16=int(input("write Immediacy Level 1-> Normal 2-> demand 3-> necessary"))
                 now = datetime.now()
                 current_time = now.strftime("%H:%M:%S")
                 Agencies.get_order(str14,str15,str16,current_time,customer)
           if n==10:  #for method 10

                 str17=input("write the name of the agency you want to see the orders ")
                 Agencies.show_orders(str17)

           if n==11:
                 break

