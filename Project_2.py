while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    
    match choice:
        case '1':
            print("\nSelect Pattern Type:")
            print("1. Regular Triangle")
            print("2. Inverted Triangle")
            print("3. Number Pyramid")
            pattern_choice = input("Enter pattern choice: ")
            
            rows = int(input("Enter the number of rows for the pattern: "))
            print("\nPattern:")
            
           
            match pattern_choice:
                case '1':
                    for i in range(rows):
                        for j in range(i + 1):
                            print("*", end=" ")
                        print()
                case '2':
                    for i in range(rows):
                        for j in range(rows - i):
                            print("*", end=" ")
                        print()
                case '3':
                    for i in range(rows):
                        for j in range(i + 1):
                            print(i + 1, end=" ")
                        print()
                case _:
                    print("Invalid pattern choice!")
            print()
                
        case '2':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            
            total_sum = 0 
            for num in range(start, end + 1):
                total_sum += num # This line is written using AI
                
        
                match num % 2:# This line is written using AI
                    case 0:
                        print(f"Number {num} is Even")
                    case 1:
                        print(f"Number {num} is Odd")
                    
            print(f"Sum of all numbers from {start} to {end} is: {total_sum}")# This line is written using AI
            print()
            
        case '3':
            print("Exiting the program. Goodbye!")
            break
            
        case _: 
            print("Invalid choice! Please select 1, 2, or 3.\n")
