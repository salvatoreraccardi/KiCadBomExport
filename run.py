import sys
import builder 

#command example:  test.py <bom_file.xml> <CSV | .XLSX> <id_template> <name_new_file>

try:
    if sys.argv[1].lower().endswith(('.xml')):

        if 'csv' == sys.argv[2]:
            print('CSV')
            #builder.csvTool(sys.argv[1], sys.argv[3], sys.argv[4])
        if 'xlsx' == sys.argv[2]:
            print('XLSX')
            #builder.xlsxTool(sys.argv[1], sys.argv[3], sys.argv[4])
        else:
            print('ERROR - WRONG COMMAND')
            print('example:  run.py <bom_file.xml> <CSV or XLSX> <id_template> <name_file>')
    else:
        print('ONLY .XML FILES!')
        
    #print('Your command: ' + sys.argv[1] + ' | ' + sys.argv[2] + ' | ' + sys.argv[3])

except IOError:
    #I can't read/convert this file: ...
    print("Error")    

