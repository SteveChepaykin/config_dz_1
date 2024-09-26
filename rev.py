def cmdrev(args):
    try:
        arg1 = args[0];
    except:
        print("Requires at least 2 arguments.")
    if arg1 == "-t":
        try:
            print((args[1])[::-1])
        except:
            print("Error in Rev with Text")
    elif arg1 == "-f":
        try:
            
        except:
            print("Error in Rev with File")