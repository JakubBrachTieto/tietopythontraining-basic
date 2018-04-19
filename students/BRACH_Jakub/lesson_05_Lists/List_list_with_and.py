example_list = ["apples", "bananas", "tofu", "cats"]

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def List_my_list(input_list):
    output_string = ""
    for i in range(len(input_list)-1):
        output_string += input_list[i]+", "
    output_string += "and " + input_list[-1]
    print(output_string)


def Draw_picture(input_picture):
   columns = len(input_picture)
   rows = len(input_picture[0])

   for i in range(rows):
        substring = ""
        for j in range(columns):
           substring += input_picture[j][i]
        print(substring)


#List_my_list(example_list)
#Draw_picture(grid)
