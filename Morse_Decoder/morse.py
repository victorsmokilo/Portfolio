

x = input('write hello')

x = open('morse.txt','r')

morse_dict = {}


for line in x:
    line = line.split()
    morse_dict[line[0]] = line[1]
    
x.close()

file = input('Enter the file you want to translate to morse:\n')
myfile = open(file,'r')

translation = []

translation_file = open('translation.txt','w+')

for line in myfile:
    line = line.split()
    for a in range(len(line)):
        for i in range(len(line[a])):
            translation_file.write(morse_dict[line[a][i]])
            translation_file.write('  ')
            if i == len(line[a])-1 and a != len(line) - 1:
                translation_file.write('/')
                translation_file.write('  ')
    translation_file.write('x')
    translation_file.write('  ')



translation_file.close()

