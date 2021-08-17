#!/usr/bin/env python

import sys
import optparse
import re

def main():
    #Parse Command Line
    parser = optparse.OptionParser()
    parser.add_option( '-p', '--profile', dest='profile', default='', action='store', help='The input file is the MetaPhlAn standard result file' )
    parser.add_option( '-k', '--krona', dest='krona', default='krona.out', action='store', help='the Krona output file name' )
    ( options, spillover ) = parser.parse_args()

    if not options.profile or not options.krona:
        parser.print_help()
        sys.exit()


    metaPhLan = list()
    with open(options.profile,'r') as f:
        metaPhLan = f.readlines()
    f.close()

    krona_tmp = options.krona 
    metaPhLan_FH = open(krona_tmp, 'w')

    for aline in (metaPhLan):
        if not aline.startswith("#"):
            try:
                linesplit = aline.rstrip().split("\t")
                lineage = linesplit[0]
                taxid = int(linesplit[1].split("|")[-1])
                abundance = float(linesplit[-1])
                if lineage.count("s__") <= 1:
                    lineage_full = "\t".join([i.split('__')[1] for i in lineage.split("|")])
                    metaPhLan_FH.write(f"{abundance}\t{lineage_full}\n")
            except ValueError:
                continue

    metaPhLan_FH.close()

if __name__ == '__main__':
    main()