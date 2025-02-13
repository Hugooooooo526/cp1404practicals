"""
read()
readline()
readlines()
for line in file

Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.

In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.

Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. Use with instead of open and close for this question.

Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question.
"""
#1.Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
user_name = input("Give me your name: ")
file_name = user_name + ".txt"

# 使用with语句打开文件，这样可以自动关闭文件，无需手动调用close方法。
with open(file_name, 'w') as out_file:
    out_file.write(user_name)


