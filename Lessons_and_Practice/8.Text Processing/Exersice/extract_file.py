filename_with_extension = input().split("\\")#разделяме по \
filename, extension = filename_with_extension[-1].split(".")#взимаме последния ел-т от лист по индекс и го раделяме с .
print(f"File name: {filename}")
print(f"File extension: {extension}")