# THIS IS MY PSEUDO CODE
# Since this project is quite bigger than the labs, I'll try my best to keep it organized and understandable
# Update: I used ChatGPT to organize the pseudo code, you're welcome. But I specifically told it not to add any new information, 
#only to reorganize what I said into a nice format. And then I went through and made it understandable, I hope.
#
# MAIN IDEA:
# Build a theater seating map as a two-dimensional list sorta like a matrix.
# - 15 rows.
# - 30 seats in each row, i.e., 30 columns.
# - Each seat starts as '#', meaning available.
# - When a seat is sold, change that seat to '@'.
#
# DATA STORAGE
# Keep the current sales information in a dictionary.
# - Store how many sales have happened. i.e., each time a sale happens there will be a counter that adds 1 in a dictionary.
# - Store how many tickets have been sold. i.e., each time a seat is sold there will be a counter that adds 1 in a dictionary.
# - Store total money collected. A dictionary variable will be set to 0.0 at the start and each sale total will be added to it.
# - Store counts of child, adult and senior tickets. another counter will keep track of how many of each type inside the same dictionary.
# - Store a history list so the clerk can review completed sales showing what each one was. This will also be done in a dictionary but a dictionary of lists if that makes sense.
# 
# MENU
# Repeatedly show a menu to the clerk with a while statement probably.
# There will be some options with a user interaction to choose from based on what you told us to have for options
# - Option 1: Sell tickets
# - Option 2: View available seats
# - Option 3: View seating prices
# - Option 4: View current sales
# - Option 5: Close theater
#
# 4. For every menu choice, validate the input before using it.
# - Read input as a string because input() always returns a string.
# - Check whether the string represents an integer because the options are based on an integer input.
# - Keep asking until the clerk enters a valid integer, if it isn't a valid input it just restarts the loop and asks again.
# - Also check whether the integer is inside the allowed range, only 5 options, thus it gotta be 1-5.
#
# 5. For the selling tickets option:
# - Ask how many tickets are in this sale.
# - For each ticket in the sale:
#      a. Ask for row number.
#      b. Ask for seat number.
#      c. Check whether the seat is already sold.
#      c.part b. Check whether row and seat number are within 1-15 and 1-30
#      d. Check whether the same seat was already picked earlier in the same sale.
#      e. Ask for the person's age.
#      f. Determine the base seat price from the row:
#           rows 1-5   -> $12.50
#           rows 6-10  -> $13.50
#           rows 11-15 -> $14.50
#      g. Apply age discount:
#           under 10   -> 35% discount
#           60 or over -> 15% discount
#           otherwise  -> no age discount
#      h. Save the ticket information in a list for this sale. 
#
# 6. After all tickets in the sale are entered (Still part of the selling tickets option):
#    - Add up the discounted ticket prices to get the sale subtotal.
#    - If the sale has 10 or more tickets, apply one overall 20% group discount.
#    - Compute the final sale total.
#    - Mark all chosen seats as sold by changing '#' to '@'.
#    - Update the running sales totals in the dictionary.
#    - Save a sale record in the sales history list.
#    - Display a sale summary to the clerk.
#
# 7. For the viewing available seats option:
#    - Print a seat-number header from 1 to 30.
#    - Print each row with '#' for available seats and '@' for sold seats.
#    - This will all be done with a bunch of loops similar to that one problem from lab 5. I think it was problem like 7 or 8 if I remember right
#
# 8. For the viewing seating prices option:
#    - Print the base prices for each row range.
#    - Print the child, senior and group discount rules.
#
# 9. For the viewing current sales option:
#    - Print total number of completed sales.
#    - Print total tickets sold.
#    - Print child, adult and senior ticket counts.
#    - Print seats remaining.
#    - Print total revenue so far.
#    - Print each individual sale summary from the history list.
#    - All of these prints are using the data in the dictionary
#
# 10. When closing the theater:
#     - Print a final summary of the day's sales just like the above option but minus a few less important information.
#     - Show tickets sold, seats remaining, and total revenue.
#     - End the program loop.
#
#   All of these options along with pretty much everything else will be their own function for simplicity and to not give myself a massive headache.
#   and also cause if I don't then anytime like it calls for the menu screen I'm gonna have to add another 5 print statement lines
#   and this code is gonna be long as heck as it is.

# This function is just to make the initial seating map
def create_seating_map():
    seating_map = []

    for row_number in range(15):
        row = []
        for seat_number in range(30):
            row.append('#')
        seating_map.append(row)

    return seating_map


# THis function will create the initial dictionary of all 0's
def create_sales_data():
    sales_data = {
        'sale_count': 0,
        'tickets_sold': 0,
        'child_tickets': 0,
        'adult_tickets': 0,
        'senior_tickets': 0,
        'total_sales': 0.0,
        'sales_history': []
    }

    return sales_data


# this function just displays the menu to the user
def display_menu():
    print('1. Sell tickets')
    print('2. View available seats')
    print('3. View seating prices')
    print('4. View current sales')
    print('5. Close theater')


# this function is checking if the user inputed an integer or not and if not then returns false
def is_integer_string(text):
    if text == '':
        return False

    start_index = 0

    if text[0] == '-':
        if len(text) == 1:
            return False
        start_index = 1

    for character in text[start_index:]:
        if character < '0' or character > '9':
            return False

    return True


# this function takes a prompt/message, a minimum and maximum value and then asks the user for an integer, if the user give an integer within the range of min-max then it
# returns that integer and if not then it asks for another. This function uses the previous function. Functionseption
def get_valid_int(prompt, minimum, maximum):
    user_text = input(prompt)

    while True:
        if is_integer_string(user_text):
            user_number = int(user_text)

            if user_number >= minimum and user_number <= maximum:
                return user_number
            else:
                print('Input must be between', minimum, 'and', maximum)
        else:
            print('Input must be an integer.')

        user_text = input(prompt)


# this just uses if statements to tell us how much the seat costs for a normal person
def get_base_price(row_number):
    if row_number >= 1 and row_number <= 5:
        return 12.50
    elif row_number >= 6 and row_number <= 10:
        return 13.50
    else:
        return 14.50


# this uses the previous function and then based on the age of the person buying the ticket it
# returns a discounted price (or no discount for normal people) along with the normal price before 
# it also returns the data on the ticket, like the type senior or child. All this data will be used 
# to update the dictionary
def calculate_ticket_price(row_number, age):
    base_price = get_base_price(row_number)
    ticket_type = 'adult'
    final_price = base_price

    if age < 10:
        final_price = base_price * 0.65
        ticket_type = 'child'
    elif age >= 60:
        final_price = base_price * 0.85
        ticket_type = 'senior'

    return final_price, ticket_type, base_price


# This just detects if a seat is available based on a selected row and seat
def seat_is_available(seating_map, row_number, seat_number):
    if seating_map[row_number - 1][seat_number - 1] == '#':
        return True
    else:
        return False


# this will cover the option for seeing the current seats available
def display_available_seats(seating_map):
    print('\nAVAILABLE SEAT MAP')
    print("'#' = available    '@' = sold")
    print()

    print('     ', end='')
    for seat_number in range(1, 31):
        if seat_number < 10:
            print(' ', seat_number, ' ', sep='', end='')
        else:
            print(' ', seat_number, ' ', sep='', end='')# Not sure about the spacing, don't forget to fix/check this
    print()

    for row_index, row in enumerate(seating_map):
        row_number = row_index + 1

        if row_number < 10:
            print('Row ', row_number, ' ', sep='', end='')
        else:
            print('Row ', row_number, sep='', end='')

        for seat_symbol in row:
            print('  ', seat_symbol, ' ', sep='', end='')
        print()



def display_seating_prices():
    """Print the base ticket prices and the discount rules."""
    print('\nSEATING PRICES')
    print('Rows 1 - 5   : $12.50 per ticket')
    print('Rows 6 - 10  : $13.50 per ticket')
    print('Rows 11 - 15 : $14.50 per ticket')
    print()
    print('DISCOUNT RULES')
    print('Children under age 10 receive 35% off')
    print('Seniors age 60 and above receive 15% off')
    print('Groups of 10 or more receive an overall 20% off')



def count_remaining_seats(seating_map):
    """Return how many seats are still available in the theater."""
    remaining_seats = 0

    for row in seating_map:
        for seat_symbol in row:
            if seat_symbol == '#':
                remaining_seats += 1

    return remaining_seats



def sell_tickets(seating_map, sales_data):
    """
    Process one complete sale, update the seating map and update sales totals.
    """
    remaining_seats = count_remaining_seats(seating_map)

    if remaining_seats == 0:
        print('\nThe theater is sold out. No more tickets can be sold.')
        return

    print('\nSELL TICKETS')
    print('There are currently', remaining_seats, 'seats remaining.')

    ticket_count = get_valid_int('How many tickets are in this sale? ', 1, remaining_seats)

    sale_tickets = []
    selected_seats = []

    for ticket_number in range(1, ticket_count + 1):
        print('\nEntering information for ticket', ticket_number)

        while True:
            row_number = get_valid_int('Enter row number (1-15): ', 1, 15)
            seat_number = get_valid_int('Enter seat number (1-30): ', 1, 30)
            seat_choice = (row_number, seat_number)

            if seat_choice in selected_seats:
                print('That seat was already chosen in this sale. Pick a different seat.')
            elif not seat_is_available(seating_map, row_number, seat_number):
                print('That seat is already sold. Pick a different seat.')
            else:
                break

        age = get_valid_int('Enter customer age: ', 0, 120)

        final_price, ticket_type, base_price = calculate_ticket_price(row_number, age)

        ticket_record = {
            'row': row_number,
            'seat': seat_number,
            'age': age,
            'type': ticket_type,
            'base_price': base_price,
            'final_price': final_price
        }

        sale_tickets.append(ticket_record)
        selected_seats.append(seat_choice)

        print('Ticket accepted.')
        print('Seat:', 'Row', row_number, 'Seat', seat_number)
        print('Type:', ticket_type)
        print(f'Price for this ticket: ${final_price:.2f}')

    subtotal = 0.0
    child_count = 0
    adult_count = 0
    senior_count = 0

    for ticket in sale_tickets:
        subtotal += ticket['final_price']

        if ticket['type'] == 'child':
            child_count += 1
        elif ticket['type'] == 'senior':
            senior_count += 1
        else:
            adult_count += 1

    group_discount = 0.0
    if ticket_count >= 10:
        group_discount = subtotal * 0.20

    sale_total = subtotal - group_discount

    for seat_choice in selected_seats:
        row_number, seat_number = seat_choice
        seating_map[row_number - 1][seat_number - 1] = '@'

    sales_data['sale_count'] += 1
    sales_data['tickets_sold'] += ticket_count
    sales_data['child_tickets'] += child_count
    sales_data['adult_tickets'] += adult_count
    sales_data['senior_tickets'] += senior_count
    sales_data['total_sales'] += sale_total

    sale_record = {
        'sale_number': sales_data['sale_count'],
        'ticket_count': ticket_count,
        'child_count': child_count,
        'adult_count': adult_count,
        'senior_count': senior_count,
        'subtotal': subtotal,
        'group_discount': group_discount,
        'total': sale_total,
        'tickets': sale_tickets
    }

    sales_data['sales_history'].append(sale_record)

    print('\nSALE COMPLETE')
    print('Sale number:', sale_record['sale_number'])
    print('Tickets in sale:', ticket_count)
    print('Children:', child_count)
    print('Adults:', adult_count)
    print('Seniors:', senior_count)
    print(f'Subtotal before group discount: ${subtotal:.2f}')
    print(f'Group discount: ${group_discount:.2f}')
    print(f'Final total: ${sale_total:.2f}')



def view_current_sales(seating_map, sales_data):
    """Print a summary of running sales totals and each completed sale."""
    remaining_seats = count_remaining_seats(seating_map)
    total_seats = 15 * 30

    print('\nCURRENT SALES SUMMARY')
    print('Completed sales:', sales_data['sale_count'])
    print('Tickets sold:', sales_data['tickets_sold'])
    print('Child tickets:', sales_data['child_tickets'])
    print('Adult tickets:', sales_data['adult_tickets'])
    print('Senior tickets:', sales_data['senior_tickets'])
    print('Seats remaining:', remaining_seats)
    print('Seats sold:', total_seats - remaining_seats)
    print(f'Total revenue: ${sales_data["total_sales"]:.2f}')

    if len(sales_data['sales_history']) == 0:
        print('No sales have been completed yet.')
    else:
        print('\nINDIVIDUAL SALE RECORDS')
        for sale in sales_data['sales_history']:
            print('--------------------------------------------------')
            print('Sale number:', sale['sale_number'])
            print('Tickets:', sale['ticket_count'])
            print('Children:', sale['child_count'], 'Adults:', sale['adult_count'], 'Seniors:', sale['senior_count'])
            print(f'Subtotal: ${sale["subtotal"]:.2f}')
            print(f'Group discount: ${sale["group_discount"]:.2f}')
            print(f'Sale total: ${sale["total"]:.2f}')
            print('Seats sold in this sale:')

            for ticket in sale['tickets']:
                print('  Row', ticket['row'], 'Seat', ticket['seat'], '-', ticket['type'], f'- ${ticket["final_price"]:.2f}')



def close_theater(seating_map, sales_data):
    """Print the final sales summary for the day and end the program."""
    total_seats = 15 * 30
    remaining_seats = count_remaining_seats(seating_map)
    sold_seats = total_seats - remaining_seats

    print('\n================ FINAL DAILY SUMMARY ================')
    print('Total sales completed:', sales_data['sale_count'])
    print('Total tickets sold   :', sales_data['tickets_sold'])
    print('Child tickets sold   :', sales_data['child_tickets'])
    print('Adult tickets sold   :', sales_data['adult_tickets'])
    print('Senior tickets sold  :', sales_data['senior_tickets'])
    print('Seats sold           :', sold_seats)
    print('Seats remaining      :', remaining_seats)
    print(f'Total revenue        : ${sales_data["total_sales"]:.2f}')
    print('Theater is now closed for the night.')
    print('=====================================================')



def main():
    """Run the theater management application until the clerk closes it."""
    seating_map = create_seating_map()
    sales_data = create_sales_data()
    theater_open = True

    print('Welcome to the ECE 264 Theater Management Application')

    while theater_open:
        display_menu()
        menu_choice = get_valid_int('Enter menu choice (1-5): ', 1, 5)

        if menu_choice == 1:
            sell_tickets(seating_map, sales_data)
        elif menu_choice == 2:
            display_available_seats(seating_map)
        elif menu_choice == 3:
            display_seating_prices()
        elif menu_choice == 4:
            view_current_sales(seating_map, sales_data)
        else:
            close_theater(seating_map, sales_data)
            theater_open = False


# ================================================================
# REPORT / WRITE-UP NOTES
# ================================================================
# FUNCTION PURPOSES AND EXPECTED OUTCOMES
#
# create_seating_map()
# - Purpose: Build the initial 15 x 30 theater seating structure.
# - Expected outcome: Returns a two-dimensional list in which every seat is '#'.
#
# create_sales_data()
# - Purpose: Build the running sales dictionary.
# - Expected outcome: Returns a dictionary with totals set to zero and an empty
#   sales_history list.
#
# display_menu()
# - Purpose: Show the clerk the available menu options.
# - Expected outcome: Prints the five required choices.
#
# is_integer_string(text)
# - Purpose: Check whether an entered string can be treated as an integer.
# - Expected outcome: Returns True for valid integer text and False otherwise.
#
# get_valid_int(prompt, minimum, maximum)
# - Purpose: Safely get integer input from the clerk.
# - Expected outcome: Keeps asking until the clerk enters an integer within the
#   allowed range, then returns that integer.
#
# get_base_price(row_number)
# - Purpose: Determine the base price from the row location.
# - Expected outcome: Returns 12.50, 13.50 or 14.50.
#
# calculate_ticket_price(row_number, age)
# - Purpose: Apply the correct age-based discount to one ticket.
# - Expected outcome: Returns the final ticket price, the ticket type label, and
#   the base price for reporting.
#
# seat_is_available(seating_map, row_number, seat_number)
# - Purpose: Check whether a seat can still be sold.
# - Expected outcome: Returns True if the seat is '#', otherwise False.
#
# display_available_seats(seating_map)
# - Purpose: Show the full theater map.
# - Expected outcome: Prints all rows and seats using '#' and '@'.
#
# display_seating_prices()
# - Purpose: Show the base row prices and discount rules.
# - Expected outcome: Prints pricing information for the clerk.
#
# count_remaining_seats(seating_map)
# - Purpose: Count how many unsold seats are left.
# - Expected outcome: Returns the number of seats marked '#'.
#
# sell_tickets(seating_map, sales_data)
# - Purpose: Handle a complete sale from start to finish.
# - Expected outcome: Validates input, prevents double booking, computes ticket
#   prices and discounts, marks seats sold, updates the sales dictionary, and
#   prints a sale summary.
#
# view_current_sales(seating_map, sales_data)
# - Purpose: Show the current business summary.
# - Expected outcome: Prints totals for revenue, tickets sold, seats remaining,
#   and a breakdown of completed sales.
#
# close_theater(seating_map, sales_data)
# - Purpose: End the day and summarize results.
# - Expected outcome: Prints the final totals for the day.
#
# main()
# - Purpose: Control the entire application.
# - Expected outcome: Repeats the menu until the clerk chooses to close the theater.
#
# ---------------------------------------------------------------
# ANSWERS TO THE FIVE REPORT QUESTIONS
# ---------------------------------------------------------------
# 1. Explain how you could go about validating a user's input in python.
#    One simple way is to read the input as a string first, because input() always
#    returns a string. Then the program can test whether the string has the correct
#    form before converting it to an integer. In this program, the function
#    is_integer_string checks each character one by one to make sure the clerk typed
#    an integer. After that, get_valid_int also checks whether the number is inside
#    the allowed range. If either test fails, the program keeps asking again. This is
#    a safe way to prevent crashes and bad data.
#
# 2. What is the best way to design the theater seating map?
#    The best design here is a two-dimensional list. Each inner list represents one
#    row, and each element inside that row represents one seat. That makes the map
#    easy to create, easy to display, and easy to update. For example,
#    seating_map[row - 1][seat - 1] directly identifies one seat. A '#' means the seat
#    is available and an '@' means the seat has already been sold.
#
# 3. If there is a group of 13 people, 5 children (aged 4 to 9 years), 5 adults,
#    and 3 seniors, what should be the amount they pay if they have seats in row 8
#    of the theater? Explain how the discounts were applied.
#    Row 8 costs $13.50 per ticket.
#    - Child ticket price: 13.50 x 0.65 = 8.775 dollars
#    - Senior ticket price: 13.50 x 0.85 = 11.475 dollars
#    - Adult ticket price: 13.50 dollars
#
#    Cost before group discount:
#    - 5 children: 5 x 8.775  = 43.875
#    - 5 adults  : 5 x 13.50  = 67.50
#    - 3 seniors : 3 x 11.475 = 34.425
#    Subtotal = 43.875 + 67.50 + 34.425 = 145.80
#
#    Because there are 13 people, the sale qualifies for the overall 20% group
#    discount:
#    Group discount = 145.80 x 0.20 = 29.16
#
#    Final amount = 145.80 - 29.16 = 116.64
#
#    So the group should pay $116.64.
#
# 4. Describe two or three test cases you would use to verify that your theater
#    management program works correctly. Explain what each test checks and what
#    the expected result should be.
#
#    Test case 1: Single adult ticket in row 3.
#    - Input: Sell 1 ticket, choose row 3 seat 5, age 25.
#    - Check: Base pricing for rows 1-5 should be used.
#    - Expected result: The ticket price should be $12.50 and the seat should change
#      from '#' to '@'.
#
#    Test case 2: Attempt to buy an already sold seat.
#    - Input: First sell row 4 seat 10. Then try to sell row 4 seat 10 again.
#    - Check: Double booking prevention.
#    - Expected result: The program should reject the second attempt and require a
#      different seat.
#
#    Test case 3: Large mixed group discount sale.
#    - Input: Sell 10 or more tickets with a mix of children, adults and seniors.
#    - Check: Age discounts and overall 20% group discount are both applied.
#    - Expected result: The sale summary should show the subtotal, the group
#      discount amount, and the correct final total.
#
# 5. Think of a new feature that could be added to this application, why do you
#    think it would be useful? And describe how you would implement it.
#    A useful new feature would be ticket cancellation. This would help the clerk if
#    a customer changes plans or if a mistake is made during a sale. To implement it,
#    I would add another menu choice called "Cancel ticket" or "Refund sale." The
#    program would ask for the seat location or the sale number, change those seats
#    from '@' back to '#', subtract the refunded amount from total sales, and reduce
#    the ticket counters. A sales history list is already stored in this program, so the
#    refund information could be found and updated from that list.
# ================================================================


main()
