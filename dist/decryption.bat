@echo off
echo Sintaxe: decryption ^<name_file.enc^> ^<.name_pass_file^> - example: decryption document.pdf.enc pass.txt


rem Parameters
set file_name=%1
set suf=%2
set name_pass_file=%3
set file_type=%suf%


rem Validate parameters
if [%1] == [] goto:eof
if [%3] == [] goto:eof

openssl aes-256-cbc -d -pbkdf2 -in %file_name%.enc -pass file:%name_pass_file% -out %file_name%

echo decrypted %file_name%.enc with pass file %name_pass_file% in %file_name%
