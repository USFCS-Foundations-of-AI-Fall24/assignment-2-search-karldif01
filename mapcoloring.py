from ortools.sat.python import cp_model

def main():
    # Instantiate model and solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    ## colors: 0: Red, 1: Blue 2: Green
    #colors = {0 : 'Red',1:'Blue',2:'Green'}
    frequencies = {0 : 'f1', 1:'f2', 2:'f3'}


    Antenna1 = model.NewIntVar(0,2, "A1")
    Antenna2 = model.NewIntVar(0,2, "A2")
    Antenna3 = model.NewIntVar(0,2, "A3")
    Antenna4 = model.NewIntVar(0,2, "A4")
    Antenna5 = model.NewIntVar(0,2, "A5")
    Antenna6 = model.NewIntVar(0,2, "A6")
    Antenna7 = model.NewIntVar(0,2, "A7")
    Antenna8 = model.NewIntVar(0,2, "A8")
    Antenna9 = model.NewIntVar(0,2, "A9")

    model.add(Antenna1 != Antenna2)
    model.add(Antenna1 != Antenna3)
    model.add(Antenna1 != Antenna4)
    model.add(Antenna2 != Antenna3)
    model.add(Antenna2 != Antenna4)
    model.add(Antenna2 != Antenna5)
    model.add(Antenna2 != Antenna6)
    model.add(Antenna3 != Antenna6)
    model.add(Antenna3 != Antenna9)
    model.add(Antenna4 != Antenna5)
    model.add(Antenna6 != Antenna7)
    model.add(Antenna6 != Antenna8)
    model.add(Antenna7 != Antenna8)
    model.add(Antenna8 != Antenna9)

    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Antenna 1: {frequencies[solver.Value(Antenna1)]}")
        print(f"Antenna 2: {frequencies[solver.Value(Antenna2)]}")
        print(f"Antenna 3: {frequencies[solver.Value(Antenna3)]}")
        print(f"Antenna 4: {frequencies[solver.Value(Antenna4)]}")
        print(f"Antenna 5: {frequencies[solver.Value(Antenna5)]}")
        print(f"Antenna 6: {frequencies[solver.Value(Antenna6)]}")
        print(f"Antenna 7: {frequencies[solver.Value(Antenna7)]}")
        print(f"Antenna 8: {frequencies[solver.Value(Antenna8)]}")
        print(f"Antenna 9: {frequencies[solver.Value(Antenna9)]}")

if __name__ == "__main__":
    main()
