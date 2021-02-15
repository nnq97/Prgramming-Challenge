#!/usr/bin/env python3
import json
import pathlib
import sys
import time

import websocket

# Connect to host url
ws = websocket.WebSocket()
host = "wss://echo.websocket.org/"


def main():
    # Create connection
    connection()
    try:
        # Call function to send int, string and json file
        user_input()
    finally:
        # Use ws.close() to close the WebSocket handshake
        ws.close()
        print(f"\n[Connection with {host} is closed]")


def connection():
    print(f"[Connecting to {host}]")
    ws.connect(host)
    time.sleep(1)
    print("[Connected]")


def user_input():
    # Allow users to replaced fixed data
    global num, string, json_file
    n = len(sys.argv)
    if n == 4:
        if not check_int(sys.argv[1]):
            if not check_str(sys.argv[1]):
                print("Invalid. Can only accept one string, json file and integer each")
                sys.exit(1)
            else:
                if not check_file(sys.argv[1]):
                    string = sys.argv[1]
                    if not check_int(sys.argv[2]):
                        if not check_str(sys.argv[2]):
                            print("Invalid. Can only accept one string, json file and integer each")
                            sys.exit(1)
                        else:
                            if not check_file(sys.argv[2]):
                                print("Invalid. No json file")
                                sys.exit(1)
                            else:
                                json_file = sys.argv[2]
                                if not check_int(sys.argv[3]):
                                    print("Invalid. Can only accept one string, json file and integer each")
                                    sys.exit(1)
                                else:
                                    num = sys.argv[3]
                    else:
                        num = sys.argv[2]
                        if not check_str(sys.argv[3]):
                            print("Invalid. Can only accept one string, json file and integer each")
                            sys.exit(1)
                        else:
                            if not check_file(sys.argv[3]):
                                print("Invalid")
                                sys.exit(1)
                            else:
                                json_file = sys.argv[3]
                else:
                    json_file = sys.argv[1]
                    if not check_int(sys.argv[2]):
                        if not check_str(sys.argv[2]):
                            print("Invalid")
                            sys.exit(1)
                        else:
                            if not check_file(sys.argv[2]):
                                string = sys.argv[2]
                                if not check_int(sys.argv[3]):
                                    print("Invalid. Can only accept one string, json file and integer each")
                                    sys.exit(1)
                                else:
                                    num = sys.argv[3]
                            else:
                                print("Invalid")
                                sys.exit(1)
                    else:
                        num = sys.argv[2]
                        if not check_str(sys.argv[3]):
                            print("Invalid. No Double file")
                        else:
                            string = sys.argv[3]
        else:
            num = sys.argv[1]
            if not check_str(sys.argv[2]):
                print("invalid")
                sys.exit(1)
            else:
                if not check_file(sys.argv[2]):
                    string = sys.argv[2]
                    if not check_str(sys.argv[3]):
                        print("invalid")
                        sys.exit(1)
                    else:
                        if not check_file(sys.argv[3]):
                            print("invalid")
                            sys.exit(1)
                        else:
                            json_file = sys.argv[3]
                else:
                    json_file = sys.argv[2]
                    if not check_str(sys.argv[3]):
                        print("invalid")
                        sys.exit(1)
                    else:
                        if not check_file(sys.argv[3]):
                            string = sys.argv[3]
                        else:
                            print("invalid")
                            sys.exit(1)
        # Create connection to server
        time.sleep(0.5)

    else:
        if n != 1:
            print("[Error] Format must be <int> <string> <json file>")
            print("Sending default values")
        else:
            pass

        num = 1234
        string = "hello"
        json_file = "data.json"

    send_int(num)
    send_str(string)
    send_json(json_file)


# Sending Int to echo server
def send_int(v):
    ws.send(str(v))
    print("\nSending number...")
    return echo_data()


# Sending String to echo server
def send_str(v):
    ws.send(v)
    print("\nSending string...")
    return echo_data()


# Sending json object to echo server
def send_json(v):
    with open(f'{v}') as f:
        getjson = json.load(f)
        ws.send(str(getjson))
        print("\nSending json...")
        return echo_data()


# Echo data  from server
def echo_data():
    result = ws.recv()
    print(f"\n[RECEIVED DATA FROM {host}]")
    print(result)
    time.sleep(0.5)
    return result


# Searching for integer in common line arguments
def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Searching for string input in common line arguments
def check_str(s):
    try:
        str(s)
        return True
    except ValueError:
        return False


# Searching for file name in common line arguments
def check_file(s):
    try:
        file = pathlib.Path(s)
        if file.exists():
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
