First = int(input('Enter number: '))
Second = int(input('Enter number: '))
Third = int(input('Enter number: '))

if (First == Second and Second == Third
        and First == Third):
    print(3)
elif (First == Second or Second == Third
      or First == Third):
    print(2)
else:
    print(0)

