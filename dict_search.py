import logging


sim_threshold = 0.8 # 查询帧与匹配帧超过此值，loop
key_sim_threshold = 0.6 #v2.0 查询帧与关键帧不过此值，直接丢弃
key_frame_threshold = 0.5 # 与前一关键帧低于此值，加入关键帧
key_frame_find_gup_min = 5 #最小查找关键帧间隔数,当关键帧数量超过5时，开启搜索
key_frame_reject = 3 #拒绝查询帧最近的前三个关键帧

frame_num = 2760
list = range(frame_num)
file_path = '/home/xxx/jsons/'

start = 0
follow = 1
key_frame = [0]#[1] 或者选择第二帧
while follow < frame_num:
    if sim(start, follow)>key_frame_threshold:
        follow +=1
    else:
        key_frame.append(follow) # generate key frames
        start = follow
        follow = start+1
    #************************************************
    # version 1.0  find most similar farme
    #**************Buddha**luck**********************
    #************************************************
    # 关键帧数量达到5，可以向前检索
    if len(key_frame)>key_frame_find_gup_min:
        first_sims = []
        for key_fra in key_frame:
            first_sims.append(sim(follow,key_fra))
        idx = first_sims.index(max(first_sims))

        if idx>0 & len(first_sims)-idx > key_frame_reject:
            second_sims = []
            for frame in range(key_frame(idx-1),key_frame(idx+1)):
                second_sims.append(follow,frame)
            idx = second_sims.index(max(second_sims))

        elif  len(first_sims)-idx < key_frame_reject:
            pass

        elif idx == 0:
            second_sims = []
            for frame in range(key_frame(idx), key_frame(idx + 1)):
                second_sims.append(follow, frame)
            idx = second_sims.index(max(second_sims))

        if second_sims[idx] > sim_threshold:
            with open('test.txt', 'a') as f:  # 打开test.txt   如果文件不存在，创建该文件。
                f.write(str(follow)+' find similar frame '+str(idx)+' score is :'+str(max(second_sims))+'\n')



    '''#version 2.0 find most similar farme 如果关键帧过小，则不进行下一步检索
    if len(key_frame) > key_frame_find_gup_min:
        sims = []
        for key_fra in key_frame:
            sims.append(sim(follow, key_fra))
        if max(sims) > key_sim_threshold:
         #'''


def sim(frame_a, frame_b):
    file_a = file_path + str(frame_a) + '.json'
    file_b = file_path + str(frame_b) + '.json'
    return graph_sim(file_a,file_b)


