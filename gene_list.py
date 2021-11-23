import os


def main():
    sequese = '00'
    frame = 843
    path = "../SG_PR_DATA/graphs_sk/"+sequese
    lenth =len(os.listdir(path))
    path2= "../SG_PR_DATA/eval/3_20/"
    # print(lenth)
    with open(path2+sequese+'.txt', 'w') as f:  # 打开test.txt   如果文件不存在，创建该文件。
        for i in range(lenth):
            if i<10:
                f.write(sequese+'/00000'+str(i)+'.json '+sequese+'/000'+str(frame)+'.json'+'\n')
            elif i<100:
                f.write(sequese + '/0000' + str(i) + '.json ' + sequese + '/000' + str(frame) + '.json'+'\n')
            elif i<1000:
                f.write(sequese + '/000' + str(i) + '.json ' + sequese + '/000' + str(frame) + '.json'+'\n')
            elif i<10000:
                f.write(sequese + '/00' + str(i) + '.json ' + sequese + '/000' + str(frame) + '.json'+'\n')

if __name__ == "__main__":
    main()