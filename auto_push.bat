@echo off
@title windows下批处理git上传演示
set path=%path%; D:\software\Git\cmd
echo\&echo
git add -v .
git commit -m "test"
git push pygame1
echo\&echo done...
pause