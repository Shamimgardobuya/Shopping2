print("This is Mama Kila's shop")

shelf={"Pkts of Milk":90,"Bread":75,"1kg Omo":30,"1kgJembe":45}

# price_shelf={"1pkt of Milk":50,"Bread":50,"1kg Omo":30,"1kgJembe":150}
print(f"Mama Kila has these items in her shelf {shelf}")
# print("1pkt of Milk is  @50,Bread is @50 ,1kg Omo is @30,1kgJembe is @150")
cart=[]

def shop():
    # choices=input("Do you wish to add another item? ")
    # if choices
    choice=input("What Item do you wish to buy? ")
   
    if  choice in shelf.keys():     #instead of inputting values for milk and  bread or jembe,or omo  
        cart.append(choice)
        print(cart)
        
        # checkout()   #what does checkout do  #checkout will make all the lines of code performed
        # for item in cart:
    # elif choice=="nothing" or "no":
       
    else:
        print("sorry the item does not exist")

    # print(cart)
shop()

def checkout():  
    # p=checkout()
    # print("hello")
    if len(cart)>0:
        answer=input(f"you have {len(cart)} Items in your cart. Proceed To checkout(Yes or No)?")
        if answer =='Yes' or "yes" "YES":
            requesting=int(input("How many would you like to buy? "))
            for item in cart:       # looping through the item of the cart
                price=shelf[item]*requesting #sHELF[item] represents value in a dictionary ,its like shelf ['Bread']    #
                cart2={}
                cart2[item]=price
            print(f"The total cost is {price}")
            shop()        

        else: 
                for i in cart2.values():
                        v=0
                        v+=i
                        i+=1
                        print(f"Your total price is sh{v}")  
checkout()                        
                                            #also want the number of price to be added.
 #commenting because don't  want them to have option
 #            # shop()                  # final list to contain the items ,values appended to pricing
            # checkout() 
            #
                                                             #         #Request for users input for number,and print is as price
                    # print(f"The total cost is {price} and your cart is {cart}")                #call the first function if user wants to buy another if not,create dictionary for item and price






                                                                                                                                                                        # def checkout():  
                                                                                                                                                                        #     p=checkout()
                                                                                                                                                                        #     # print("hello")
                                                                                                                                                                        #     if len(cart)>0:
                                                                                                                                                                        #         answer=input(f"you have {len(cart)} Items in your cart. Proceed To checkout(Yes or No)?")
                                                                                                                                                                        #         if answer =='Yes' or "yes" "YES":
                                                                                                                                                                        #             requesting=int(input("How many would you like to buy? "))
                                                                                                                                                                        #             for item in cart:       # looping through the item of the cart
                                                                                                                                                                        #                 price=shelf[item]*requesting #sHELF[item] represents value in a dictionary ,its like shelf ['Bread']    #
                                                                                                                                                                        #             print(f"The total cost is {price}")
                                                                                                                                                                        #             shop()

                                                                                                                                                                        #         elif answer=='No':        #also want the number of price to be added.
                                                                                                                                                                        #  #commenting because don't  want them to have option
                                                                                                                                                                        #  #            # shop()                  # final list to contain the items ,values appended to pricing
                                                                                                                                                                        #             # checkout() 
                                                                                                                                                                        #             #        #Request for users input for number,and print is as price
                                                                                                                                                                        #             print(f"The total cost is {price}")                #call the first function if user wants to buy another if not,create dictionary for item and price

                                                                                                                                                                        # checkout()

                                                                                                                                                                        # print("You can also remove the item you bought,if it doesn't suit you.")
                                                                                                                                                                        # price=list(shelf.values())t 

                                                                                                                                                                        #let me try plaing function inside function