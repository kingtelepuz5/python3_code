#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################################
#
# Info Section
#
#############################################################################

'''
python script

converts _simple_ SFZ  sound-bank-definition files to   Hydrogen2-drum-machine format.

adjust the input-file name below !
then run the script like:

python sfz_to_h2.py > drumkit.xml

edit drumkit.xml
(h2 does not support sub-directories yet, remove them. copy oga/flac files to same directory)


drumkit.sfz ===> drumkit.h2.xml

Note:
midi note-nr _36_ (c3) will be hydrogen-instrument-id _0_
midi notes below 36 will be appended to the end !


**********************************************************************
* License Info
**********************************************************************

    Copyright (C) Emanuel Rumpf
    Contact:  em-rumpf (at) gmx (.) de

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation,  version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>




'''


#!/usr/bin/python
# -*- coding: utf-8 -*-


#import sys
import re
import os, os.path


# ADJUST INPUT FILE NAME  (will not be modified)
#
#
filename = '1.sf2'

output_file = '1.h2drumkit'
#
#############################################################################



#############################################################################
#
# Start template definitions
#
#############################################################################


# <region>  key=37  offset=0  lovel=0  hivel=127  sample=ogg/beats_09-12.oga

# hydrogen 2 xml-file template

h2tem_head = '''
<drumkit_info>

	<name>Drumkit Name</name>

	<author>Author Name</author>

	<license>License Info + License URL</license>

	<info> Information </info>

	<instrumentList>
	'''

h2tem = '''
		<instrument>
			<id>%s</id>

			<name>%s</name>

			<filename>%s</filename>

			<volume>0.900000</volume>
			<isMuted>false</isMuted>
			<pan_L>1.000000</pan_L>
			<pan_R>1.000000</pan_R>
			<exclude></exclude>
		</instrument>
	'''

h2tem_foot = '''
	</instrumentList>
</drumkit_info>
	'''

# test string (part of an SFZ file)
matchstr = """
		<region>  key=34  offset=0  lovel=0  hivel=127  sample=ogg/beats_01-34.oga
		<region>  key=35  offset=0  lovel=0  hivel=127  sample=ogg/beats_06-50.oga
		// c3 - bass drum 1
		<region>  key=36  offset=0  lovel=0  hivel=127  sample=ogg/beats_06-38.oga
		// c#3 - stick
		<region>  key=37  offset=0  lovel=0  hivel=127  sample=ogg/beats_09-12.oga
		// d3 - snare 1
		<region>  key=38  offset=0  lovel=0  hivel=127  sample=ogg/beats_01-21.oga
	"""


#############################################################################
#
# End template definitions
#
#############################################################################



fcont = ''


def read_file():
	global fcont

	# try:
	f = open( filename, 'rb' )
	fcont = str( f.read() )
	f.close()


def create_match_dic( mat ):

	#print "match : ", mat

	if type( mat ) is tuple:
		m1 = mat[0]
		m2 = mat[1]
	elif ( type( mat ) is str ):
		# is string
		m1 = ''		# comment not given
		m2 = mat
	else:
		print( "Error in create_match_dic() - mat is neither tuple nor string ")
		return

	dd = {}

	s2 = m2.split(' ')
	for k in s2:

		ss = k.strip()

		if ss != '':

			s3 = ss.split('=')
			if len(s3) > 1:
				dd[ s3[0].strip() ] = s3[1].strip()
			#end
		#end

	# note: m1 is set, if there is a comment
	# before the <region> word in the sfz file

	dd['comment'] = m1

	#print " Dic : ", dd

	return dd



def process_file():

	ins_id = '0'
	name = 'bass drum 1'
	filename = 'flac/beats_08-19.flac'

	ret = ''

	# common variables

	# match with comment
	#rawstr_c = r"""\/\/\s?(.*)\s?\n\<region\>(.*)"""
	rawstr_c = r"""\/\/\s?(.*)\s?\n\<region\>([^\<]*)"""

	# match without comment
	#rawstr_n = r"""\<region\>(.*)"""
	rawstr_n = r"""\<region\>([^\<]*)"""

	# embedded_rawstr = r"""(?mx)\<region\>(.*)"""

	global fcont
	matchstr = str( fcont )

	# use a compile object
	re_comp_n = re.compile( rawstr_n,  re.MULTILINE| re.VERBOSE |re.DOTALL )
	re_comp_c = re.compile( rawstr_c,  re.MULTILINE| re.VERBOSE |re.DOTALL )





	# first process matches _with_ comment
	#####################################

	# search pattern
	#match_obj = re_comp_c.search(matchstr)
	matches =  re_comp_c.findall( matchstr )
	#print matches
	#dir( matches )


	# Retrieve group(s) from match_obj
	#all_groups = match_obj.groups()

	# a dic with instrument-id as key and another dic as value,
	# containing name-value mappings for a region
	all_mat = {}

	for mat in matches:
		# matches with comment

		# mDic has name-value mappings for a single region
		mDic = create_match_dic( mat )

		ins_id 		= mDic['key']			# 0
		all_mat[ ins_id ] = mDic

	# end for(mat)




	# now process matches _without_ comment
	#####################################

	# search pattern
	#match_obj = re_comp_n.search(matchstr)
	matches =  re_comp_n.findall(matchstr)
	#print matches
	#dir( matches )

	# Retrieve group(s) from match_obj
	#all_groups = match_obj.groups()

	for mat in matches:
		# matches without comment

		mDic = create_match_dic( mat )

		ins_id 		= mDic['key']			# 0

		if mDic['comment'] == '':
			mDic['comment'] = 'Sample: ' + mDic['sample']

		if ins_id in all_mat:
			pass
			# region was processed in previous match round (with comments)
		else:
			all_mat[ ins_id ] = mDic

	# end for(mat)




	keys = list(all_mat.keys())
	# sort regions (found matches) by instrument id
	keys.sort()

	sorted_out_dic = {}
	last_id = 0

	for k in keys:
		mDic = all_mat[ k ]

		ins_id 		= mDic['key']			# 0
		ins_id_nr	= int(ins_id)
		name 		= mDic['comment']		# bass drum 1
		filename	= mDic['sample']		# flac/beats_08-19.flac

		if int(ins_id) < 36:
			#
			# sfz note 36 is equal hydrogen instrument 0
			# thus we sort out values below 36
			# and append those later
			#
			sorted_out_dic[ ins_id ] = mDic
			continue

		#last_id = ins_id_nr

		temx = h2tem % ( last_id, name, filename )
		ret += temx
		last_id += 1


	keys = list(sorted_out_dic.keys())
	# sort regions (found matches) by instrument id
	keys.sort()
	for k in keys:
		mDic = sorted_out_dic[ k ]

		last_id += 1

		ins_id 		= mDic['key']			# 0
		ins_id_nr	= last_id # int( ins_id) + last_id
		name 		= mDic['comment']		# bass drum 1
		filename	= mDic['sample']		# flac/beats_08-19.flac

		temx = h2tem % ( str(ins_id_nr), name, filename )
		ret += temx



	# FINAL OUTPUT
	#
	output_text = h2tem_head + ret + h2tem_foot

	# print( out )

	global output_file
	# output_file = 'drumkit.h2.xml'

	if os.path.exists( output_file ):
		print( 'NOTE: File NOT written. File %s already exists. ' % output_file )
	else:
		f = open( output_file, 'w+b' )
		# f.write( bytes( output_text, 'UTF-8' ))
		f.write( output_text.encode('UTF-8') )
		f.close()
		#
		print( 'Output file written: ' + output_file )





#############################################################################
#
# Start main function
#
#############################################################################




def main():

	read_file()

	process_file()




if __name__ == '__main__':
	main()





k = """
// 35 Acoustic Bass Drum
36 Bass Drum 1		= h2-instrument 0
37 Side Stick 		= h2-instrument 1
38 Acoustic Snare
39 Hand Clap
40 Electric Snare
41 Low Floor Tom
42 Closed Hi Hat
43 High Floor Tom
44 Pedal Hi-Hat
45 Low Tom
46 Open Hi-Hat
47 Low-Mid Tom
48 Hi-Mid Tom
49 Crash Cymbal 1
50 High Tom
51 Ride Cymbal 1
52 Chinese Cymbal
"""
