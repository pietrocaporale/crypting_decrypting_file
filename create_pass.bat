@echo off
echo Sintaxe: create_pass ^<name_pass_file^> ^<len_pass^>

rem Parameters
set name_pass_file=%1
set pass_len=%2

rem Validate parameters
if [%1] == [] goto:eof
if [%2] == [] set pass_len=64

openssl rand -base64 %pass_len% > %name_pass_file%

echo %name_pass_file% created with %pass_len% characters len

rem pause


