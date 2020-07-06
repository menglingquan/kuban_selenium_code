import xlrd
class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = 'D:\Kuban\config\logindata.xls'
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows
    def get_data(self):
        result = []
        for i in range(1,self.rows):
            if type(i) == int:
                i = int(i)
                col = self.table.row_values(i)
                result.append(col)
        return result
if __name__ == '__main__':
    eu = ExcelUtil('D:\Kuban\config\logindata.xls')
    p = eu.get_data()
    print(p)