clear all;
close all;
clc;
fid = fopen('01stream_sample.txt','r');
datastream = fscanf(fid,'%d');
datastream = datastream';
fclose(fid);
list_counter = [];
list_timestamp = [];
N = 10^2;%window size
r = 2;%the maximum number of bucket for each size;

for i=1:length(datastream)
    time_order = mod(i,N);
    if time_order ==0
        time_order = N;
    end 
    index = [];
    rest_index = find(list_timestamp ~= time_order);
    if length(rest_index) < length(list_timestamp) %evict outdated elements
        new_list_counter = [];
        new_list_timestamp = [];
        new_list_counter = list_counter(rest_index);
        new_list_timestamp = list_timestamp(rest_index);
        list_counter = [];
        list_timestamp = [];
        list_counter = new_list_counter;
        list_timestamp = new_list_timestamp;
    end
    
    x = datastream(i); %newly incoming element
    if x == 1 %store the newly incoming element
        list_length = length(list_counter);
        list_counter(list_length+1) = 1;
        list_timestamp(list_length+1) = time_order;
    end
    delete_flag = 0;
    for index = list_length:-1:1
        bucket_size = list_counter(index);
        if bucket_size ~= -1;
            pos = [];
            pos = find(list_counter == bucket_size);
            if length(pos) == r+1
                list_counter(pos(2)) =  list_counter(pos(2)) + list_counter(pos(1));
                list_timestamp(pos(2)) = list_timestamp(pos(2));
                list_counter(pos(1)) = -1; %mark it -1 to represent that this position is deleted
                list_timestamp(post(1)) = -1;
                delete_flag = 1;
            end
        end
    end
    if delete_flag == 1 %means that we have deleted some buckets
        rest_index = find(list_timestamp ~= -1);
        if length(rest_index) < length(list_timestamp) %evict outdated elements
            new_list_counter = [];
            new_list_timestamp = [];
            new_list_counter = list_counter(rest_index);
            new_list_timestamp = list_timestamp(rest_index);
            list_counter = [];
            list_timestamp = [];
            list_counter = new_list_counter;
            list_timestamp = new_list_timestamp;
        end
    end
end
        
    
            
            
    
    