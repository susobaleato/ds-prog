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
##  Description : Example of summary and plotting
##
##  Instructions: python <script.py>
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

import pandas as pd
# example path for windows (keep the 'r' in front of the string)
df = pd.read_csv(r"C:\Users\cgistest3\Desktop\materials\DSS-IntroProgResearch-20180316\input\GDP-OECD-2017\data\OECD-GDP_20180313_2017.csv")

# example path for standard OS (Linux, OSX)
# df = pd.read_csv("~/folder/file.csv")



df.describe()

import matplotlib.pyplot as plt
from pylab import * 

positions = range(0,len(df.iloc[:,0]))

#fig = plt.subplots( nrows=1, ncols=1,figsize=(6,13) )
figure(1, figsize=(6,13))
barh(positions,df.iloc[:,2],align="center")
yticks(positions,df.iloc[:,0])
xticks(rotation=45)
xlabel('GDP per capita')
title('GDP per capita OECD countries')
#show()
plt.savefig(r"C:\Users\cgistest3\Desktop\materials\DSS-IntroProgResearch-20180316\output\myplot.pdf",format='pdf')
#plt.close(fig)
