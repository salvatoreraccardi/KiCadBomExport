import sys
import builder 
import terminal

#command example:  test.py <bom_file.xml> <CSV | .XLSX> <id_template> <name_new_file>

#ID_TEMPLATE:
#   T1: For JLSCPCB
#       

try:
    if sys.argv[1].lower().endswith(('.xml')):

        if 'csv' == sys.argv[2]:
            print('CSV')
            #builder.csvTool(sys.argv[1], sys.argv[3], sys.argv[4])
        if 'xlsx' == sys.argv[2]:
            builder.xlsxTool(sys.argv[1], sys.argv[3], sys.argv[4])
        if 'xlsx' != sys.argv[2] and 'csv' != sys.argv[2]:
            print(terminal.style.RED('ERROR - WRONG COMMAND'))
            print(terminal.style.YELLOW('example:  run.py <bom_file.xml> <CSV or XLSX> <id_template> <name_file>') + terminal.style.RESET(''))
    else:
        print('ONLY .XML FILES!')
        
except IOError:
    #I can't read/convert this file: ...
    print("Error")    