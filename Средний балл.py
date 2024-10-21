#Условия задачи:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]

#Преобразуем множество в список и сортируем.
students = (list(students))
students.sort()

#Вычисляем средний балл
AS_Aaron = sum(grades[0]) / len(grades[0])
AS_Bilbo = sum(grades[1]) / len(grades[1])
AS_Johnny = sum(grades[2]) / len(grades[2])
AS_Khendrik = sum(grades[3]) / len(grades[3])
AS_Steve = sum(grades[4]) / len(grades[4])

Average_score = {students[0] : AS_Aaron, students[1] : AS_Bilbo,
                 students[2] : AS_Johnny, students[3] : AS_Khendrik,
                 students[4] : AS_Steve}
print(Average_score)
