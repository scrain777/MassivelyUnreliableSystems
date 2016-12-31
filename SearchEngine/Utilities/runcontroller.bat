@echo off

Setlocal EnableDelayedExpansion

set /A START="(1%TIME:~0,2%-100)*3600 + (1%TIME:~3,2%-100)*60 + (1%TIME:~6,2%-100)"

for /F "tokens=1,2,3" %%i in (controller.txt) do (
    set CURRENT=!TIME!
    set /A WAIT="((1!CURRENT:~0,2!-100)*3600 + (1!CURRENT:~3,2!-100)*60 + (1!CURRENT:~6,2!-100) - !START! - %%j)"

    if !WAIT! gtr 0 timeout !WAIT!

    if %%k gtr 0 (
        echo Editing %%i
        copy raw\%%i\%%k %%i
    ) else (
        echo Deleting %%i
        del %%i
    )
)
