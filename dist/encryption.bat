@echo off
echo Sintaxe: encryption ^<name_file^>  ^<.suffix^> ^<.name_pass_file^> - example: encryption document .pdf pass.txt

rem Parameters
set file_name=%1
set suf=%2
set name_pass_file=%3
set file_type=%suf%

rem Validate parameters
if [%1] == [] goto:eof
if [%3] == [] goto:eof

openssl enc -aes-256-cbc -pbkdf2 -p -in %file_name%%file_type% -pass file:%name_pass_file% -out %file_name%%file_type%.enc

echo encrypted %file_name%%file_type% with pass file %name_pass_file% in %file_name%%file_type%.enc
