# CompleterArzyabi
پر کردن خودکار فرم ارزیابی اساتید دانشگاه دولتی کاشان

[See on Instagram](https://www.instagram.com/p/BsgN-iTA2Xqx1A8kG92amRlf3PXqGDVk3EDNxs0/)

برای اجرا یادتون نره کتابخانه سلنیوم رو نصب کنید و اگر نیاز به وب درایور داشتید براتون در سورس قرار دادم

# Run with docker

1. First run chrome driver on your machine
    `docker run -d -p 4444:4444 selenium/standalone-chrome`
2. Now place your properties and enjoy!
    `docker run -it -e USER=(your username) -e PASSWORD=(your password) -e SALARY=(نمره استاد) analyze_ostad`
