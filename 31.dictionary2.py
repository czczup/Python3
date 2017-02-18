#利用字典将两个通讯录文本合并为一个文本
def main():
        ftele2=open('TeleAddressBook.txt','rb')
        ftele1=open('EmailAddressBook.txt','rb')
 
        ftele1.readline()#跳过第一行,第一行是表头
        ftele2.readline()
        lines1 = ftele1.readlines()
        lines2 = ftele2.readlines()
 
        dic1 = {}   #字典方式保存
        dic2 = {}
 
 
        for line in lines1:#获取第一个本文中的姓名和电话信息
                elements = line.split()
                #将文本读出来的bytes转换为str类型
                dic1[elements[0]] = str(elements[1].decode('gbk'))
                 
        for line in lines2:#获取第二个本文中的姓名和电话信息
                elements = line.split()
                dic2[elements[0]] = str(elements[1].decode('gbk'))
 
        ###开始处理###
        lines = []
        lines.append('姓名\t    电话   \t  邮箱\n')
 
        for key in dic1:
            s= ''
            if key in dic2.keys():
                    s = '\t'.join([str(key.decode('gbk')), dic1[key], dic2[key]])
                    s += '\n'   #单引号内为间隔
            else:
                    s = '\t'.join([str(key.decode('gbk')), dic1[key], str('   -----   ')])
                    s += '\n'
            lines.append(s)
             
        for key in dic2:
            s= ''
            if key not in dic1.keys():
                    s = '\t'.join([str(key.decode('gbk')), str('   -----   '), dic2[key]])
                    s += '\n'       
            lines.append(s)
 
        ftele3 = open('AddressBook.txt', 'w')
        ftele3.writelines(lines)
 
        ftele3.close()
        ftele1.close()
        ftele2.close()
        print("The addressBooks are merged!")
 
if __name__ == "__main__":
        main()
#__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
