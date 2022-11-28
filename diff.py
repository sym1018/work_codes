import os
import shutil 

def main():
    path=os.getcwd()+'\\epoch_28'
    path_output_origin=os.getcwd()+'\\diff\\'
    ##file_dir='C:\\Users\\yimin_shao\\Desktop\\temp\\21042_result\\epoch_28'
    print(path)
    print(os.path.exists(path))
    code_names=os.listdir(path)
    for code_1 in code_names:
        code_dir_1=path+'\\'+code_1
        #print(code_dir_1)
        code_names_1=os.listdir(code_dir_1)
        for code_2 in code_names_1:
            code_dir_2=code_dir_1+'\\'+code_2
            #print(code_dir_2)

            
                
            if code_2 != code_1:
                path_output=path_output_origin+'\\'+code_1
                if not os.path.exists(path_output):
                    os.makedirs(path_output)

                if os.path.exists(code_dir_2):
                    # root 所指的是当前正在遍历的这个文件夹的本身的地址
                    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
                    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
                    for root, dirs, files in os.walk(code_dir_2):
                        for file in files:
                            src_file = os.path.join(root, file)
                            shutil.copy(src_file, path_output)
                            print(src_file)
        
        print('finish_'+code_1)



if __name__ == '__main__':
    main()