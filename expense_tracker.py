import argparse

def main():
    parser = argparse.ArgumentParser(prog="expense-tracker", description="Simple expense tracker")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    #add command
    add_parser = subparsers.add_parser("add", help="Add new log")
    add_parser.add_argument("--description", required=True, help="Description")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount")

    #list command
    subparsers.add_parser("list", help="Listing")

    #delete command
    delete_parser = subparsers.add_parser("delete", help="Delete")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of deleting op")

    #summary command
    summary_parser = subparsers.add_parser("summary", help="Summary")
    summary_parser.add_argument("--month", type=int, help="Month filter")


    #args definition
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()