@echo off
call env\Scripts\activate
uvicorn app.web.interface:app --reload
