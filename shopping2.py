# from tkinter import W


print("This is Mama Kila's shop")

# shelf={"Pkts of Milk":90,"Bread":75,"1kg Omo":30,"1kgJembe":45}
shelf={"Milk":5,"Bread":10,"Omo":3}


print(f"Mama Kila has these items in her shelf {shelf}")
cart=[]

def shop():
   
    choice=input("What Item do you wish to buy? ")
    
   
    if  choice in shelf.keys():     #instead of inputting values for milk and  bread or jembe,or omo  
        cart.append(choice)
        print(cart)
        print("hello")
        
       
       
    else:
        print("sorry the item does not exist")
shop()



def checkout(): 
    # cart2={}
    if len(cart)>0:
        requesting=int(input("How many would you like to buy? ")) 
        answe=(str(input(f"you have {len(cart)} Items in your cart. Proceed To checkout(Yes or No)? "))).lower()
        if answe =='yes' :
        
            def pricing():
                print(cart)
                tot=0
                for item in cart:
                    price=shelf[item]*requesting
                    tot+=price
                print(f"{tot} is your total price")
            pricing()
                #break
                    # break

            



                  
            #   /checkout()
        elif answe =='no':
            shop()
            checkout()
            # print(price)
             
        else:
            print("invalid Option for buying")
        # checkout()
            
checkout()                        
                                       



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