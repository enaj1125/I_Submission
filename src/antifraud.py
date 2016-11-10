import csv
import sys
from social_graph import Graph, Node

def main():  
    input_batch, input_stream, outputfile1, outputfile2, outputfile3 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    
    # read in the exsiting data and build a graph
    with open(input_batch, newline ='') as f:
        csvread = csv.reader(f)
        batch_data = [line for line in csvread]

    with open(input_stream, newline ='') as f:
        csvread = csv.reader(f)
        stream_data = [line for line in csvread]

    
    # Build graph from batch data
    PayGraph = Graph() 
    for i in range(1, len(batch_data)):
        try:
            PayGraph.add(batch_data[i][1], batch_data[i][2])

        except Exception as e:  ## check potential errous data 
            print("Error in building graph in line:", i, e)


    # Start processing stream data
    output1 = open(outputfile1, "w")
    output2 = open(outputfile2, "w")    
    output3 = open(outputfile3, "w")

    # Process stream data
    for i in range(1, len(stream_data)):
        print("this is the stream data line:", i, "total lines to process:", len(stream_data)-1)
        
        try:
            result = PayGraph.bfs_search(stream_data[i][1], stream_data[i][2], 1)
            PayGraph.reset()
            flag = "trusted" if result else "unverified"            
            output1.write(flag + "\n")
           
            result = PayGraph.bfs_search(stream_data[i][1], stream_data[i][2], 2)
            PayGraph.reset()
            flag = "trusted" if result else "unverified"   
            output2.write(flag + "\n")

            result = PayGraph.bfs_search(stream_data[i][1], stream_data[i][2], 4)
            PayGraph.reset()
            flag = "trusted" if result else "unverified"   
            output3.write(flag + "\n")
            
            PayGraph.add(stream_data[i][1], stream_data[i][2])

        except Exception as e:
            print("Error in processing stream error in line", i, e)
    
        
if __name__ == '__main__':
    main()
