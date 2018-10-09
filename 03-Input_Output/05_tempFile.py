#!/usr/bin/env python3

# # TempFile module
import tempfile

# # Create a temporary file
tempFile = tempfile.TemporaryFile()

# # Write  to a temporary file
tempFile.write(b'Save this special number: 5678309') # b' =  Byte Object
tempFile.seek(0) # volta ao inicio do documento

# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()