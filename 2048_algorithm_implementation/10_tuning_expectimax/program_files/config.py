import os

##################################################################################
""""
    ONLY THINGS YOU MAY NEED TO CHANGE.
"""

# How many mili seconds to wait after a test case encounters game over.
finish_wait_time = 1

# How many mili seconds to wait before the next move.
time_between_moves = 1


# Be sure to clear the log files before new experimenting as the log files are appended.

##################################################################################










# Filename for CSV Log
global log_filename

log_filename = "/Users/aadityarajk/VS_CODE/2048_unleashed/2048_algorithm_implementation/9_alg_expectimax/logs/2_seed.csv"

random_seed = 2



"""
    Colors or Colours ?
"""

TILE_COLORS = {
    0: "#3c3a32",     
    2: "#a39489",     
    4: "#9c8b7a",     
    8: "#d07c40",     
    16: "#ca6e3e",    
    32: "#c14e34",    
    64: "#bb3320",    
    128: "#b79a32",  
    256: "#b28e2a",   
    512: "#ad8324",   
    1024: "#a7751d",  
    2048: "#a16711",  
}

TEXT_COLORS = {
    0: "#3c3a32",   
    2: "#312821",    
    4: "#3a2f27",    
    8: "#fff8e5",    
    16: "#ffdf8c",   
    32: "#ffb347",  
    64: "#ff6347",   
    128: "#ffec66", 
    256: "#ffcc00", 
    512: "#ffaa00", 
    1024: "#ff8800", 
    2048: "#ff6600", 
}



