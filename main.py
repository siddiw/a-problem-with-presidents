import process_data
import draw_graph

def main():
    # Processes the input data
    dataframe = process_data.processData()

    # Draws the necessary plots
    draw_graph.drawGraph(dataframe)
    
    return 0

if __name__ == "__main__":
    main()