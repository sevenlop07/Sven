@echo off
title SVEN Depth Video Studio (RTX 3060 CUDA Local Server)
cd /d "%~dp0"
echo ======================================================================
echo   Starting SVEN Depth Video Studio on http://127.0.0.1:7865 ...
echo   GPU Acceleration: NVIDIA CUDA FP16 (Depth Anything V2)
echo ======================================================================
python tools\depth_video_studio.py
pause
