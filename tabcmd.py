from pythontabcmd2.context import Context

def main():
    parser = Context.initialize_parsers()
    Context.parse_inputs(parser)

if __name__ == "__main__":
    main()
