#!/bin/sh

inp_file="input"
if test "$1" = "-t"; then
  inp_file="test-$inp_file"
  shift
fi

part="1"
if test "$2" = "2"; then
  part="2"
fi

cat "day$1/$inp_file" | python "day$1/part$part.py"
