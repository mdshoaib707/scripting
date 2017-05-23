import csv
import os

# Read the data
with open('data.csv', 'rb') as csvfile:
    dd=csv.reader(csvfile, delimiter=',', lineterminator = '\r\n')
    for row in dd:
        print(row)

comm="sed ':a;N;$!ba;s/\\n/;/g' data.csv > dataout.csv"
os.system(comm)

# Reference for this
# https://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed
# Use this solution with GNU sed:
# sed ':a;N;$!ba;s/\n/ /g'
# This will read the whole file in a loop, then replaces the newline(s) with a space.
#
# Explanation:
#
# Create a label via :a.
# Append the current and next line to the pattern space via N.
# If we are before the last line, branch to the created label $!ba ($! means not to do it on the last line as there should be one final newline).
# Finally the substitution replaces every newline with a space on the pattern space (which is the whole file).
# Here is cross-platform compatible syntax which works with BSD sed (as per @Benjie comment):
#
# sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g'
