def calculate_split(total_amount: float, number_of_people: int,splits, currency: str) -> None:
    
    print(f"Total expense: {currency}{total_amount:,.2f}")
    print(f"Number of people: {number_of_people}")
    
    share_amount: list = [round((percent / 100) * total_amount, 2) for percent in splits]
    # share_amount: dict = {i + 1: round((splits[i] / 100) * total_amount, 2) for i in range(len(splits))}

    print("-" * 37)    
    print("Final Breakdown:")
    print(f"{'Persons':<10}{'Split (%)':<12}{'Share Amount':<15}")
    print("-" * 37)
    for i in range(len(share_amount)):
        print(f"{'Person '+ str(i+1):<10}{str(splits[i]) + '%':<12}{f'${share_amount[i]:,.2f}':<15}")
        # print(f"{'Person '+ str(i+1):<10}{str(splits[i]) + '%':<12}{f'${share_amount[i+1]:,.2f}':<15}")
    
    
def proper_input(msg, input_type, min_val=None):
    while True:
        try:
            value = input_type(input(msg))
            
            if min_val is not None and value < min_val:
                print(f"Please enter a value greater than or equal to {min_val}.")
                continue
        
            return int(value) if input_type is int else value

        except ValueError:
            print(f"Invalid input. Please enter a valid {'whole number' if input_type is int else 'number'}.")
            
def get_percentage_input(prompt, max_remaining):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative percentage.")
            elif value > max_remaining:
                print(f"You only have {max_remaining}% remaining to split.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def collect_uneven_splits(num_people,splits):
    splits = []
    total = 0

    for i in range(num_people):
        remaining = 100 - total

        if remaining == 0:
            print("The total split is already 100%.")
            break

        # If it's the last person, auto-calculate their split
        if i == num_people - 1:
            print(f"Person {i + 1} gets the remaining {remaining}%")
            splits.append(remaining)
            total += remaining
            break

        # Ask user for their percentage
        prompt = f"Enter the percentage for person {i + 1} (Remaining: {remaining}%): "
        split = get_percentage_input(prompt, remaining)
        splits.append(split)
        total += split

    if total != 100:
        print(f"Warning: Total split is {total}%, expected 100%.")
    return splits

def main() -> None:
    splits =[]
    try:
        total_amount: float = proper_input("Enter the total amont of expense: ",float,min_val=0)
        number_of_people : int = proper_input("Enter the number of people sharing the expense: ",int,min_val=1)
        
        if number_of_people > 1:
            splits = collect_uneven_splits(number_of_people,splits)
            print(f"Splits: {splits}")
        else:
            splits = [100.0]
            print(f"Only one person they - cover 100% of the cost.")
                
        
        calculate_split(total_amount,number_of_people,splits,currency='$')

        
    except ValueError as e:
        print(f'Error : {e}')
    
if __name__ == '__main__':
    main()