#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script creates new python scripts"""

# Import the modules needed to run the script.
from time import strftime
import os

title = input("Enter a title for your script withouth the prefix .py: ")

# Add .py to the end of the script.
title = title + '.py'

# Convert all letters to lower case.
title = title.lower()

# Remove spaces from the title.
title = title.replace(' ', '_')

# Details
shebang = "#!/usr/bin/env python"
author = "Miroslav Vidović"
email = "vidovic.miroslav@yahoo.com"
version = "0.1"
status = "Development"

# Set the date automatically.
date = strftime("%d.%m.%Y.")

# Create a file that can be written to.
filename = open(title, 'w')

# Write the data to the new script file.
filename.write(shebang)
filename.write('\n\n')
filename.write('\"\"\" %s : short descripton of what the script does' % (title))
filename.write('\n\n')
filename.write('Longer description\n')
filename.write('\"\"\"' )
filename.write('\n\n')
filename.write('import argparse \n')
filename.write('# Other imports \n\n')
filename.write('__author__ = \"' + author +'\"\n' )
filename.write('__email__ = \"' + email +'\"\n' )
filename.write('__date__ = \"' + date +'\"\n' )
filename.write('__version__ = \"' + version +'\"\n' )
filename.write('__status__ = \"' + status +'\"\n' )
filename.write('\ndef main():\n')
filename.write('    """\n')
filename.write('    Main function\n\n')
filename.write('    """\n')
filename.write('    print("main function")\n\n')
filename.write('if __name__ == \'__main__\': \n')
filename.write('    main()')

# Close the file after writing to it.
filename.close()

# Clear the screen. This line of code will not work on Windows.
os.system("clear")
