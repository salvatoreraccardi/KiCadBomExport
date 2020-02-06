import kicad_netlist_reader
import csv
import xlsxwriter
import terminal 
from time import sleep

def csvTool(XmlData, template, name):
    #Next
    print('.XML TO .CSV')
    print('OldDir: ' + XmlData + ' -Template: ' + template+ ' -Name_File: ' + name)

#XLSX Builder    
def xlsxTool(XmlData, template, name):
    row = 1
    #Debug print
    print(terminal.style.YELLOW('.XML TO .XLSX'))
    print('OldDir: ' + XmlData + ' -Template: ' + template + ' -Name_File: ' + name + terminal.style.RESET(''))

    if 't1' in template:
        print(terminal.style.BLUE('Template selected: T1 ~ JLCPCB TEMPLATE') + terminal.style.RESET(''))
        #Create excel file
        workbook = xlsxwriter.Workbook('./export/' + name + '.xlsx') 
        worksheet = workbook.add_worksheet("BOM") 

        #set_column(first_col, last_col, width, cell_format, options)
        title = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
        cell_format = workbook.add_format({'align': 'center'})

        #Comment
        worksheet.write(0, 0, 'Comment', title) 
        worksheet.set_column(0, 0, 35, cell_format)

        #Designator
        worksheet.write(0, 1, 'Designator', title) 
        worksheet.set_column(1, 1, 10, cell_format)

        #Footprint
        worksheet.write(0, 2, 'Footprint', title) 
        worksheet.set_column(2, 2, 90, cell_format)

        #Data pickup from .xml
        net = kicad_netlist_reader.netlist(XmlData)
    
        grouped = net.groupComponents()
        for group in grouped:
            refs = ""

            for component in group:
                refs += component.getRef() + ", "
                c = component
                #print(str(row) + ' | ' + c.getRef() + ' | ' + c.getValue())

                worksheet.write(row, 0, c.getValue()) 
                worksheet.write(row, 1, c.getRef()) 
                worksheet.write(row, 2, c.getFootprint()) 

                row = row + 1  
        print(terminal.style.GREEN('Done!') + terminal.style.RESET(''))          
        workbook.close()