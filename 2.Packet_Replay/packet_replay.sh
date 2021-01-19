#!/bin/bash

echo ""
echo "==================PACKET REPLAY=================="
echo "This is a packet replay script."
echo "Follow some instructions"
echo "================================================="
echo ""
while :
do
    echo "Select 'Method'"
    printf "1. GET\n"
    printf "2. POST\n"
    read method
    case $method in
        1)  echo ""
            echo "===================GET REPLAY==================="
            exit
            ;;
        2)  echo ""
            echo "===================POST REPLAY=================="
            exit
            ;;
        *)  echo ""
            echo "======================ERROR====================="
            echo "Unknown Command"
            echo ""
    esac
done

echo "Destination IP : "
read method




function print() {
    echo "PRINT your input"$*
}

if [[-f .lock]]; then
    echo "already running..."
else
    touch .lock
    echo "running"
    rm .lock
fi