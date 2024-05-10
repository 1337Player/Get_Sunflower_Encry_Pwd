print("1.向日葵便携版\n"
      "2.向日葵专业版\n")
id = input("请输入编号：")
if id == "1":
    向日葵便携版 = "C:\\ProgramData\\Oray\\SunloginClientLite\\config.ini"
    fopen = open(向日葵便携版, "r")
    for line in fopen:
        if "encry_pwd" in line:
            print(f"验证码{line}")
            break

    for line2 in fopen:
        if "fastcode" in line2:
            print(f"识别码:{line2}")
            break

    fopen.close()
if id == "2":
    向日葵专业版 = r"C:\ProgramData\Oray\SunloginClient\sys_config.ini"
    fopen = open(向日葵专业版, "r")
    for line in fopen:
        if "encry_pwd" in line:
            print(f"验证码:{line}")
            break

    for line2 in fopen:
        if "fastcode" in line2:
            print(f"识别码:{line2}")
            break

    fopen.close()

if id != "1" and id != "2":
    print("输入错误")