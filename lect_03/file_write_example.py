mood_today = input("What's your mood today? ")
num_stars = int(input("Star rating 1 to 5? "))

out_file = open("blog.txt", "a")   # "w" is to overwrite
# "a" is for append

# out_file.write(mood_today + "\n") # must always write a string
# out_file.write(str(num_stars))

out_file.write(f"{mood_today} - {num_stars} stars\n")
out_file.close()

print("--- Updated file ---")