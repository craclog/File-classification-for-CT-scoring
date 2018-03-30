import os
import shutil
# python v 3.6.4

unsubmit = []
mentees = [20181281, 20181433,
           20181296, 20181462,
           20181276, 20181769,
           20181388, 20181712,
           20181753, 20181711,
           20181715, 20181733
           ]


def search_n_copy(dirname, dest_dir):
    cnt = 0
    filenames = os.listdir(dirname)
    for mentee in mentees:
        found = False
        for file in filenames:
            if str(mentee) in file:
                shutil.copy(file, dest_dir)
                print("File copied :", file)
                found = True
                cnt += 1
        if found == False:
            unsubmit.append(mentee)
    print("{} files copied".format(cnt))
    if unsubmit:
        for mentee in unsubmit:
            print("Cannot find : {}".format(mentee))
        os.system('Pause')

def makedir(dir_name):
    try:
        if not(os.path.isdir(dir_name)):
            os.makedirs(os.path.join(dir_name))
            print("Directory \"{}\" created".format(dir_name))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory")
            raise

if __name__ == "__main__":
    dest_dir = "Mentees"    # 만들고자 하는 폴더명
    makedir(dest_dir)
    search_n_copy('.', dest_dir)
    
