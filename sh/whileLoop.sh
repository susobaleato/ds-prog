#!/bin/bash
##  Copyright 2018, Suso Baleato <jesus.benitez-baleato@uni-konstanz.de>
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
###
####
#####>-
##
##  Description : Example of while statement
##
##  Instructions: bash <script.sh>
##
##  Notes       : Part of the Harvard University Data Science Workshop
##                Introduction to  Programming for Researchers, by the
##                Data Science Services of the Institute for Quantitative
##                Social Science. Workshop material available in:
##                https://github.com/susobaleato
##
#####>-
####
###
##

x=1
while [ $x -le 5 ]
do
    echo "Now I have number $x"
    x=$(( $x + 1 ))
done
