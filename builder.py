import kicad_netlist_reader
import csv
import xlsxwriter 
from time import sleep

def csvTool(XmlData, template, name):
    #Next
    print('.XML TO .CSV')
    print('OldDir: ' + XmlData + ' -Template: ' + template+ ' -Name_File: ' + name)

#XLSX Builder    
def xlsxTool(XmlData, template, name):
    row = 1
    print('.XML TO .XLSX')
    print('OldDir: ' + XmlData + ' -Template: ' + template + ' -Name_File: ' + name)

    #Create excel file
    workbook = xlsxwriter.Workbook('./export/' + name + '.xlsx') 
    worksheet = workbook.add_worksheet("BOM") 
    
    #set_column(first_col, last_col, width, cell_format, options)
    title = workbook.add_format({'bold': True, 'align': 'center'})
    cell_format = workbook.add_format({'align': 'center'})

    #Settings Value cell
    worksheet.write(0, 0, 'Ref', title) 
    worksheet.set_column(0, 0, 10)

    #Settings Value cell
    worksheet.write(0, 1, 'Value', title) 
    worksheet.set_column(1, 1, 35, cell_format)

    #Data pickup from .xml
    net = kicad_netlist_reader.netlist(XmlData)
   
    grouped = net.groupComponents()
    for group in grouped:
        refs = ""

        for component in group:
            refs += component.getRef() + ", "
            c = component
            print(str(row) + ' | ' + c.getRef() + ' | ' + c.getValue())
            #print(c.getRef())
            #print(c.getValue())
            worksheet.write(row, 0, c.getRef()) 
            worksheet.write(row, 1, c.getValue()) 
            #sleep(0.05)
            row = row + 1
        #row = row + 1
    
    workbook.close()
