echo off
cls
title YouTube bot
set botdir=%cd%
for /L %%n in (1,0,10) do (
echo %botdir%\.. && cls && py -3.5 main.py
echo.
echo The application has been stopped, and will restart in 5 seconds.
echo Press Ctrl+C to interrupt the process.
ping -n 5 localhost>nul
)