# Determinant of matrix 3x3
def matrix_determinant():
 
    count = 0
    row, column = 1, 1

    init_matrix, matrix_upgrader = {}, {count:"Blank"}
    array = []

    represent_matrix = "[a11 , a12 , a13\n a21 , a22 , a23\n a31 , a32 , a33]\n"
    print(f"\nMatrix 3x3 is: \n{represent_matrix}")

    while count < 10:

        user_input = input(f"Enter a{row}{column}:\n")
        number = float(user_input) if '.' in user_input else int(user_input)

        matrix_upgrader[count] = number
        init_matrix.update({count:number})

        if column == 3:
            column = 0
            row += 1

            if row == 4:
                break

        column += 1
        count += 1

    for index in matrix_upgrader:
        array.append(matrix_upgrader[index])

    mat = array
    determinant = (mat[0] * mat[4] * mat[8]) + (mat[1] * mat[5] * mat[6]) + (mat[2] * mat[3] * mat[7]) - (mat[6] * mat[4] * mat[2]) - (mat[7] * mat[5] * mat[0]) - (mat[8] * mat[3] * mat[1])
    matrix = f"[{mat[0]: ^6} , {mat[1]: ^6} , {mat[2]: ^6}\n {mat[3]: ^6} , {mat[4]: ^6} , {mat[5]: ^6}\n {mat[6]: ^6} , {mat[7]: ^6} , {mat[8]: ^6}]\n"

    print(f"\nMatrix 3x3 is: \n{matrix}")
    print(f"Determinant of matrix 3x3 is {determinant:.2f}\n")

matrix_determinant()