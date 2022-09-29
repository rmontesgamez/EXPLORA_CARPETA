import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

book = open_workbook("C:\\activa\\adibujar\\oferta.xls")
wb = copy(book)

s = wb.get_sheet(0)


style= xlwt.XFStyle()

font = xlwt.Font() 

font.bold = True
font.color_index = 4
font.height = 200
pattern1 = xlwt.Pattern()
pattern1.pattern=pattern1.SOLID_PATTERN
#pattern.pattern_back_colour = 0x00BFBF
pattern1.pattern_fore_colour = 0x32

borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
style.borders = borders
style.font = font
style.pattern= pattern1

lista =["CLIENTE","" ,"NºPedido:","Fecha:", "Plazo:", "Horas O.T.:"]
for i in range(len(lista)):
    s.write(i,0, lista[i],style)

pattern2 = xlwt.Pattern()
pattern2.pattern=pattern2.SOLID_PATTERN
#pattern.pattern_back_colour = 0x00BFBF
pattern2.pattern_fore_colour = 0x32

pattern2.pattern_fore_colour = 0x0E
style.pattern= pattern2

lista = ["Padre","Version Padre", "Hijo", "Version Hijo", "Denominacion", "Material", "Esp.", "Cant.", "Procesos"]


for i in range(len(lista)):
    s.write(7,i, lista[i],style)




wb.save("C:\\activa\\oferta.xls")

