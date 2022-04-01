# receives value
seconds = input("Enter the number of seconds you'd like to convert: ")

# conversion from seconds to days, hours, minutes and seconds
days = int((float(seconds))//86400)
rest1 = int((float(seconds))%86400)
hours = int(rest1//3600)
rest2 = int(rest1%3600)
minute = int(rest2//60)
seg = int(rest2%60)

print(f"{days} days, {hours} hours, {minute} minutes and {}seg seconds.")

