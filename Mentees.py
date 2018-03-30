import os
import shutil
import argparse
# python v 3.6.4

unsubmit = []
mentees = [20181281, 20181433,
           20181296, 20181462,
           20181276, 20181769,
           20181388, 20181712,
           20181753, 20181711,
           20181715, 20181733
           ]

def parse_args():
    parser = argparse.ArgumentParser(description="컴싸 과제 채점 helper")
    parser.add_argument('-d', '--dirname', help="과제 파일(.py)들 있는 폴더명", default='.')
    parser.add_argument('-r', '--run', help="mentees 학생 파일들 실행한다", action='store_true')
    return parser.parse_args()


def search_n_copy(dirname, dest_dir):
    cnt = 0
    filenames = os.listdir(dirname)
    for mentee in mentees:
        found = False
        for file in filenames:
            if str(mentee) in file:
                shutil.copy(dirname+'/'+file, dest_dir)
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

def run_scripts(dir_name, inputfile=None):
    # dir_name안의 모든 .py 스크립트를 실행한다.
    # inputfile로 redirection 가능
    
    file_list = os.listdir(dir_name)

    # 학번으로 정렬
    file_list = sorted(file_list, key=lambda x:x[5:13])

    # 각 학생의 스크립트 실행
    for f in file_list:
        print('{:-^56}'.format(f))
        if inputfile:
            os.system('python '+'"{}"/"{}" < {}'.format(dir_name, f, inputfile))
        else:
            os.system('python '+'"{}"/"{}"'.format(dir_name, f))
        print('-' * 59 + '\n')

if __name__ == "__main__":
    args = parse_args()
    dest_dir = args.dirname+'/'+"Mentees"    # 만들고자 하는 폴더명
    
    makedir(dest_dir)
    search_n_copy(args.dirname, dest_dir)

    if args.run:
        run_scripts(dest_dir)
