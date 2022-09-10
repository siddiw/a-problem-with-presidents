import process_data
import draw_graph

def main():
    dataframe = process_data.processData()
    draw_graph.drawGraph(dataframe)
    return 0

if __name__ == "__main__":
    main()