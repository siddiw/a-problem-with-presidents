import processData
import drawgraph

def main():
    dataframe = processData.processData()
    drawgraph.drawGraph(dataframe)
    return 0

if __name__ == "__main__":
    main()