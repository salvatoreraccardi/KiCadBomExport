import sys
import builder


#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

#print(sys.argv[2])

#command example:  test.py <bom_file.xml> <CSV | .XLSX> <id_template> <name_new_file>

try:
    if 'csv' in sys.argv[2]:
        builder.csvTool(sys.argv[1], sys.argv[3], sys.argv[4])
    if 'xlsx' in sys.argv[2]:
        builder.xlsxTool(sys.argv[1], sys.argv[3], sys.argv[4])
    if not 'csv' and 'xlsx' in sys.argv[2]:
        print('Oops, extensions available: .CVS or .XLSX')
        
    #print('Your command: ' + sys.argv[1] + ' | ' + sys.argv[2] + ' | ' + sys.argv[3])

except IOError:
    #I can't read/convert this file: ...
    print("Error")    

