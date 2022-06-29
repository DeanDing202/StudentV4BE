from django.db import models

# Create your models here.
class Student(models.Model): #--->mysql --->studentv4DB --->student
    gender_choices = (('男', '男'), ('女', '女'))

    sno = models.IntegerField(db_column='SNo', primary_key=True, null=False) #学号-主键，不为空
    sname = models.CharField(db_column='SName', max_length=100, null=False)
    gender = models.CharField(db_column='Gender', max_length=100, choices=gender_choices)
    birthday = models.DateField(db_column='Birthday', null=True)
    mobile = models.CharField(db_column='Mobile', max_length=100, null=True)
    email = models.CharField(db_column='Email', max_length=100, null=True)
    address = models.CharField(db_column='Address', max_length=200, null=True)
    image = models.CharField(db_column="Image", max_length=200,null=True)

    # 原数据
    class Meta:
        managed = True # 这个类是否同步到数据库中的表！True-同步关联，False-不同步
        db_table = 'student' # 定义同步到数据库表的名称，default name：app_class（student_Student）

    # _str_方法: 定义打印格式
    def __str__(self):
        return "学号: %s\t姓名：%s"%(self.sno,self.sname)