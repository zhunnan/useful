%% display groundtruth of KITTI poses
% include sequence from 00-10.txt
clear all
% read from poses
filename = '/media/wan/bei/dataset/kiiti00-10/data_odometry_poses/dataset/poses/10.txt';
fid = fopen(filename);
fseek(fid, 0, 'bof');
lastposition = ftell(fid);
disp(['start position:',num2str(lastposition)]);

groundtruth = [];

while fgetl(fid) ~= -1, % end of line check

    fseek(fid, lastposition, 'bof');
    line = textscan(fid,'%f %f %f %f %f %f %f %f %f %f %f %f\n',1);
    line = [line{:}];
    transform = vec2mat(line,4);

    groundtruth = [groundtruth; [transform(1,4), transform(3,4)]];
    lastposition = ftell(fid);
    %disp(['lastposition:',num2str(lastposition)]);

end
save('Matlab/10.mat','groundtruth')
% display ground truth
%load (['/home/wan/2021-4/SG_PR/00pred_db.mat'])
%c = foo;
%scatter(x,y,sz,c,'filled')
%scatter(groundtruth(:,1),groundtruth(:,2),[],c,'filled');
%scatter(groundtruth(:,1),groundtruth(:,2),15,c,'filled');
%colormap jet;
%colorbar;
%fclose(fid);