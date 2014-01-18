#!/bin/bash                                                                              
for f in `ls *~`; do
    read -p "delete file $f?" op
    case $op in
        [Yy]* ) rm $f;; 
        [Nn]* )	echo;;
        * ) rm $f;;
    esac
    done

