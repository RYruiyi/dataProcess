objdump --disassembly tool
map.json --The mapping between the driver name and the search path

------------------------------uncalled_funcs.py------------------------------
//** Input parameter **//
--output_path
result .json file output path; zero or one, if user does not input, the script gets the user's current path as the output path.
e.g. --output_path '/home/zuiryi/Item_one/result'

--sourcedir
The path where the user's native folder is located, ends with '/'
e.g. --sourcedir '/home/zruiyi/main/vmkdrivers/native/'

--build 
If user enters a build number, use the entered number; If user does not enter a build number, the script looks for the latest build number.
Zero or one
e.g. --build '13973930'

--driver_name 
The driver name to search for.
One or more, names can be separated by spaces
e.g. --driver_name 'i40en' 'ntg3' 'ne1000'


//** Funtion **//
Find the uncalled functions in the given driver and generate the result .json files.
e.g. 
I.find the uncalled functions in the 'nenic' driver (build number is provided)
$ python uncalled_funcs.py --output_path '/home/zuiryi/Item_one/result' --sourcedir '/home/zuiruiyi/main/vmkdrivers/native/' --build '13973930' --driver_name 'nenic'

II.find the uncalled functions in the 'i40en', 'ntg3', 'ne1000' driver (build and output_path are not provided)
$ python uncalled_funcs.py  --sourcedir '/home/zuiruiyi/main/vmkdrivers/native/' --driver_name 'i40en' 'ntg3' 'ne1000'

#README Git Test
