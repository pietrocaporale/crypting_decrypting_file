# crypting_decrypting_file
This code allows you to encrypt and decrypt any file using a key in turn created by the program.

The operations are performed through the use of openSSL which must already be installed.

The program launches batch files already set up to receive the parameters from the program.

If you want to change the type of encryption/decryption just edit these batch files.

After choosing the file to encrypt it is possible to create a key. This key will be 
created in a text file called pass.txt in the same folder as the file to be encrypted.

When creating a new key, which will be used to encrypt files, its length is requested.

If you don't already have openSSL on your computer at this link you can find the light version of openSSL for Windows.

https://slproweb.com/products/Win32OpenSSL.html

In the dist folder you can find the executable of this software with the bat files included.