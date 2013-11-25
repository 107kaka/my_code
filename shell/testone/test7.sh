#!/bin/bash
# testing string equality
testuser=zhuxu

if [ $USER =  $testuser ]
then
	echo "Welcome $testuser"
fi
