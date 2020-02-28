function [ output_args ] = somalgo( input_args )
data=loadjson(input_args);
net=selforgmap([8 8]);
net=train(net,data.numbers);
output=net(data.numbers);
output_args=savejson('output',output);
end

