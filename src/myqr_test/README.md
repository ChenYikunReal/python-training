# myqr库

加上颜色`-c`后报错：
```text
OSError: cannot write mode RGBA as JPEG
```

出问题的代码（源自网络）：
```text
captcha.save('code.jpg')
```
修改方法1：
```text
captcha=captcha.convert('RGB')
captcha.save('code.jpg')
```
修改方法2：
```text
captcha.save('code.png')
```
