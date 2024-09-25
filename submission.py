from routefinder import main as routefinder_main
from mars_planner import main as planner_main
from mapcoloring import main as mapcoloring_main

def run_assignment():


    print("\n--- Mars Planner ---")
    planner_main()
    print("\n--- Mars Planner Done ---")

    print("\n--- NEXT ---")

    print("\n--- Route Finder ---")
    routefinder_main()
    print("\n--- Route Finder Done ---")

    print("\n--- NEXT ---")

    print("\n--- Map Coloring ---")
    mapcoloring_main()
    print("\n--- Map Coloring Done ---")



if __name__ == "__main__":
    run_assignment()
