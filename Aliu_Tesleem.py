#!/usr/bin/env python
# coding: utf-8

# In[8]:


try:
    # define function that calculates the total amount of sales on each shift in a day
    def total_sales(morning_sales, evening_sales):
        '''
        Calculates the total amount of morning, evening and the daily sales. 
        Returns 3 variables which are floats. The function takes 2 arguments.
        args:
            morning_sales(list) : list of prices of items sold in the morning shift.
            evening_sales(list) : list of prices of items sold in the evening shift.
        '''

        total_morning_sales = sum(morning_sales) # summing the morning sales
        total_evening_sales = sum(evening_sales) # summing the evening sales
        total_day_sales = total_morning_sales + total_evening_sales # summing the total sales of the whole day
        return total_morning_sales, total_evening_sales, total_day_sales # return total sales for morning and evening shift and the whole day
    # define function that calculates the workers salary for each shift
    def worker_salary(hourly_rate, hours_worked):
        '''
        Calculates the salary of each worker based his or her hourly rate and hours worked.
        args:
            hourly_rate(float) : float that represents the amount a worker collects hourly
            hours_worked(float) : float that represents the hours a worker has worked
        float was used for the 'hours_worked' argument so as to cater for the minutes. In case a worker could not work a complete an hour of work, the minutes can be converted to    hours before inputting in the program.
        '''
        try:
            # calculating the salary of a worker with known hourly rate and hours worked
            salary = hourly_rate * hours_worked
            return salary
        # Error handling
        except:
            print('Incorrect input. Kindly check and re-enter.')
    
    # define function that calculates profit or loss for sales for each shift.
    def profit_loss(day_sales, day_cost):
        '''
        Calculates the profit or loss when based on the price a product was bought and how much it was sold.
        args:
            day_sales(list) : list of amounts different products were sold.
            day_cost(list) : list of amount different products were bought.
        '''
        # calculates proft or loss by subtracting the total price of amount items were bought from the total price items were sold
        profit_or_loss = sum(day_sales) - sum(day_cost)
        try:
            # creating a condition if the result is greater than 0
            if profit_or_loss > 0:
                print(f'\nProfit of \033[1m${profit_or_loss}\033[0m was made.\n')
            # creating a condition if the result is less than 0
            elif profit_or_loss < 0:
                print(f'\nLoss of \033[1m${profit_or_loss}\033[0m was made.\n')
            # creating a condition if the result is not greater or less 0
            else:
                print(f'\nNeither Profit nor Loss was made: \033[1m${abs(profit_or_loss)}\033[0m.\n')
        # handling errors
        except ValueError:
            print('Invalid input.')
        except ZeroDivisionError:
            print('Sorry can not divide by 0')
        except TypeError:
            print('Invalid type input.')
    
    # define function that calculates the tips for each shift
    def shift_tips(morning_sales,evening_sales):
        '''
        Calculates the tips for each both morning and evening shift which is 2% of the total sales per shift.
        args:
            morning_sales(list) : list of prices of items sold in morning shift
            evening_sales(list) : list of prices of items sold in evening shift
        '''
        try:
            # creating a condition for if the list 'morning_sales' is empty
            if not morning_sales:
                print('Morning sales data have not been inputted or No sales.')
            # creating a condition for if the list 'morning_sales' is not empty
            else:
                morning_tips = (2 / 100) * sum(morning_sales)
            # creating a condition for if the list 'evening_sales' is empty
            if not evening_sales:
                print('Evening sales data have not been inputted or No sales.')
            # creating a condition for if the list 'evening_sales is not empty'
            else:
                evening_tips = (2 / 100) * sum(evening_sales)
            # creating a condition for if both lists 'morning_sales' and 'evening_sales' are empty
            if not morning_sales and not evening_sales:
                print('No tips for the day. NO SALES!!!')
            # creating a condition for if both lists 'morning_sales' and 'evening_sales' are not empty
            else:
                daily_tips = (2 / 100) * (sum(morning_sales) + sum(morning_sales))
        # handling errors
        except ValueError:
            print('Invalid input.')
        except ZeroDivisionError:
            print('Sorry can not divide by 0')
        except TypeError:
            print('Invalid type input.')
        return morning_tips, evening_tips, daily_tips
            

    # function to run all the individual functions in loops.
    def auto_app():
        
        '''
        This function opens a loop that continuously prompts the user to input an option from a list of open menus. 
        There is the main menu and other submenus that run in a loop until an option is selected to exit the menu.
    
        Args:
            None

        Returns:
            None
        '''
        print('\033[1mSmartBooks Automation\033[0m \n')
        # creating empty list to hold the amount sold for each shift (morning and evening)
        morning_sales = []
        evening_sales = []

        # creating empty list and dictionary to hold workers hourly_rate and hours_worked information.
        list_of_workers_info = []
        workers_info = {}
        
        # creating empty list to hold the cost of items sold and
        daily_cost = []
        # creating a list to store morning and evening sales together
        daily_sales = []

        # initiating a while loop to prompt the user to give input option (1-6); where option 6 breaks the loop. This serve as the main menu
        while True:
            # saving the input of the user to a variable user_input
            user_input = input("1. Daily sales \n2. Worker's Salary \n3. Profit or loss\n"
                              "4. Tips for a shift \n5. Exit \nEnter option 1-5: ")
            # creating a condition for when the user chooses option1 in the main menu
            if user_input == '1':
                # initiating a while loop to prompt the user to give input option(1-4); where option 4 breaks the loop. This serve as menu for the Daily sales option.
                while True:
                    # saving the input of the user to a variable daily_sales_option
                    daily_sales_option = input('1. Input morning sales \n2. Input evening sales \n'
                                               '3. Get total sales\n4. Return to main menu \nEnter option 1-4: ')
                    # creating a condition for when the user chooses option1 in the 'Daily sales' menu
                    if daily_sales_option == '1':
                        # initiating a while loop to prompt the user to input the amount of morning shift sales
                        while True:
                            try:
                                # saving the morning shift sales input from the user to a variable morning_sales_input
                                morning_sales_input = input('Enter sales or enter "#" to proceed: ')

                                # creating a condition to break the loop when '#' is entered by the user
                                if morning_sales_input == '#':
                                    break
                                # appending the user input to the empty list 'morning_sales' created in the beginning of the function 
                                else:
                                    morning_sales.append(float(morning_sales_input))
                                    daily_sales = morning_sales + evening_sales
                            # creating an exception for ValueError
                            except ValueError:
                                print('Invalid input. Make another entry')
                                continue 
                    # creating a condition for when the user chooses option2 in the 'Daily sales' menu
                    elif daily_sales_option == '2':
                        # initiating a while loop to prompt the user to input the amount of evening shift sales
                        while True:
                            try:
                                # saving the morning shift sales input from the user to a variable evening_sales_input
                                evening_sales_input = input('Enter sales and enter "#" to proceed: ')

                                # creating a condition to break the loop when '#' is entered by the user
                                if evening_sales_input == '#':
                                    break
                                # appending the user input to the empty list 'evening_sales' created in the beginning of the function
                                else:
                                    evening_sales.append(float(evening_sales_input))
                                    daily_sales = morning_sales + evening_sales
                            # creating an exception for ValueError
                            except ValueError:
                                print('Invalid input. Make another entry')
                                continue
                    # creating a condition for when the user chooses option3 in the 'Daily sales' menu
                    elif daily_sales_option == '3':
                        # calling the total_sales function which returns 3 variables. 
                        total_sales_mor, total_sales_eve, total_sales_daily = total_sales(morning_sales, evening_sales)

                        # initiating a while loop to prompt the user to input an option in the 'daily_sales_option' menu
                        while True:
                            # storing the user input in a variable 'result_view'
                            result_view = input('1. View total morning sales \n2. View total evening sales \n'
                                                '3. View total sales for the day \n4. Return to previous menu \nEnter option 1-4: ')
                            # creating a condition when the user choose option1 in the 'Get total sales' menu
                            if result_view == '1':
                                # printing the total amount sold in the morning shift in bold
                                print(f'The total sales for morning shift is: \033[1mN{total_sales_mor}\033[0m')# the code; \033[1mN  \033[0m, is responsible for making 'total_sales_mor' bold when printing
                                break
                            # creating a condition when the user choose option2 in the 'Get total sales' menu
                            elif result_view == '2':
                                # printing the total amount sold in the evening shift in bold
                                print(f'The total sales for evening shift is: \033[1mN{total_sales_eve}\033[0m')# the code; \033[1mN  \033[0m, is responsible for making 'total_sales_eve' bold when printing
                                break
                            # creating a condition when the user choose option3 in the 'Get total sales' menu
                            elif result_view == '3':
                                # printing the total amount sold that day in bold
                                print(f'The total sales for the day is: \033[1mN{total_sales_daily}\033[0m')# the code; \033[1mN  \033[0m, is responsible for making 'total_sales_daily' bold when printing
                                break
                            # condition to break the loop and return to the previous menu(loop)
                            elif result_view == '4':
                                break
                            # condition to tell the user to choose the correct option when an invalid option has been entered
                            else:
                                print('\nInvalid choice. Choose between option 1-4.\n')
                    # creating the condition when the user chooses option 4 in the 'Daily sales' menu
                    elif daily_sales_option == '4':
                        break
                    # condition to tell the user to choose the correct option when an invalid option has been entered
                    else:
                        print('\nInvalid choice. Choose between option 1-4.\n')
            # creating a condition for when the user chooses option2 in the main menu        
            elif user_input == '2':
                try:
                    # initiating a while loop to prompt the user to give input option (1-3); where option 3 breaks the loop.
                    while True:       
                        # saving the input of the user to a variable worker_salary_option
                        worker_salary_option = input('\n1. Enter worker information \n2. View worker salary information \n'
                                                     '3. Return to main menu \nEnter option 1-3: ')
                        # creating a condition for when the user chooses option1 in the worker salary menu
                        if worker_salary_option == '1':
                            # initiating a while loop to prompt the user to enter the information of each worker until the user inputs 'n' to break the loop
                            while True:
                                try:
                                    # storing each input information from the user about a worker in an intuitive variable name
                                    worker_name = str(input('Enter the name of the worker: '))
                                    worker_hourly_rate = float(input('Enter the hourly rate of the worker: '))
                                    hours_worked = float(input('Enter the number of hours the worker has worked: '))
                                    
                                    # storing the information in 'workers_info' dictionary created in the beginning of this function 
                                    workers_info.update({
                                        'Worker Name' : worker_name, 
                                        'Hourly Rate' : f'${worker_hourly_rate}',
                                        'Hours Worked' : f'{hours_worked}hrs',
                                        'Salary' : f'${worker_salary(worker_hourly_rate, hours_worked)}'
                                    })
                                    # after storing the information in the dictionary, we then append it to 'list_of_workers_info' which was also created at the beginning of the function
                                    list_of_workers_info.append(workers_info.copy())
                                    # prompt user on whether or not to continue entering workers information
                                    continue_entry = str(input("Click 'Enter' to continue entry or 'n' to go back to menu: ")).lower()
                                    # creating a condition for when the user chooses option 'n'
                                    if continue_entry == 'n':
                                        break
                                    # creating a condition for when the user does not pick 'n'
                                    else:
                                        continue
                                # handling errors
                                except ValueError:
                                    print('Invalid input. Make another entry.')
                                    continue
                                    
                        # creating a condition for when the user chooses option2 in the worker salary menu
                        elif worker_salary_option == '2':
                            # initiating a while loop to prompt the user to give input option (1-3); where option 3 breaks the loop.
                            while True:
                                # saving the input of the user to a variable view_salary_option
                                view_salary_option = input('\n1. View worker information \n2. View salary \n'
                                                          '3. Return to previous menu \nEnter option 1-3: ')
                                # creating a condition for when the user chooses option1 in the view worker salary information menu.
                                if view_salary_option == '1': 
                                    # creating a condition for when the list 'list_of_workers_info' is empty
                                    if not list_of_workers_info:
                                        print('No worker data has been entered.')
                                    # creating a condition for when the list 'list_of_workers_info' is not empty
                                    else:
                                        # using a for loop to access each item on the 'list_of_workers_info' list
                                        for worker_info in list_of_workers_info:   
                                            # displaying/printing the workers information
                                            print(f'\nWorker Name: {worker_info["Worker Name"]} \n'
                                                  f'Hourly Rate: {worker_info["Hourly Rate"]}\n'
                                                  f'Hours Worked: {worker_info["Hours Worked"]}\n'
                                                  f'Salary: {worker_info["Salary"]}\n\n')
                                # creating a condition for when the user chooses option2 in the view worker salary information menu.
                                elif view_salary_option == '2':
                                    # creating a condition for when the list 'list_of_workers_info' is empty
                                    if not list_of_workers_info:
                                        print('No data has been entered.')
                                    # creating a condition for when the list 'list_of_workers_info' is  not empty
                                    else:
                                        # using a for loop to access each item on the list 'list_of_workers_info'
                                        for item in list_of_workers_info:
                                            #displaying/printing the workers names and salaries
                                            print(f"\n{item['Worker Name']}:  {item['Salary']}")
                                # creating a condition for when the user chooses option3 in the view worker salary information menu
                                elif view_salary_option == '3':
                                    break
                                # condition to tell the user to choose the correct option when an invalid option has been entered
                                else:
                                    print('Invalid choice. Choose between option 1-3.')
                        # creating a condition for when the user chooses option3 in the worker salary menu
                        elif worker_salary_option == '3':
                            break
                        # condition to tell the user to choose the correct option when an invalid option has been entered
                        else:
                            print('Invalid choice. Choose between option 1-3')
                # error handling
                except ValueError:
                    print('Invalid input.')  
                except UnboundLocalError:
                    print('Data have not been inputted.')
                        
            # creating a condition for when the user chooses option3 in the main menu
            elif user_input == '3':
                # creating a condition for when the list 'daily_cost' is empty
                if not daily_cost:
                    # initiating a while loop to prompt the user to give input for the cost of each item sold
                    while True:
                        try:
                            # saving the input of the user to a variable 'cost_input'
                            cost_input = input('Enter the cost of items sold or enter "#" to proceed: ')
                            
                            # creating a condition for when the user enters '#' to break the loop
                            if cost_input == '#':
                                break
                            # creating a condition for when the user enters anything asides '#'
                            else:
                                # appending user input to the list 'daily_cost' 
                                daily_cost.append(float(cost_input))
                        # error handling
                        except ValueError:
                            print('Invalid input. Make another entry.')
                    # creating a condition for when the list 'daily_sales' is empty
                    if not daily_sales:
                        print('Please go back to option 1 in the main menu to input the sales for both shifts.')
                    # creating a condition for when the list 'daily_sales' not empty
                    else:
                        profit_loss(daily_sales, daily_cost)
                # creating a condition for when the list 'daily_cost' is not empty
                else:
                    # creating a condition for when the list 'daily_sales' is empty
                    if not daily_sales:
                        print('Please go back to option 1 in the main menu to input the sales for both shifts.')
                    # creating a condition for when the list 'daily_sales' is not empty
                    else:
                        profit_loss(daily_sales, daily_cost)

            # creating a condition for when the user chooses option4 in the main menu
            elif user_input == '4':
                try:
                    # using tuple unpacking to hold the variables returned from the function 'shift_tips' 
                    morning_tips, evening_tips, daily_tips = shift_tips(morning_sales, evening_sales)
                    
                    # initiating a while loop to prompt the user to give input option (1-4); where option 4 breaks the loop.
                    while True:
                        # saving input of the user to a variable 'tips_input'
                        tips_input = input('\n1. View morning tips \n2. View evening tips \n3. View daily tips \n'
                                          '4.Return to main menu \nEnter option 1-4: ')
                        # creating a condition for when the user chooses option 1 in the 'tips for a shift' option
                        if tips_input == '1':
                            print(f'Tips for morning workers is \033[1m${morning_tips}\033[0m.')
                        # creating a condition for when the user chooses option 2 in the 'tips for shift' option
                        elif tips_input == '2':
                            print(f'Tips for evening workers is \033[1m${evening_tips}\033[0m.')
                        # creating a condition for when the user chooses option 3 in the 'tips for shift' option
                        elif tips_input == '3':
                            print(f'Total tips for the day is \033[1m${daily_tips}\033[0m.')
                        # creating a condition for when the user chooses option 4 in the 'tips for shift' option
                        elif tips_input == '4':
                            break
                        # condition to tell the user to choose the correct option when an invalid option has been entered
                        else:
                            print('\nInvalid choice. Choose between option 1-4.\n')
                # error handling
                except UnboundLocalError:
                    print('Input the sales data for morning and evening shift.')
                    continue
                except ValueError:
                    print('Invalid input.')
                    continue
                    
            # creating a condition for when the user chooses option5 in the main menu
            elif user_input == '5':
                print('\033[1m\nThanks for using SmartBooks Automation. See you soon!!!\033[0m\n')
                break
            # condition to tell the user to choose the correct option when an invalid option has been entered
            else:
                print('\nInvalid choice. Choose between option 1-5.\n')

    auto_app()
# error handling for when the user tries to interupt the program manually from the keyboard
except KeyboardInterrupt:
    print('\033[1m\nThanks for using SmartBooks Automation. See you soon!!!\n\033[0m')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




